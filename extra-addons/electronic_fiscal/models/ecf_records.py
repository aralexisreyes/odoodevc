import logging
from odoo import models, fields, api
import os
import json
_logger = logging.getLogger(__name__)

class EcfRecord(models.Model):
    _name = "ecf.records"
    _description = "Ecf Records"

    ecf_number = fields.Char(string='Ecf')
    signature_date = fields.Char(string="Signature date")
    ecf_type = fields.Char(string='ecf Type')
    customer = fields.Char(string='Customer')
    tax = fields.Float(string='ITBIS')
    total_amount = fields.Float(string='Amount Total')
    ecf_message = fields.Char(string="DGII message")
    environment_records = fields.Char(string="Validation environment")

    status = fields.Selection(
        [
        ('Aceptado', 'Accepted'),
        ('Aceptado Condicional', 'Conditionally Accepted'),
        ('Rechazado', 'Refused')
        ], 
        string='Status')

    @api.model
    def ecf_records_from_api(self):

        environment = self.env["res.config.settings"].sudo().get_values()
        environment_records = environment.get("ecf_environment")

        data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
        file_path = os.path.join(data_dir, 'api_response.json')

        try:

            with open(file_path, 'r', encoding='utf-8') as file:

                # Cargar el JSON
                response_data = json.load(file)

                # Convertir las claves a minúsculas
                response_data = {k.lower(): v for k, v in response_data.items()}

            # Validar si se recibieron datos
            if not response_data:
                _logger.warning("No API data received.")
                return False

            ecf_number = response_data.get('encf')
            signature_date = response_data.get('fechahorafirma')
            ecf_type = response_data.get('tipo_ecf')
            customer = response_data.get('customer')
            tax = response_data.get('totalitbis')
            total = response_data.get('total_amount')
            status = response_data.get('estado')
            ecf_message = response_data.get('mensajes')
            

            # Buscar el registro existente en Odoo
            existing_record = self.search([('ecf_number', '=', ecf_number)], limit=1)

            if existing_record:
                # Actualizar el registro existente
                existing_record.write({
                    'signature_date': signature_date,
                    'ecf_type': ecf_type,
                    'customer': customer,
                    'tax': tax,
                    'total_amount': total,
                    'status': status,
                    'ecf_message': ecf_message,
                    'environment_records': environment_records
                })

            else:
                # Crear un nuevo registro
                self.create({
                    'ecf_number': ecf_number,
                    'signature_date': signature_date,
                    'ecf_type': ecf_type,
                    'customer': customer,
                    'tax': tax,
                    'total_amount': total,
                    'status': status,
                    'ecf_message': ecf_message,
                    'environment_records': environment_records
                })


        except Exception as e:
            _logger.error("Error processing ecf records: %s", e)
            return False

