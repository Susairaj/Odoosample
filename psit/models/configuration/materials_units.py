from openerp import models, fields

class MaterialUnits(models.Model):
    _name = "materials.units"
    _description = 'PSIT materials units'
     
    name = fields.Char('Unit', required=1)