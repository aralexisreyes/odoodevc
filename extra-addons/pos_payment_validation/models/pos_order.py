from odoo import models, api, exceptions

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def create_from_ui(self, orders, draft=False):
        # Iteramos sobre cada orden en la lista de órdenes
        for order_data in orders:
            data = order_data.get('data', {})
            
            # Validamos que la orden tenga un cliente antes de crearla
            if not data.get('partner_id'):
                raise exceptions.UserError("Debes seleccionar un cliente antes de crear la orden.")
            
            # Si la orden debe ser facturada, validamos la opción de factura
            if data.get('to_invoice', False) and not data.get('partner_id'):
                raise exceptions.UserError("Debes seleccionar un cliente antes de facturar.")

        # Creamos las órdenes de la manera usual
        return super(PosOrder, self).create_from_ui(orders, draft)
