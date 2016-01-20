from openerp import models, fields, api, _

"""  Author : Sathish M  """ 

class StoreStore(models.Model):
    _name = 'store.store'
    _description = 'Store Details'
    
    # Added by Muthu
    @api.model
    def default_get(self, fields):
        rec = super(StoreStore, self).default_get(fields)
        rec['country_id'] = self.env['res.country'].search([('name', '=', 'India')]).id
        return rec
    
    name = fields.Char('Name', required=True)
    store_sequence = fields.Char('Unique Manual Id', required=True)
    company_id = fields.Many2one('res.company', 'Company', required=True)
    project_id = fields.Many2one('project.project','Project', required=True)
    business_type = fields.Char('Business Type')
    address1 = fields.Text('Address 1')
    address2 = fields.Text('Address 2')
    city = fields.Char('City')
    state_id = fields.Many2one('res.country.state', 'State/Province', domain="[('country_id.name','=','India')]")
    country_id = fields.Many2one('res.country', 'Country', readonly=True, store=True)
    zip = fields.Char('Zip code')
    phone = fields.Char('Phone')
    email = fields.Char('Email')
    currency_id = fields.Many2one('res.currency', 'Currency')
    logo = fields.Binary('Store Logo')
    description = fields.Text('Description')
    
    # Added By Nivas M
    user_id = fields.Many2one('res.users', string='Responsible', required=False, default=lambda self: self.env.user)
    active_store = fields.Boolean('Active Store')
    
    #active_store = fields.Boolean(compute='_get_active_store','Active Store', store=True)
    
#     clear_active_store = fields.Char(compute='_clear_active_store', string='Clear Active Store', store=True)
#     @api.multi
#     def _clear_active_store(self):
#         a= 0;
#         for record in self.search([]):
#             if record.active_store:
#                 record.active_store = False
    
#     @api.multi
#     def _get_active_store(self):
#         a= 0;
#         for line in self:
#             line.active_store = self.get_active_store(self)
    
    @api.multi
    def get_active_store(self):
        a= 0;
        for line in self:
            receice_active_store = self.env.context.get('receice_active_store')
            if receice_active_store == 'yes':
                if line.store_sequence and line.name:
                    line.user_id.write({'active_store_id': line.id})
                    for record in self.search([]):
                        if record.active_store:
                            record.active_store = False
                    line.active_store = True
            else:
                line.active_store = False
        return line.active_store
            
    # End 