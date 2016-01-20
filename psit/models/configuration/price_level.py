from openerp import models, fields

class PriceLevel(models.Model):
    _name = "price.level"
    _description = 'PSIT Price Level'
    
    name = fields.Char('Name', required=True)