{
    'name': 'Create new order in POS',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Create a new order with a button on the POS product screen',
    'description': """
    This module adds a button to create a new order on the product screen of the POS.
    """,
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            # Incluye tu archivo JS aquí
            'pos_button_custom/static/src/js/pos_create_button.js',
            'pos_button_custom/static/src/xml/pos_button_templates.xml',  # Incluye tu archivo XML aquí
        ],
    },
    'installable': True,
    'application': False,
}
