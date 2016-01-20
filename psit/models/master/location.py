from openerp import models, fields

class LocationsLocations(models.Model):
    _name = "locations.locations"
    _description = 'PSIT locations'
    
    # Added by Nivas M (This field is used to filter the records based on selected store.)
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)
    
    block_id = fields.Many2one('blocks.blocks', 'Block', domain="[('store_id.active_store','=',True)]")
    name = fields.Char('Name', required=1)
    unique_id = fields.Char('Unique ID', required=1)