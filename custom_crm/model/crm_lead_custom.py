from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CrmLeadCustom(models.Model):
    _inherit = 'crm.lead'

    car_ids = fields.One2many('car.model', 'crm_lead_id', string='Cars')

    # SQL constraint to make the phone field unique
    # _sql_constraints = [
    #     ('phone_unique', 'unique(phone)', 'The phone number must be unique!')
    # ]