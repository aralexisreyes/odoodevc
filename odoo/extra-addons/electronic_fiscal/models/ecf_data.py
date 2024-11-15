# Importar libreria de odoo y excepciones de usuarios
from odoo.exceptions import UserError
from odoo import _, fields

# Creamos clases para la extraccion de datos por cada tipo de ecf

######### Clase para los datos del ecf tipo E31

class EcfData_E31:
    def __init__(self, move):
        self.common_data = EcfCommonData(move)


    def fetch_ecf_data(self):

        ecf_data = self.common_data._get_ecf_data()

        return ecf_data

    def fetch_customer_data(self):

        customer_data = self.common_data._get_customer_data()

        return customer_data
    
    def fetch_totales_data(self):
        
        data_totales = self.common_data._get_totales_data()

        return data_totales

    def fetch_additional_data(self):
        
        data_totales = self.common_data._get_additional_data()

        return data_totales

    def fetch_items_data(self):

        items_data = self.common_data._get_items() 

        return items_data 

######### Clase para los datos del ecf tipo E32

class EcfData_E32:
    def __init__(self, move):
        self.common_data = EcfCommonData(move)

    def fetch_ecf_data(self):

        ecf_data = self.common_data._get_ecf_data()

        return ecf_data
    
    def fetch_customer_data(self):

        customer_data = self.common_data._get_customer_data()

        return customer_data

    def fetch_totales_data(self):
        
        data_totales = self.common_data._get_totales_data()

        return data_totales

    def fetch_additional_data(self):
        
        data_totales = self.common_data._get_additional_data()

        return data_totales

    def fetch_items_data(self):

        items_data = self.common_data._get_items() 

        return items_data 

######### Clase para los datos del ecf tipo E33

class EcfData_E33:
    def __init__(self, move):
        self.common_data = EcfCommonData(move)

    def fetch_ecf_data(self):

        ecf_data = self.common_data._get_ecf_data()

        return ecf_data

    def fetch_customer_data(self):

        customer_data = self.common_data._get_customer_data()

        return customer_data

    def fetch_totales_data(self):
        
        data_totales = self.common_data._get_totales_data()

        return data_totales

    def fetch_additional_data(self):
        
        data_totales = self.common_data._get_additional_data()

        return data_totales

    def fetch_items_data(self):

        items_data = self.common_data._get_items() 

        return items_data 
    
    def fetch_reference_information(self):

        fetch_reference_information = self.common_data._get_reference_information()

        return fetch_reference_information
    
######### Clase para los datos del ecf tipo E34

class EcfData_E34:
    def __init__(self, move):
        self.common_data = EcfCommonData(move)

    def fetch_ecf_data(self):

        ecf_data = self.common_data._get_ecf_data()

        return ecf_data

    def fetch_customer_data(self):

        customer_data = self.common_data._get_customer_data()

        return customer_data

    def fetch_totales_data(self):
        
        data_totales = self.common_data._get_totales_data()

        return data_totales

    def fetch_additional_data(self):
        
        data_totales = self.common_data._get_additional_data()

        return data_totales

    def fetch_items_data(self):

        items_data = self.common_data._get_items() 

        return items_data 
    
    def fetch_reference_information(self):

        fetch_reference_information = self.common_data._get_reference_information()

        return fetch_reference_information
    

######### Clase para los datos del ecf tipo E41

class EcfData_E41:
    def __init__(self, move):
        self.common_data = EcfCommonData(move)

    def fetch_ecf_data(self):

        ecf_data = self.common_data._get_ecf_data()

        return ecf_data

    def fetch_customer_data(self):

        customer_data = self.common_data._get_customer_data()

        return customer_data

    def fetch_totales_data(self):
        
        data_totales = self.common_data._get_totales_data()

        return data_totales

    def fetch_additional_data(self):
        
        data_totales = self.common_data._get_additional_data()

        return data_totales

    def fetch_items_data(self):

        items_data = self.common_data._get_items() 

        return items_data 

######### Clase para los datos del ecf tipo E43

class EcfData_E43:
    def __init__(self, move):
        self.common_data = EcfCommonData(move)

    def fetch_ecf_data(self):

        ecf_data = self.common_data._get_ecf_data()

        return ecf_data

    def fetch_customer_data(self):

        customer_data = self.common_data._get_customer_data()

        return customer_data

    def fetch_totales_data(self):
        
        data_totales = self.common_data._get_totales_data()

        return data_totales

    def fetch_additional_data(self):
        
        data_totales = self.common_data._get_additional_data()

        return data_totales

    def fetch_items_data(self):

        items_data = self.common_data._get_items() 

        return items_data 

######### Clase para los datos del ecf tipo E44

class EcfData_E44:
    def __init__(self, move):
        self.common_data = EcfCommonData(move)

    def fetch_ecf_data(self):

        ecf_data = self.common_data._get_ecf_data()

        return ecf_data

    def fetch_customer_data(self):

        customer_data = self.common_data._get_customer_data()

        return customer_data

    def fetch_totales_data(self):
        
        data_totales = self.common_data._get_totales_data()

        return data_totales

    def fetch_additional_data(self):
        
        data_totales = self.common_data._get_additional_data()

        return data_totales

    def fetch_items_data(self):

        items_data = self.common_data._get_items() 

        return items_data 

######### Clase para los datos del ecf tipo E45

class EcfData_E45:
    def __init__(self, move):
        self.common_data = EcfCommonData(move)

    def fetch_ecf_data(self):

        ecf_data = self.common_data._get_ecf_data()

        return ecf_data

    def fetch_customer_data(self):

        customer_data = self.common_data._get_customer_data()

        return customer_data

    def fetch_totales_data(self):
        
        data_totales = self.common_data._get_totales_data()

        return data_totales

    def fetch_additional_data(self):
        
        data_totales = self.common_data._get_additional_data()

        return data_totales

    def fetch_items_data(self):

        items_data = self.common_data._get_items() 

        return items_data 

######### Clase para los datos del ecf tipo E46

class EcfData_E46:
    def __init__(self, move):
        self.common_data = EcfCommonData(move)

    def fetch_ecf_data(self):

        ecf_data = self.common_data._get_ecf_data()

        return ecf_data

    def fetch_customer_data(self):

        customer_data = self.common_data._get_customer_data()

        return customer_data

    def fetch_totales_data(self):
        
        data_totales = self.common_data._get_totales_data()

        return data_totales

    def fetch_additional_data(self):
        
        data_totales = self.common_data._get_additional_data()

        return data_totales

    def fetch_items_data(self):

        items_data = self.common_data._get_items() 

        return items_data 

######### Clase para los datos del ecf tipo E47

class EcfData_E47:
    def __init__(self, move):
        self.common_data = EcfCommonData(move)

    def fetch_ecf_data(self):

        ecf_data = self.common_data._get_ecf_data()

        return ecf_data

    def fetch_customer_data(self):

        customer_data = self.common_data._get_customer_data()

        return customer_data

    def fetch_totales_data(self):
        
        data_totales = self.common_data._get_totales_data()

        return data_totales

    def fetch_additional_data(self):
        
        data_totales = self.common_data._get_additional_data()

        return data_totales

    def fetch_items_data(self):

        items_data = self.common_data._get_items() 

        return items_data 
    
# Creamos una clase que contiene todos los datos de las facturas asignados a variables independientes
  
class EcfCommonData:
    def __init__(self, move):
        self.move = move

    def _get_ecf_data(self):

        # Creamos el diccionario base 
        ecf_data = {}
       
        # Establecemos datos fijos segun el ecf

        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E31':
            ecf_data["EcfName"] = 'Factura de Crédito Fiscal Electrónica'
            ecf_data["TipoEcf"] = '31'
        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E32':
            ecf_data["EcfName"] = 'Factura de Consumo Electrónica'
            ecf_data["TipoEcf"] = '32'
        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E33':
            ecf_data["EcfName"] = 'Nota de Débito Electrónica'
            ecf_data["TipoEcf"] = '33'
        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E34':
            ecf_data["EcfName"] = 'Nota de Crédito Electrónica'
            ecf_data["TipoEcf"] = '34'
        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E41':
            ecf_data["EcfName"] = 'Compras Electrónico'
            ecf_data["TipoEcf"] = '41'
        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E43':
            ecf_data["EcfName"] = 'Gastos Menores Electrónico'
            ecf_data["TipoEcf"] = '43'
        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E44':
            ecf_data["EcfName"] = 'Regímenes Especiales Electrónico'
            ecf_data["TipoEcf"] = '44'
        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E45':
            ecf_data["EcfName"] = 'Gubernamental Electrónico'
            ecf_data["TipoEcf"] = '45'
        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E46':
            ecf_data["EcfName"] = 'Comprobante de Exportaciones Electrónico'
            ecf_data["TipoEcf"] = '46'
        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E47':
            ecf_data["EcfName"] = 'Comprobante para Pagos al Exterior Electrónico'
            ecf_data["TipoEcf"] = '47'

        ecf_data["Encf"] = self.move.l10n_latam_document_number

        if self.move.l10n_latam_document_type_id.doc_code_prefix not in ['E32','E34']:
            ecf_data["FechaVencimientoSecuencia"] = self.move.l10n_do_ncf_expiration_date.strftime("%d-%m-%Y")

        if self.move.l10n_latam_document_type_id.doc_code_prefix in ['E34']:
            if self.move.reversed_entry_id and self.move.reversed_entry_id.invoice_date:
            # Calcular la diferencia de días entre la fecha actual y la fecha de emisión del ecf afectado
                diferencia_dias = (fields.Date.today() - self.move.reversed_entry_id.invoice_date).days
                    
                # Asignar "0" si la diferencia es menor o igual a 30 días, "1" si es mayor a 30 días
                if diferencia_dias <= 30:
                    ecf_data["IndicadorNotaCredito"] = '0'
                else:
                    ecf_data["IndicadorNotaCredito"] = '1'
            else:
                ecf_data["IndicadorNotaCredito"] = '0'  # Valor por defecto si no hay factura afectada
 

        if self.move.l10n_latam_document_type_id.doc_code_prefix in ["E31", 'E32', 'E33', 'E34', 'E41', 'E45']:
            if any(tax_group.name == 'ITBIS' for tax_group in self.move.invoice_line_ids.tax_ids.tax_group_id):
                ecf_data["IndicadorMontoGravado"] = '01'
            else:
                ecf_data["IndicadorMontoGravado"] = '0'

        if self.move.l10n_latam_document_type_id.doc_code_prefix not in ['E41', 'E43', 'E47']:

            ecf_data["TipoIngresos"] = self.move.l10n_do_income_type
        
        if self.move.amount_total == 0:
            if self.move.l10n_latam_document_type_id.doc_code_prefix not in ['E34']:
                ecf_data["TipoPago"] = '3'  # Gratuito
        elif self.move.invoice_date_due and self.move.invoice_date_due > self.move.invoice_date:
            ecf_data["TipoPago"] = '2'  # Crédito
        else:
            ecf_data["TipoPago"] = '1'  # Contado

        if self.move.l10n_latam_document_type_id.doc_code_prefix not in ['E43']:
            if self.move.invoice_date < self.move.invoice_date_due:
                ecf_data["FechaLimitePago"] = str(self.move.invoice_date_due)

        return ecf_data
# ----------------------------------------------------------------------------------------    
    def _get_customer_data(self):

        customer_data = {}
      
        customer_data["RNCComprador"] = self.move.partner_id.vat
        customer_data["RazonSocialComprador"] = self.move.partner_id.name  

        if self.move.l10n_latam_document_type_id.doc_code_prefix in ['E46', 'E47']:
            customer_data["IdentificadorExtranjero"] = self.move.partner_id.vat    
            del customer_data["RNCComprador"]

        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E32' and self.move.amount_total < 250000: 
            del customer_data["RNCComprador"]
            del customer_data["RazonSocialComprador"]

        if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E43': 
            del customer_data["RNCComprador"]
            del customer_data["RazonSocialComprador"]

        return customer_data

    def _get_totales_data(self):

        # Creamos el diccionario base
        totales_data = {}

        self.itbis_totales = {"1": 0, "2": 0, "3": 0}
        self.montos_gravados = {"1": 0, "2": 0, "3": 0}
        self.tasas_itbis = {"1": 18, "2": 16, "3": 0}
        self.montos_exentos = {"4": 0}  # Agregar para exentos

        # Montos en pesos (RD$)

        if self.move.currency_id.name == "DOP":

            totales_data["MontoTotal"] = "{:.2f}".format(self.move.amount_total)

            # Solo procesamos si no es uno de los tipos excluidos

            if self.move.l10n_latam_document_type_id.doc_code_prefix not in ['E43', 'E44', 'E47']:
                for line in self.move.invoice_line_ids:
                    # indicador_facturacion = self._get_items(line)
                    impuestos_itbis = [tax for tax in line.tax_ids if tax.tax_group_id.name == 'ITBIS']

                    # Comprobar que no haya más de un impuesto ITBIS
                    if len(impuestos_itbis) > 1:
                        raise UserError(_("Product '%s' has more than one ITBIS tax applied. You can only have one ITBIS tax.") % line.product_id.name)

                    indicador_facturacion = "4"  # Predeterminado para exentos
                    if len(impuestos_itbis) == 1:
                        tax = impuestos_itbis[0]
                        if tax.amount == 18:
                            indicador_facturacion = "1"
                        elif tax.amount == 16:
                            indicador_facturacion = "2"
                        elif tax.amount == 0:
                            indicador_facturacion = "3"

                        itbis_amount = line.price_subtotal * tax.amount / 100
                        self.itbis_totales[indicador_facturacion] += itbis_amount
                        self.montos_gravados[indicador_facturacion] += line.price_subtotal

                    if indicador_facturacion == '4' and self.move.l10n_latam_document_type_id.doc_code_prefix != 'E46':  # Exento de impuestos
                        self.montos_exentos[indicador_facturacion] += line.price_subtotal
                        totales_data["MontoExento"] = "{:.2f}".format(self.montos_exentos.get('4', 0))

                # Total de montos gravados
                totales_data["MontoGravadoTotal"] = "{:.2f}".format(sum(self.montos_gravados.values()))

                # Asignar valores para cada tipo de ITBIS
                for i in range(1, 4):
                    if self.montos_gravados[str(i)] > 0:
                        totales_data[f"MontoGravadoI{i}"] = "{:.2f}".format(self.montos_gravados[str(i)])
                        totales_data[f"ITBIS{i}"] = str(self.tasas_itbis[str(i)])
                        totales_data[f"TotalITBIS{i}"] = "{:.2f}".format(self.itbis_totales[str(i)])

                # Total de ITBIS
                totales_data["TotalITBIS"] = "{:.2f}".format(sum(self.itbis_totales.values()))

            if self.move.l10n_latam_document_type_id.doc_code_prefix in ['E47']:
                totales_data["MontoExento"] = "{:.2f}".format(self.move.amount_total)
                totales_data["TotalISRRetencion"] = "0.00"

            if self.move.l10n_latam_document_type_id.doc_code_prefix in ['E41']:
                totales_data["TotalISRRetencion"] = "0.00"
                totales_data["TotalITBISRetenido"] = "0.00"

            if self.move.l10n_latam_document_type_id.doc_code_prefix in ['E43', 'E44']:
                totales_data["MontoExento"] = "{:.2f}".format(self.move.amount_total)

                # Impuestos adicionales
                tipo_impuesto_adicional_index = 1  # INICIALIZAMOS EL ÍNDICE PARA LOS TIPOS DE IMPUESTOS
                for line in self.move.invoice_line_ids:
                    for tax in line.tax_ids:
                        if tax.tax_group_id.name == 'Propina':
                            totales_data[f"TipoImpuesto[{tipo_impuesto_adicional_index}]"] = "001"
                            tipo_impuesto_adicional_index += 1  # INCREMENTAMOS EL ÍNDICE
                        elif tax.tax_group_id.name == 'CDT':
                            totales_data[f"TipoImpuesto[{tipo_impuesto_adicional_index}]"] = "002"
                            tipo_impuesto_adicional_index += 1  # INCREMENTAMOS EL ÍNDICE

        # Montos en otra moneda

        else:

            totales_data["TipoMoneda"] = self.move.currency_id.name

            totales_data["MontoTotalOtraMoneda"] = "{:.2f}".format(
                self.move.amount_total)

            # Solo procesamos si no es uno de los tipos excluidos

            if self.move.l10n_latam_document_type_id.doc_code_prefix not in ['E43', 'E44', 'E47']:
                for line in self.move.invoice_line_ids:
                    impuestos_itbis = [tax for tax in line.tax_ids if
                                       tax.tax_group_id.name == 'ITBIS']

                    # Comprobar que no haya más de un impuesto ITBIS
                    if len(impuestos_itbis) > 1:
                        raise UserError(_("Product '%s' has more than one ITBIS tax applied. You can only have one ITBIS tax.") % line.product_id.name)

                    indicador_facturacion = "4"  # Predeterminado para exentos
                    if len(impuestos_itbis) == 1:
                        tax = impuestos_itbis[0]
                        if tax.amount == 18:
                            indicador_facturacion = "1"
                        elif tax.amount == 16:
                            indicador_facturacion = "2"
                        elif tax.amount == 0:
                            indicador_facturacion = "3"

                        itbis_amount = line.price_subtotal * tax.amount / 100
                        self.itbis_totales[
                            indicador_facturacion] += itbis_amount
                        self.montos_gravados[
                            indicador_facturacion] += line.price_subtotal

                    if indicador_facturacion == '4' and self.move.l10n_latam_document_type_id.doc_code_prefix != 'E46':  # Exento de impuestos
                        self.montos_exentos[
                            indicador_facturacion] += line.price_subtotal
                        totales_data["MontoExentoOtraMoneda"] = "{:.2f}".format(
                            self.montos_exentos.get('4', 0))

                # Total de montos gravados
                totales_data["MontoGravadoTotalOtraMoneda"] = "{:.2f}".format(
                    sum(self.montos_gravados.values()))

                # Asignar valores para cada tipo de ITBIS
                for i in range(1, 4):
                    if self.montos_gravados[str(i)] > 0:
                        totales_data[f"MontoGravado{i}OtraMoneda"] = "{:.2f}".format(
                            self.montos_gravados[str(i)])
                        totales_data[f"TotalITBIS{i}OtraMoneda"] = "{:.2f}".format(
                            self.itbis_totales[str(i)])

                # Total de ITBIS
                totales_data["TotalITBISOtraMoneda"] = "{:.2f}".format(
                    sum(self.itbis_totales.values()))

            if self.move.l10n_latam_document_type_id.doc_code_prefix in ['E47']:
                totales_data["MontoExentoOtraMoneda"] = "{:.2f}".format(
                    self.move.amount_total)

            if self.move.l10n_latam_document_type_id.doc_code_prefix in ['E43','E44']:

                totales_data["MontoExentoOtraMoneda"] = "{:.2f}".format(
                    self.move.amount_total)

                # Impuestos adicionales
                tipo_impuesto_adicional_index = 1  # INICIALIZAMOS EL ÍNDICE PARA LOS TIPOS DE IMPUESTOS
                for line in self.move.invoice_line_ids:
                    for tax in line.tax_ids:
                        if tax.tax_group_id.name == 'Propina':
                            totales_data[
                                f"TipoImpuestoOtraMoneda[{tipo_impuesto_adicional_index}]"] = "001"
                            tipo_impuesto_adicional_index += 1  # INCREMENTAMOS EL ÍNDICE
                        elif tax.tax_group_id.name == 'CDT':
                            totales_data[
                                f"TipoImpuestoOtraMoneda[{tipo_impuesto_adicional_index}]"] = "002"
                            tipo_impuesto_adicional_index += 1  # INCREMENTAMOS EL ÍNDICE

        return totales_data

#---------------------------------------------------------------

    def _get_items(self):

        items_data = {}
        monto_isr_total = 0

        # Montos en pesos (DOP)

        if self.move.currency_id.name == "DOP":
            
            for index, line in enumerate(self.move.invoice_line_ids, start=1):
                nombre_item = line.product_id.name
                numero_secuencia = str(index)
                impuestos_itbis = [tax for tax in line.tax_ids if tax.tax_group_id.name == 'ITBIS']
                if len(impuestos_itbis) > 1:
                    raise UserError(_("Product '%s' has more than one ITBIS tax applied. You can only have one ITBIS tax.") % nombre_item)

                if len(impuestos_itbis) == 1:
                    tax = impuestos_itbis[0]
                    if tax.amount == 18:
                        indicador_facturacion = "1"
                    elif tax.amount == 16:
                        indicador_facturacion = "2"
                    elif tax.amount == 0:
                        indicador_facturacion = "3"
                else:
                    indicador_facturacion = "4"

                if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E46':
                    if not impuestos_itbis or tax.amount != [0]:
                        raise UserError(_("The ecf type E46 must have itbis of 0% (Not billable)"))

                if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E44':
                    if impuestos_itbis:
                        raise UserError(_("Ecf type E44 cannot contain ITBIS"))

                if line.product_id.type in ['consu', 'product', 'set']:
                    indicador_bien_o_servicio = "1"
                elif line.product_id.type == 'service':
                    indicador_bien_o_servicio = "2"
                else:
                    indicador_bien_o_servicio = "1"

                impuestos_isr = [tax for tax in line.tax_ids if
                                tax.tax_group_id.name == 'ISR']

                if len(impuestos_itbis) > 1:
                    raise UserError(
                        _("Product '%s' has more than one withholding (27%) applied. You can only have one.") % nombre_item)

                indicador_facturacion_retencion_o_percepcion = "1"
                
                items_data[numero_secuencia] = {
                    "NombreItem": nombre_item,
                    "NumeroSecuencia": numero_secuencia,
                    "IndicadorFacturacion": indicador_facturacion,
                    "IndicadorAgenteRetencionoPercepcion": indicador_facturacion_retencion_o_percepcion,
                    "MontoITBISRetenido": "0.00",
                    "MontoISRRetenido": "0.00",
                    "CantidadItem": "{:.0f}".format(line.quantity),
                    "PrecioUnitarioItem": "{:.2f}".format(line.price_unit),
                    "MontoItem": "{:.2f}".format(line.price_subtotal),
                    "IndicadorBienOServicio": indicador_bien_o_servicio
                }

                if indicador_facturacion == "4" and indicador_facturacion_retencion_o_percepcion == "1":
                    items_data[numero_secuencia]["MontoITBISRetenido"] = '0.00'

                if impuestos_isr:
                    tax = impuestos_isr[0]
                    isr_27_amount = line.price_subtotal * tax.amount / 100
                    items_data[numero_secuencia]["MontoISRRetenido"] = "{:.2f}".format(isr_27_amount)
                    monto_isr_total += isr_27_amount  # SUMA EL MONTO ISR A LA VARIABLE ACUMULADORA

                if self.move.l10n_latam_document_type_id.doc_code_prefix in ['E31', 'E32', 'E33', 'E34','E43','E44', 'E45', 'E46']:
                    del items_data[numero_secuencia]["IndicadorAgenteRetencionoPercepcion"]
                    del items_data[numero_secuencia]["MontoITBISRetenido"]
                    del items_data[numero_secuencia]["MontoISRRetenido"]

                if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E47':
                    del items_data[numero_secuencia]["MontoITBISRetenido"]

        # Montos en otra moneda

        else:

            for index, line in enumerate(self.move.invoice_line_ids, start=1):
                nombre_item = line.product_id.name
                numero_secuencia = str(index)
                impuestos_itbis = [tax for tax in line.tax_ids if tax.tax_group_id.name == 'ITBIS']
                if len(impuestos_itbis) > 1:
                    raise UserError(_("Product '%s' has more than one ITBIS tax applied. You can only have one ITBIS tax.") % nombre_item)

                if len(impuestos_itbis) == 1:
                    tax = impuestos_itbis[0]
                    if tax.amount == 18:
                        indicador_facturacion = "1"
                    elif tax.amount == 16:
                        indicador_facturacion = "2"
                    elif tax.amount == 0:
                        indicador_facturacion = "3"
                else:
                    indicador_facturacion = "4"

                if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E46':
                    if not impuestos_itbis or tax.amount != [0]:
                        raise UserError(
                            _("The ecf type E46 must have itbis of 0% (Not billable)"))

                if line.product_id.type in ['consu', 'product', 'set']:
                    indicador_bien_o_servicio = "1"
                elif line.product_id.type == 'service':
                    indicador_bien_o_servicio = "2"
                else:
                    indicador_bien_o_servicio = "1"

                impuestos_isr = [tax for tax in line.tax_ids if
                                tax.tax_group_id.name == 'ISR']

                if len(impuestos_itbis) > 1:
                    raise UserError(_("Product '%s' has more than one withholding (27%) applied. You can only have one.") % nombre_item)

                indicador_facturacion_retencion_o_percepcion = "1"

                items_data[numero_secuencia] = {
                    "NombreItem": nombre_item,
                    "NumeroSecuencia": numero_secuencia,
                    "IndicadorFacturacion": indicador_facturacion,
                    "IndicadorAgenteRetencionoPercepcion": indicador_facturacion_retencion_o_percepcion,
                    "MontoITBISRetenido": "0.00",
                    "MontoISRRetenido": "0.00",
                    "CantidadItem": "{:.0f}".format(line.quantity),
                    "PrecioOtraMoneda": "{:.2f}".format(line.price_unit),
                    "MontoItemOtraMoneda": "{:.2f}".format(line.price_subtotal),
                    "IndicadorBienOServicio": indicador_bien_o_servicio
                }

                if indicador_facturacion == "4" and indicador_facturacion_retencion_o_percepcion == "1":
                    items_data[numero_secuencia]["MontoITBISRetenido"] = '0.00'

                if impuestos_isr:
                    tax = impuestos_isr[0]
                    isr_27_amount = line.price_subtotal * tax.amount / 100
                    items_data[numero_secuencia]["MontoISRRetenido"] = "{:.2f}".format(isr_27_amount)
                    monto_isr_total += isr_27_amount  # SUMA EL MONTO ISR A LA VARIABLE ACUMULADORA

                if self.move.l10n_latam_document_type_id.doc_code_prefix in [
                    'E31', 'E32', 'E33', 'E34', 'E43', 'E44', 'E45', 'E46']:
                    del items_data[numero_secuencia]["IndicadorAgenteRetencionoPercepcion"]
                    del items_data[numero_secuencia]["MontoITBISRetenido"]
                    del items_data[numero_secuencia]["MontoISRRetenido"]

                if self.move.l10n_latam_document_type_id.doc_code_prefix == 'E47':
                    del items_data[numero_secuencia]["MontoITBISRetenido"]

        return items_data

    def _get_additional_data(self):

        additional_data = {}
    
        additional_data["FechaEmision"] = self.move.invoice_date.strftime("%d-%m-%Y")

        return additional_data
    
    def _get_reference_information(self):

        reference_information = {}

        reference_information["1"] = {}

        reference_information["1"]["TipoDocumentoReferencia"] = "01"
        reference_information["1"]["NCFModificado"] = self.move.l10n_do_origin_ncf or ""
        reference_information["1"]["FechaNCFModificado"] = self.move.invoice_date.strftime("%d-%m-%Y") or ""
        reference_information["1"]["CodigoModificacion"] = self.move.l10n_do_ecf_modification_code or ""


        return reference_information