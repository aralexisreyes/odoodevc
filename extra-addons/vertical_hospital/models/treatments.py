from odoo import models, fields, api

class VerticalHospitalTreatments(models.Model):
    """
    Modelo para gestionar los tratamientos del hospital.
    """
    _name = 'vertical.hospital.treatments'
    _description = 'Hospital Treatments'

    # Atributos de tratamientos
    treatment_code = fields.Char(string="Codigo de tratamiento", readonly=True)
    treatment_name = fields.Char(string="Nombre del tratamiento")
    treating_doctor = fields.Char(string="Medico tratante")

    @api.model
    def create(self, vals):
        """
        Método para crear un nuevo registro de tratamiento.
        Genera un código de tratamiento único si no está presente.

        :param vals: Diccionario de valores para el nuevo registro.
        :return: El nuevo registro de tratamiento.
        """
        record = super(VerticalHospitalTreatments, self).create(vals)
        if not record.treatment_code:
            treatment_sequence = self.env['ir.sequence'].next_by_code('vertical.hospital.treatments.sequence')
            record.treatment_code = treatment_sequence
        return record

    @api.depends('treatment_code', 'treatment_name')
    def _compute_display_name(self):
        """
        Método para calcular el nombre para mostrar del tratamiento.
        Combina el código de tratamiento y el nombre del tratamiento.

        :return: None
        """
        for record in self:
            record.display_name = f"{record.treatment_code} - {record.treatment_name}"