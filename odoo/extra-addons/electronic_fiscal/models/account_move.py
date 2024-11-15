# Estamos importado libreria de odoo las principales de odoo y libreria para generar json codigo qr solutud a la api
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import json
import os
from io import BytesIO
import qrcode
import base64
import requests


# Importamos el archivo que contiene los datos de las facturas de odoo

from .ecf_data import EcfData_E31, EcfData_E32, EcfData_E33, EcfData_E34, EcfData_E41, EcfData_E43, EcfData_E44, EcfData_E45, EcfData_E46, EcfData_E47 # IMPORTAR LA CLASE DE OBTENCIÓN DE DATOS

class AccountMove(models.Model):
    # Extiende la clase 'account.move' para agregar campos y lógica adicional

    _inherit = 'account.move'

    # Campo Booleano para indicar si el comprobante ha sido validado
    validated_ecf = fields.Boolean(default=False)

    # Campo Binario para almacenar el código QR, que será calculado mediante un método
    qr_code = fields.Binary(string="QR Code", compute="generate_qr_code", store=True)

    # Campo Char para almacenar la URL del código QR
    url_qr = fields.Char(string="QR Code URL") 

    # Campo Char para almacenar el código de seguridad
    security_code = fields.Char(string='Security code')

    # Campo Char para almacenar la fecha de firma del comprobante
    signature_date = fields.Char(string='Signature date')

    ecf_environment = fields.Selection(
        selection=[
            ('pruebas', 'Test environment'),
            ('certificacion', 'Certification environment'),
            ('produccion', 'Production environment'),
        ],
        string='Billing environment',
        readonly=True, 
        groups="base.group_system" 
    )

    # Campo para enlazar el ecf correspondiente a la factura
    ecf_record_id = fields.Many2one('ecf.records', string='ecf record')

    # Campo relacionado para mostrar el estado del ecf directamente en la factura
    status = fields.Many2one(
        "ecf.records",
        string="Ecf status",
        readonly=True
    )

    @api.model
    def validate_ecf(self):
        # Método para validar el comprobante basado en su tipo de documento
        for move in self:
            if move.l10n_latam_document_type_id.doc_code_prefix == 'E31':
                fetcher = EcfData_E31(move) # E31
            elif move.l10n_latam_document_type_id.doc_code_prefix == 'E32':
                fetcher = EcfData_E32(move) # E32
            elif move.l10n_latam_document_type_id.doc_code_prefix == 'E33':
                fetcher = EcfData_E33(move) # E33
                datos_referencia = fetcher.fetch_reference_information() 
            elif move.l10n_latam_document_type_id.doc_code_prefix == 'E34':
                fetcher = EcfData_E34(move)# E34
                datos_referencia = fetcher.fetch_reference_information() 
            elif move.l10n_latam_document_type_id.doc_code_prefix == 'E41':
                fetcher = EcfData_E41(move) # E41
            elif move.l10n_latam_document_type_id.doc_code_prefix == 'E43':
                fetcher = EcfData_E43(move) # E43
            elif move.l10n_latam_document_type_id.doc_code_prefix == 'E44':
                fetcher = EcfData_E44(move)  # E44
            elif move.l10n_latam_document_type_id.doc_code_prefix == 'E45':
                fetcher = EcfData_E45(move) # E45
            elif move.l10n_latam_document_type_id.doc_code_prefix == 'E46':
                fetcher = EcfData_E46(move) # E46
            elif move.l10n_latam_document_type_id.doc_code_prefix == 'E47':
                fetcher = EcfData_E47(move) # E47
            # OBTENER LOS DATOS DEL COMPROBANTE, customer, TOTALES Y ITEMS
            datos_comprobante = fetcher.fetch_ecf_data()
            customer_data = fetcher.fetch_customer_data()
            datos_totales = fetcher.fetch_totales_data()
            datos_adicionales = fetcher.fetch_additional_data()
            datos_items = fetcher.fetch_items_data()

            # PROCESO PARA VALIDAR COMPROBANTE
            if move.move_type in ['out_invoice', 'in_invoice', 'out_refund']:
                e_ecf = datos_comprobante
                customer = customer_data
                totales = datos_totales
                items = datos_items
                adicionales = datos_adicionales

                # Proceso para validar el comprobante en función del tipo de movimiento
                if move.l10n_latam_document_type_id.doc_code_prefix in ['E31', 'E32', 'E41', 'E43', 'E44', 'E45', 'E46', 'E47']:

                    datos = {
                        "datos_comprobante": e_ecf,
                        "comprador": customer,
                        "totales": totales,
                        "datos_adicionales": adicionales,
                        "items": items
                    }
                # Definición de los datos según el tipo de documento
                elif move.l10n_latam_document_type_id.doc_code_prefix in ['E33', 'E34']:
                    informacion_referencia = datos_referencia

                    datos = {
                        "datos_comprobante": e_ecf,
                        "comprador": customer,
                        "totales": totales,
                        "datos_adicionales": adicionales,
                        "items": items,
                        "informacion_referencia": informacion_referencia
                    }
                 # En caso de ser E43, solo se procesan algunos campos junto con la referencia
                # elif move.l10n_latam_document_type_id.doc_code_prefix in ['E43']:

                #     datos = {
                #         "datos_comprobante": e_ecf,
                #         "totales": totales,
                #         "datos_adicionales": adicionales,
                #         "items": items,
                #     }
                # Se define la URL del API para enviar los datos del comprobante
                url = "http://54.91.135.223//api/fct/"
                # url = "http://localhost:5000//api//fct/aprobacion"

                self.send_data_to_api(datos, move, url)

    # Llama al método que envía los datos a la API
    def send_data_to_api(self, datos, move, url):
            # Método para enviar los datos del comprobante a una API externa

            # Define la ruta del archivo donde se guardarán los datos en formato JSON
        ecf = move.l10n_latam_document_number
        data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
        file_path = os.path.join(data_dir, f"{ecf}.json")

        try:
            # Escribe los datos en un archivo JSON
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(datos, file, ensure_ascii=False, indent=4)

        # Manejo de excepciones en caso de error al escribir el archivo
        except IOError as e:
            raise UserError(_("Error writing file: %s") % str(e))

        headers = self.get_headers()

        try:

            response = requests.post(url, json=datos, headers=headers)

            if response.status_code == 200:
                
                response_data = response.json()
                response_data = {k.lower(): v for k, v in response_data.items()}

                if 'estado' not in response_data:
                    # Si el campo no está en la respuesta, levanta un UserError
                    raise UserError(_("No status has been received from the DGII, messages: %s") % str(response_data))

                if response_data['estado'] == 'aceptado':
                    move.validated_ecf = True

                elif response_data['estado'] == 'aceptado condicional':
                    move.validated_ecf = True  # Permitir que el proceso continúe
                    # Enviar notificación al usuario utilizando bus
                    self.env['bus.bus']._sendone(
                        self.env.user.partner_id,
                        'notify_info',  # Tipo de notificación (puede cambiar según necesidad)
                        {
                            'title': _("Information"),
                            'message': _("The ecf has been conditionally accepted, message: %s") % str(response_data['mensajes']),
                            'sticky': False  # Indica si la notificación debería quedarse visible
                        }
                    )
                
                elif response_data['estado'] == 'rechazado':
                    move.validated_ecf = False
                    # raise UserError(_("The ecf has been Refused, message: %s") % str(response_data['mensajes']))
                
                if response_data['estado'] == 'rechazado' and 'mensajes' not in response_data:
                    move.validated_ecf = False
                    # raise UserError(_("The ecf has been Refused, message: %s") % str(response_data))

                move.url_qr = response_data.get('url')
                move.security_code = response_data.get('codigoseguridad')
                move.signature_date = response_data.get('fechahorafirma')

                data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
                file_path = os.path.join(data_dir, 'api_response.json')

                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(response_data, file, ensure_ascii=False, indent=4)

                return response_data

            else:

                raise UserError(_("Error sending ecf to API: %s") % response.text)

        except requests.exceptions.RequestException as e:

            raise UserError(_("Connection error when trying to send the ecf to the API: %s") % str(e))

    def action_post(self):
        result = super(AccountMove, self).action_post()

        ecf_record_model = self.env['ecf.records']

        # existing_record = ecf_record_model.search([('ecf_number', '=', ecf_number)], limit=1)

        for move in self:
            if move.move_type in ['out_invoice', 'in_invoice', 'out_refund']:
                move.validate_ecf()
                ecf_record_model.ecf_records_from_api()

                # if not move.validated_ecf:
                #        raise UserError(_("The ecf has not been validated correctly. Please check your details and try again"))

            if move.validate_ecf and move.url_qr:
                self.generate_qr_code()
            # else:
            #      raise UserError(_("Error, the QR has not been generated on the invoice, if the error persists, please contact the administrator"))
        return result

    def get_qr_image(self, move):

        for move in self:
            qr_data = move.url_qr 
        
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=30, border=2)
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Convertir el QR en imagen
        img = qr.make_image(fill='black', back_color='white')
        buffered = BytesIO()
        img.save(buffered, format="PNG")

        # Convertir la imagen a base64 para almacenarla en el modelo
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')  # Asegúrate de decodificar la base64

        return img_str

    @api.depends('partner_id', 'invoice_line_ids', 'amount_total', 'url_qr')  # Asegúrate de incluir url_qr como dependencia
    def generate_qr_code(self):
        for move in self:# Verificar si el url_qr ya tiene valor
            qr_image = self.get_qr_image(move)
            move.qr_code = qr_image  # Almacenar la imagen codificada en base64

    @api.model
    def get_ecf_environment(self):
        # Recupera el valor de DgiiSettings
        settings = self.env['res.config.settings'].sudo().get_values()

        environment = settings.get('ecf_environment')

        return environment

    def get_headers(self):
        settings = self.env['res.config.settings'].sudo().get_values()
        autorization = settings.get('token_api')

        environment = self.get_ecf_environment()

        headers = {'Content-Type': 'application/json'}
        headers['Ambiente'] = environment
        headers['Authorization'] = autorization

        return headers

    @api.onchange('ecf_environment')
    def _onchange_ecf_environment(self):
        # Al crear o editar un account.move, se establece el valor del entorno
        self.ecf_environment = self.get_ecf_environment()

    @api.model
    def create(self, vals):
        # Buscar y enlazar el registro de ecf en función del número
        if vals.get('ecf_number'):
            ecf_record = self.env['ecf.records'].search([('ecf_number', '=', vals['ecf_number'])], limit=1)
            if ecf_record:
                vals['ecf_record_id'] = ecf_record.id
        return super(AccountMove, self).create(vals)
    
    def write(self, vals):
        # Actualizar el enlace del registro ecf si el número de comprobante cambia
        if vals.get('ecf_number'):
            ecf_record = self.env['ecf.records'].search([('ecf_number', '=', vals['ecf_number'])], limit=1)
            if ecf_record:
                vals['ecf_record_id'] = ecf_record.id
        return super(AccountMove, self).write(vals)


