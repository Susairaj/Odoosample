from openerp import models, fields
from datetime import datetime

class BoqMaterial(models.Model):
    _name = "boq.material"
    _description = 'PSIT materials'
    
    material_id = fields.Many2one('material.material', 'Material', required=True)
    boq_material_id = fields.Many2one('material.material', 'Material')
    unit_id = fields.Many2one('materials.units', 'Unit')
    category_id = fields.Many2one('material.categories','Category', required=True)
    qty = fields.Integer('Quantity', required=True)
    date = fields.Datetime('Date', default=datetime.today())