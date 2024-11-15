import io  # Para manejar archivos en memoria
import base64  # Para codificar el archivo Excel a base64
import xlsxwriter  # Para generar archivos Excel
from odoo import models, fields, api  # Importaciones estándar de Odoo para definir modelos y campos
from odoo.http import request  # Para manejar las respuestas HTTP en Odoo
from datetime import datetime

class EmployeeTss(models.Model):
    _name = 'hr.employee.tss'
    _description = 'Employee TSS'
    
    tss_type = fields.Char(string="Tipo de TSS", required=True)
    payroll_batch = fields.Char(string="Lote de Nómina", required=True)
    start_date = fields.Date(string="Fecha de Inicio", required=True)  # Agregando campo de fecha de inicio
    end_date = fields.Date(string="Fecha de Fin", required=True)  # Agregando campo de fecha de fin


class HrEmployeeTssReport(models.Model):
    _inherit = 'hr.employee.tss'

    def generate_tss_excel(self):
        # Obtener las fechas directamente del registro
        if not self.start_date or not self.end_date:
            # Si no se pasan las fechas, lanzar un error
            raise ValueError("Debe proporcionar un rango de fechas válido para generar el reporte.")

        # Convertir fechas a objetos de tipo datetime
        start_date = fields.Date.from_string(self.start_date)
        end_date = fields.Date.from_string(self.end_date)

        # Crear un archivo Excel en memoria
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        sheet = workbook.add_worksheet('Reporte de TSS')

        # Agregar encabezados de columna
        headers = ['Clave nómina', 'No. documento', 'Nombre', 'Sexo', 'Fecha de nacimiento', 'Aporte', 'Salario ISR', 'Tipo ingreso']
        for col, header in enumerate(headers):
            sheet.write(0, col, header)

        # Obtener todos los empleados ordenados por fecha de creación
        employees = self.env['hr.employee'].search([], order="create_date asc")

        # Filtrar los empleados según las fechas del lote de nómina
        filtered_employees = employees.filtered(
            lambda e: e.contract_id 
            and e.contract_id.date_start 
            and e.contract_id.date_start <= end_date 
            and (not e.contract_id.date_end or e.contract_id.date_end >= start_date)
        )

        # Agregar datos de empleados
        row = 1
        for index, employee in enumerate(filtered_employees):
            clave_nomina = index + 1
            contract = self.env['hr.contract'].search([('employee_id', '=', employee.id), ('state', '=', 'open')], limit=1)

            sheet.write(row, 0, clave_nomina)
            sheet.write(row, 1, employee.identification_id or 'Sin datos')
            sheet.write(row, 2, employee.name or 'Sin datos')
            sheet.write(row, 3, employee.gender or 'Sin datos')
            sheet.write(row, 4, employee.birthday.strftime("%d-%m-%Y") if employee.birthday else 'Sin datos')
            sheet.write(row, 5, 0)  # Aporte, puedes modificar este campo si es necesario

            if contract:
                sheet.write(row, 6, contract.wage or 'Sin datos')
                sheet.write(row, 7, contract.contract_type_id.name or 'Sin datos')
            else:
                sheet.write(row, 6, 0)  # No hay salario
                sheet.write(row, 7, 'Sin contrato')  # No hay contrato

            row += 1

        # Cerrar el archivo
        workbook.close()

        # Guardar el archivo como adjunto
        output.seek(0)
        data = output.read()
        output.close()

        attachment = self.env['ir.attachment'].create({
            'name': 'TSS_Report.xlsx',
            'type': 'binary',
            'datas': base64.b64encode(data),
            'res_model': 'hr.employee',
            'res_id': self.id,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }































# import io  # Para manejar archivos en memoria
# import base64  # Para codificar el archivo Excel a base64
# import xlsxwriter  # Para generar archivos Excel
# from odoo import models, fields, api # Importaciones estándar de Odoo para definir modelos y campos
# from odoo.http import request  # Para manejar las respuestas HTTP en Odoo

# class EmployeeTss(models.Model):
#     _name = 'hr.employee.tss'
#     _description = 'Employee TSS'
#     tss_type = fields.Char(string="Tipo de TSS", required=True)
#     payroll_batch = fields.Char(string="Lote de Nómina", required=True) 


# class HrEmployeeTssReport(models.Model):
#     _inherit = 'hr.employee.tss'
    
#     # Método para generar el archivo Excel
#     def generate_tss_excel(self, *args, **kwargs):

#         # Crear un archivo Excel en memoria
#         output = io.BytesIO()
#         workbook = xlsxwriter.Workbook(output)
#         sheet = workbook.add_worksheet('Reporte de tss')

#         # Agregar encabezados de columna
#         headers = ['Clave nomina', 'No. documento', 'Nombre', 'Sexo', 'Fecha de nacimiento', 'Aporte', 'Salario ISR', 'Tipo ingreso']
#         for col, header in enumerate(headers):
#             sheet.write(0, col, header)

#         # Obtener todos los empleados ordenados por fecha de creación
#         employees = self.env['hr.employee'].search([], order="create_date asc")
        
#         # Agregar datos de empleados
#         row = 1
#         for index, employee in enumerate(employees):
#             # Asignar la clave nómina según el orden de creación
#             clave_nomina = index + 1

#             # Obtener el contrato activo del empleado
#             contract = self.env['hr.contract'].search([('employee_id', '=', employee.id), ('state', '=', 'open')], limit=1)

#             sheet.write(row, 0, clave_nomina)  # Clave nómina
#             sheet.write(row, 1, employee.identification_id or 'Sin datos')
#             sheet.write(row, 2, employee.name or 'Sin datos')
#             sheet.write(row, 3, employee.gender or 'Sin datos')
#             sheet.write(row, 4, employee.birthday.strftime("%d-%m-%Y") if employee.birthday else 'Sin datos')
#             sheet.write(row, 5, 0)  # Aporte, puedes modificar este campo si es necesario

#             if contract:
#                 sheet.write(row, 6, contract.wage or 'Sin datos')
#                 sheet.write(row, 7, contract.contract_type_id.name or 'Sin datos')
#             else:
#                 sheet.write(row, 6, 0)  # No hay salario
#                 sheet.write(row, 7, 'Sin contrato')  # No hay contrato

#             row += 1

#         # Cerrar el archivo
#         workbook.close()

#         # Guardar el archivo como adjunto
#         output.seek(0)
#         data = output.read()
#         output.close()

#         attachment = self.env['ir.attachment'].create({
#             'name': 'TSS_Report.xlsx',
#             'type': 'binary',
#             'datas': base64.b64encode(data),
#             'res_model': 'hr.employee',
#             'res_id': self.id,
#             'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#         })

#         return {
#             'type': 'ir.actions.act_url',
#             'url': f'/web/content/{attachment.id}?download=true',
#             'target': 'self',
#         }

    # # Método para generar el archivo PDF
    # def generate_tss_pdf(self, *args, **kwargs):
    #     # Crear un archivo PDF en memoria con orientación horizontal y tamaño carta
    #     output = io.BytesIO()
    #     pdf = canvas.Canvas(output, pagesize=landscape(letter))  # Cambia aquí a landscape(letter)

    #     # Título del reporte
    #     pdf.setFont("Helvetica-Bold", 12)
    #     pdf.drawString(200, 550, "Reporte TSS de Empleados")  # Ajusta la posición según el nuevo tamaño

    #     # Encabezados de las columnas
    #     pdf.setFont("Helvetica-Bold", 10)
    #     headers = ['Clave nómina', 'Nombre', 'Teléfono', 'Departamento', 'Salario', 'Tipo de Contrato']
    #     x_offset = 50
    #     y_offset = 520  # Ajusta según la altura de la página
    #     for header in headers:
    #         pdf.drawString(x_offset, y_offset, header)
    #         x_offset += 120

    #     # Obtener todos los empleados ordenados por fecha de creación
    #     employees = self.env['hr.employee'].search([], order="create_date asc")

    #     # Datos de los empleados
    #     y_offset = 500  # Ajusta para dejar espacio para los encabezados
    #     pdf.setFont("Helvetica", 10)
    #     for index, employee in enumerate(employees):
    #         # Asignar la clave nómina según el orden de creación
    #         clave_nomina = index + 1

    #         # Obtener el contrato activo del empleado
    #         contract = self.env['hr.contract'].search([('employee_id', '=', employee.id), ('state', '=', 'open')], limit=1)

    #         pdf.drawString(50, y_offset, str(clave_nomina))  # Clave nómina
    #         pdf.drawString(170, y_offset, employee.name)
    #         pdf.drawString(290, y_offset, employee.work_phone or 'No tiene')
    #         pdf.drawString(410, y_offset, employee.department_id.name or 'Sin departamento')

    #         # Si se encuentra un contrato, mostrar el salario y tipo de contrato
    #         if contract:
    #             pdf.drawString(530, y_offset, str(contract.wage or 0))
    #             pdf.drawString(650, y_offset, contract.contract_type_id.name or 'Desconocido')
    #         else:
    #             pdf.drawString(530, y_offset, '0')  # No hay salario
    #             pdf.drawString(650, y_offset, 'Sin contrato')  # No hay contrato

    #         y_offset -= 20  # Espacio entre filas

    #     # Finalizar el archivo PDF
    #     pdf.showPage()
    #     pdf.save()

    #     # Guardar el archivo como adjunto
    #     output.seek(0)
    #     data = output.read()
    #     output.close()

    #     attachment = self.env['ir.attachment'].create({
    #         'name': 'TSS_Report.pdf',
    #         'type': 'binary',
    #         'datas': base64.b64encode(data),
    #         'res_model': 'hr.employee',
    #         'res_id': self.id,
    #         'mimetype': 'application/pdf'
    #     })

    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': f'/web/content/{attachment.id}?download=true',
    #         'target': 'self',
    #     }