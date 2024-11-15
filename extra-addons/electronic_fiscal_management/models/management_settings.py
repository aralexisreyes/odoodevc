from odoo import models, fields

class ManagementSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    request_count = fields.Char('Request count')

    pass


