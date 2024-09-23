from odoo import models, fields

class CarModel(models.Model):
    _name = 'car.model'
    _description = 'Car Model'

    name = fields.Char(string='Car Name', required=True)
    model = fields.Char(string='Model')
    brand = fields.Char(string='Brand')
    crm_lead_id = fields.Many2one('crm.lead', string='Related Lead')
