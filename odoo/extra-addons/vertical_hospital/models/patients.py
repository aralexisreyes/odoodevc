from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class VerticalHospitalPatients(models.Model):
    """
    Modelo para gestionar los pacientes del hospital.
    """
    _name = 'vertical.hospital.patients'
    _description = 'Hospital Patients'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Campos del modelo
    patient_code = fields.Char(string="Codigo de paciente", readonly=True)
    full_name = fields.Char(string="Nombre completo", required=True)
    patient_rnc = fields.Char(string="RNC", required=True)
    treatments_performed = fields.Many2one('vertical.hospital.treatments', string='Treatments performed')
    date_discharge = fields.Datetime(string="Fecha y hora de alta", readonly=True)
    update_date = fields.Datetime(string="Fecha de actualizacion", readonly=True)
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('alta', 'Alta'),
        ('baja', 'Baja')
    ], string="Estado", default='borrador')

    def action_set_active(self):
        """
        Método para cambiar el estado del paciente a 'alta' y asignar la fecha y hora de alta.
        """
        self.state = 'alta'
        self.date_discharge = datetime.now()

    def action_set_inactive(self):
        """
        Método para cambiar el estado del paciente a 'baja'.
        """
        self.state = 'baja'

    @api.model
    def create(self, vals):
        """
        Método para crear un nuevo registro de paciente.
        Asigna la fecha actual a update_date y genera un código de paciente único.

        :param vals: Diccionario de valores para el nuevo registro.
        :return: El nuevo registro de paciente.
        """
        # Asigna la fecha actual a update_date antes de crear el registro
        vals['update_date'] = fields.Datetime.now()

        # Genera un código de paciente único
        vals["patient_code"] = self.env["ir.sequence"].next_by_code(
            "vertical.hospital.patients.sequence")

        return super(VerticalHospitalPatients, self).create(vals)
    
    def write(self, vals):
        """
        Método para actualizar un registro de paciente existente.
        Actualiza la fecha de modificación antes de guardar y registra mensajes si cambian campos específicos.

        :param vals: Diccionario de valores para actualizar el registro.
        :return: El registro de paciente actualizado.
        """
        # Actualiza la fecha de modificación antes de guardar
        vals['update_date'] = fields.Datetime.now()

        for patient in self:
            old_rnc = patient.patient_rnc
            old_state = patient.state

            # Verifica si se ha cambiado el valor de 'patient_rnc'
            if 'patient_rnc' in vals and vals['patient_rnc'] != old_rnc:
                patient.message_post(
                    body=f"Ha cambiado el RNC de {old_rnc} a {vals['patient_rnc']}",
                )

            # Verifica si se ha cambiado el estado
            if 'state' in vals and vals['state'] != old_state:
                patient.message_post(
                    body=f"Ha cambiado el estado de {old_state} a {vals['state']}",
                )

        # Llama al método write original para guardar los cambios
        return super(VerticalHospitalPatients, self).write(vals)

    @api.constrains('patient_rnc')
    def _check_fields(self):
        """
        Método de restricción para validar el campo RNC.
        Verifica que el RNC solo contenga números y tenga una longitud de 9 u 11 caracteres.

        :raises ValidationError: Si el RNC no cumple con las condiciones.
        """
        for record in self:
            if not str(record.patient_rnc).isdigit():
                raise ValidationError("El campo RNC solo puede contener números.")
            elif len(record.patient_rnc) not in [9, 11]:
                raise ValidationError("El campo RNC debe contener 9 u 11 números.")