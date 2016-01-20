from openerp import models, fields

"""  Author : Moses I  """    
class BlocksBlocks(models.Model):
    _name = "blocks.blocks"
    _description = 'PSIT Blocks'
    
    # Added by Nivas M (This field is used to filter the records based on selected store.)
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)
    
    name = fields.Char('Name', required=1)
    unique_id = fields.Integer('Unique ID', required=1)