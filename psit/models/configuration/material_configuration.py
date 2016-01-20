from openerp import models, fields, api, _

class MaterialConfiguration(models.Model):
    _name = "material.configuration"
    _description = 'PSIT Blocks'
    
    name = fields.Char('Name', required=1)
    unique_id = fields.Char('Unique ID', required=1)
    
    
    
    
    
    