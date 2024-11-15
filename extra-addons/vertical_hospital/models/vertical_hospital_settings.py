from odoo import models, fields, api

class HospitalSettings(models.TransientModel):
    """
    Modelo para gestionar la configuración del hospital.
    """
    _inherit = 'res.config.settings'

    # Campo para almacenar la URL del endpoint
    endpoint_url = fields.Char(string="Endpoint URL")

    @api.model
    def get_values(self):
        """
        Método para obtener los valores de configuración.
        Llama al método super para obtener los valores predeterminados y luego actualiza el valor del endpoint_url.

        :return: Diccionario con los valores de configuración.
        """
        # Llamada al super para obtener valores predeterminados
        res = super(HospitalSettings, self).get_values()

        # Actualiza el valor del endpoint_url desde ir.config_parameter
        res.update({
            'endpoint_url': self.env['ir.config_parameter'].sudo().get_param(
                'hospital.endpoint_url'),
        })

        return res

    def set_values(self):
        """
        Método para establecer los valores de configuración.
        Llama al método super para guardar los valores y luego guarda el valor del endpoint_url en ir.config_parameter.

        :return: None
        """
        # Guardamos el valor en 'ir.config_parameter'
        super(HospitalSettings, self).set_values()

        # Guarda el valor del endpoint_url en ir.config_parameter
        self.env['ir.config_parameter'].sudo().set_param(
            'hospital.endpoint_url', self.endpoint_url)