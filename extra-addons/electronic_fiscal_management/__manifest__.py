{
    'name': 'Electronic Fiscal Management',
    'version': '1.0',
    'summary': 'Electronic fiscal model management module',
    'description': 'This module provides functionalities to manage the electronic fiscal model in Odoo.',
    'author': 'Codeando, SRL',
    'category': 'Accounting',
    'depends': ['base', 'account', 'electronic_fiscal'],
    'data': [
        'views/electronic_fiscal_management_views.xml',
        'views/management_settings_views.xml',
        'views/menuitem_electronic_fiscal_management_views.xml',
        'security/ir.model.access.csv'
    ],

    'installable': True,
    'application': True,
    'auto_install': False
}