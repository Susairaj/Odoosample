from openerp import models, fields

class BoqBoq(models.Model):
    _name = "boq.boq"
    _description = 'PSIT Bill Of Quantity materials'
    
    # Added by Nivas M (This field is used to filter the records based on selected store.)
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)
             
    material_id = fields.Many2one('material.material', 'Material', required=True, domain="[('store_id.active_store','=',True)]")
    quantity = fields.Integer(required=True)
    date_created = fields.Datetime('Date')