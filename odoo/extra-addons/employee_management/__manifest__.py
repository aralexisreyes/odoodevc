{
    'name': 'Employee Management',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Manage employee loans and deductions in payroll',
    'description': """
        This module allows you to manage employee loans and automatically deduct loan payments from payroll.
    """,
    'author': 'Condeando, SRL',
    'website': 'https://www.codeando.com.do',
    'depends': ['hr', 'hr_payroll'],
    'data': [
        'security/ir.model.access.csv',  # Archivo de permisos de acceso
        'views/employee_loan_views.xml',  # Vista de préstamos a empleados
        'views/hr_payroll_views.xml',  # Integración con las vistas de nómina
        'views/hr_employee_tss.xml', # Vista para de botones para generar tss
        'views/employee_loan_views.xml',
        'data/salary_rule_data.xml'
        
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
