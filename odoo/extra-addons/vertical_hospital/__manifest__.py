{
    'name': 'Aplicacion hospital',
    'version': '1.0',
    'author': 'Alexis', 
    'description': 'Modulo de prueba para Aset Technology',
    'depends': ['base', 'mail'],
    'data': [

        'views/vertical_hospital_patients_views.xml',
        'views/vertical_hospital_treatments_views.xml',
        'views/vertical_hospital_menuitem_views.xml',
        'views/vertical_hospital_settings.xml',
        'security/ir.model.access.csv',
        'reports/report_patient_template.xml',
        'reports/report_patient_action.xml',
        'reports/report_patient.xml'

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'images': [
        'static/description/odoo_logo_enterprise'
    ],
}