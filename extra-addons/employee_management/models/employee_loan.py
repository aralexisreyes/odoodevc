from odoo import models, fields, api

class EmployeeLoan(models.Model):
    _name = 'hr.employee.loan'
    _description = 'Employee Loan'

    employee_id = fields.Many2one('hr.employee', string="Empleado", required=True)
    loan_amount = fields.Float(string="Monto del prestamo", required=True)
    remaining_amount = fields.Float(string="Cantidad restante", compute='_compute_remaining_amount')
    deduction_amount = fields.Float(string="Deduccion por nomina", required=True)
    total_installments = fields.Integer(string="Cuotas totales", required=True)
    current_installment = fields.Integer(string="Cuotas actuales", default=0)

    @api.depends('loan_amount', 'current_installment', 'deduction_amount')
    def _compute_remaining_amount(self):
        for record in self:
            record.remaining_amount = record.loan_amount - (record.current_installment * record.deduction_amount)

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    @api.model

    def compute_sheet(self):
        res = super(HrPayslip, self).compute_sheet()
        for slip in self:
            if slip.employee_id.loan_id and slip.employee_id.loan_id.remaining_amount > 0:
                    slip.employee_id.loan_id.current_installment += 1
        return res
      


class Employee(models.Model):
    _inherit = 'hr.employee'

    loan_id = fields.Many2one('hr.employee.loan', string="Prestamo", help="Current loan of the employee")
