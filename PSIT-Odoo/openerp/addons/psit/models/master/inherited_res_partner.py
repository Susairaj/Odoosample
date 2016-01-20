from openerp import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"
    _description = 'PSIT Suppliers'
    
    # Added by Nivas M (This field is uesd to filter the records based on selected store.)
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)
    
    provider_of = fields.Char('Provider of')
    contact_person = fields.Char('Contact Person')
    service_tax = fields.Float('Service tax')
    pan = fields.Char('PAN#')
    tin_number = fields.Integer('TIN#')
    
