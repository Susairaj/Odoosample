from openerp import fields, models

"""  Author : Nivas M  """    
class ResUsers(models.Model):
    _inherit = "res.users"
    _description = 'PSIT Users'
       
    active_store_id = fields.Many2one('store.store', string='Active Store')
    
    
""" End """ 