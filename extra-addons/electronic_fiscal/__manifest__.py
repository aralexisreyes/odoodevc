{
    'name': 'Electronic Fiscal Accounting',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Issuance and validation of electronic receipts (E-cf)',
    'description': """
      This module integrates the issuance and validation 
      of electronic documents at the tax level in the Dominican Republic.
    """,
    'depends': ['account', 'base'],

    'data': [
      'views/account_move_views.xml',
      'views/ecf_records_views.xml',
      'views/dgii_menuitem_views.xml',
      'views/dgii_views.xml',
      'views/dgii_settings_views.xml',
      'security/ir.model.access.csv'

    ],
    
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    
    'images': [
        'static/description/logo.png'
    ],
}