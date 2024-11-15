
from odoo import models, fields, _
from odoo.exceptions import UserError

import requests

class ElectronicFiscalManagement(models.Model):

    _name = 'electronic.fiscal.management'
    _description = 'Management of electronic fiscal model'

    # Datos del usuario

    user_id = fields.Char(string='Unique Identifier', readonly=True)
    name = fields.Char(string='User Name', readonly=True)
    email = fields.Char(string='Email', readonly=True)
    status = fields.Selection(
        [('active', 'Active'), ('inactive', 'Inactive')],
        string='Status',
        readonly=True
    )
    date_created = fields.Char(string='Creation Date', readonly=True)

    # Estadísticas de uso

    request_count = fields.Char(string='Request Count', readonly=True)
    last_request_date = fields.Datetime(string='Last Request Date',
                                        readonly=True)
    avg_requests_per_day = fields.Char(string='Average Requests per Day',
                                        readonly=True)

    # Controles de seguridad

    auth_token = fields.Char(string='Authentication Token', readonly=True)

    token_expiry_date = fields.Char(string='Token Expiry Date',
                                        readonly=True)

    # Configuración personalizada

    additional_settings = fields.Text(string='Additional Settings',
                                      readonly=True)

    # Auditoria

    account_status = fields.Selection(
        [('blocked', 'Blocked'), ('allowed', 'Allowed')],
        string='Account Status'
    )

    def get_data_from_api(self):

        url = ""
        headers = {}

        try:

            response = requests.get(url, headers=headers)

            if response.status_code == 200:

                response_data = response.json()
                response_data = {k.lower(): v for k, v in
                                 response_data.items()}


                return response_data

            else:
                raise UserError(_("Error sending ecf to API: %s") % response.text)

        except requests.exceptions.RequestException as e:

            raise UserError(
                _("Connection error when trying to send the ecf to the API: %s") % str(
                    e))

        try:
            # Obtener los datos de respuesta
            user_id = response_data.get('user_id')
            name = response_data.get('name')
            email = response_data.get('email')
            status = response_data.get('status')
            date_created = response_data.get('date_created')

            # Estadísticas de uso
            request_count = response_data.get('request_count')
            last_request_date = response_data.get('last_request_date')
            avg_requests_per_day = response_data.get('avg_requests_per_day')

            # Controles de seguridad
            auth_token = response_data.get('auth_token')
            token_expiry_date = response_data.get('token_expiry_date')

            # Configuración personalizada
            additional_settings = response_data.get('additional_settings')

            # Auditoría
            account_status = response_data.get('account_status')

            # Buscar el registro existente en Odoo
            existing_record = self.search([('user_id', '=', user_id)], limit=1)

            if existing_record:
                # Actualizar el registro existente
                existing_record.write({
                    'name': name,
                    'email': email,
                    'status': status,
                    'date_created': date_created,
                    'request_count': request_count,
                    'last_request_date': last_request_date,
                    'avg_requests_per_day': avg_requests_per_day,
                    'auth_token': auth_token,
                    'token_expiry_date': token_expiry_date,
                    'additional_settings': additional_settings,
                    'account_status': account_status
                })
            else:
                # Crear un nuevo registro
                self.create({
                    'user_id': user_id,
                    'name': name,
                    'email': email,
                    'status': status,
                    'date_created': date_created,
                    'request_count': request_count,
                    'last_request_date': last_request_date,
                    'avg_requests_per_day': avg_requests_per_day,
                    'auth_token': auth_token,
                    'token_expiry_date': token_expiry_date,
                    'additional_settings': additional_settings,
                    'account_status': account_status
                })

        except Exception as e:
            return False



