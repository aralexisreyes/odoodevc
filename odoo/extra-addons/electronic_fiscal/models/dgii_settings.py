from odoo import fields, models, api,_
import os
from odoo.exceptions import UserError
import json
import requests
import base64

class DgiiSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ecf_environment = fields.Selection(
        [
            ('prueba', 'Test environment'),
            ('certificacion', 'Certification environment'),
            ('produccion', 'Production environment'),

        ], 
        readonly=False,        
        groups="base.group_system" 
    )

    token_api = fields.Char(string="API Access Token", readonly=True)

    company_data = fields.Many2one('res.company', string="Company")

    autorization_code = fields.Char(string='Authorization code')

    password_p12 = fields.Char(string="Certificate password")

    certificate_p12 = fields.Binary(string="Digital certificate")

    def send_company_data_to_api(self):
        if not self.company_data:
            raise UserError(_("You must select a company to send the data."))

        if not self.autorization_code:
            raise UserError(_("You must provide your authorization code to register data in the API."))

        if not self.password_p12:
            raise UserError(_("You must provide your certificate private key to register the data."))

        # Crear el JSON con los datos de la compañía
        data_company = {
            "data": {
                "rnc": self.company_data.vat or "",
                "razon_social": self.company_data.name or "",
                "nombre_comercial": self.company_data.name or "",
                "direccion": self.company_data.street or "",
                "municipio": self.company_data.city or "",
                "provincia": self.company_data.state_id.name or "",
                "telefono": self.company_data.phone or self.company_data.mobile or "",
                "email": self.company_data.email or "",
                "p12_pss": self.password_p12 or ""
            }
        }

        # Decodifica el archivo binario desde el campo Odoo `certificate_p12`
        binary_archive = base64.b64decode(self.certificate_p12)

        # Crear el diccionario `files` con el archivo binario y el JSON
        files = {
            'archivo_p12': ('certificate.p12', binary_archive, 'application/x-pkcs12'),  # Archivo
            'data': (None, json.dumps(data_company), 'application/json')  # JSON de los datos como cadena
        }

        # URL y encabezados
        url = "http://54.91.135.223/api/admin/verify"
        headers = {
            'Authorizationcode': self.autorization_code  # Código de autorización
        }

        try:
            # Enviar la solicitud `PUT`
            response = requests.put(url, files=files, headers=headers)

            # Procesar la respuesta
            if response.status_code == 200:
                response_data = response.json()
                response_data = {k.lower(): v for k, v in response_data.items()}

                # Guardar la respuesta en un archivo JSON (opcional)
                data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
                response_file_path = os.path.join(data_dir, 'api_record_response.json')


                if response_data.get("authorizationcode") == False and response_data.get("error"):
                    raise UserError(_("An error has occurred: %s") % str(response_data["error"]))

                elif response_data.get("authorizationcode") == False:
                    raise UserError(_("The authorization code is invalid, please try again."))

                else:
                    self.token_api = response_data.get("authorization")

                with open(response_file_path, 'w', encoding='utf-8') as response_file:
                    json.dump(response_data, response_file, ensure_ascii=False, indent=4)

                return response_data

            else:
                raise UserError(_("Error sending data to API: %s") % response.text)

        except requests.exceptions.RequestException as e:
            raise UserError(_("Connection error when trying to send data to the API: %s") % str(e))

    @api.model
    def get_values(self):
        # Llamada al super para obtener valores predeterminados
        res = super(DgiiSettings, self).get_values()
        # Obtenemos el valor guardado en 'ir.config_parameter'
        res.update({
            'ecf_environment': self.env['ir.config_parameter'].sudo().get_param(
                'dgii.ecf_environment', default='prueba'),
            'company_data': int(self.env['ir.config_parameter'].sudo().get_param(
                'dgii.company_data', default=0)) or False,
            'token_api': self.env['ir.config_parameter'].sudo().get_param(
                'dgii.token_api', default=''),
            'certificate_p12': self.env['ir.config_parameter'].sudo().get_param(
                'dgii.certificate_p12', default='')
        })

        return res

    def set_values(self):

        if not self.token_api:
            self.send_company_data_to_api()

        # Guardamos el valor en 'ir.config_parameter'
        super(DgiiSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'dgii.ecf_environment', self.ecf_environment)
        self.env['ir.config_parameter'].sudo().set_param(
            'dgii.company_data', self.company_data.id if self.company_data else False)
        self.env['ir.config_parameter'].sudo().set_param(
            'dgii.token_api', self.token_api or '')
        self.env['ir.config_parameter'].sudo().set_param(
            'dgii.certificate_p12', self.certificate_p12 or '')