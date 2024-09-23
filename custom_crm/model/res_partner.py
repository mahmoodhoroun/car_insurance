from odoo import models

class ResPartnerCustom(models.Model):
    _inherit = 'res.partner'

    # SQL constraint to make the phone field unique
    _sql_constraints = [
        ('partner_phone_unique', 'unique(phone)', 'The phone number must be unique for each contact!')
    ]