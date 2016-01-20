from openerp import models, fields, api

class ContractorContractor(models.Model):
    _name = "contractor.contractor"
    _description = 'PSIT Contractor'
    
    # Added by Muthu
    @api.model
    def default_get(self, fields):
        rec = super(ContractorContractor, self).default_get(fields)
        rec['country_id'] = self.env['res.country'].search([('name', '=', 'India')]).id
        return rec
    
    # Added by Nivas M (This field is used to filter the records based on selected store.)
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)
    
    name = fields.Char('Full Name', required=True)
    business_title = fields.Char('Business Title')
    mobile = fields.Char()
    phone = fields.Char()
    authorized_person_ids = fields.One2many('authorized.person', 'contact_id', 'Authorized person', limit=3)
    address = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state', 'State', domain="[('country_id.name','=','India')]")
    country_id = fields.Many2one('res.country', 'Country', readonly=True, store=True)
    email = fields.Char('Email')
    price_level_id = fields.Many2one('price.level', 'Price Level')
    note = fields.Text('Notes')
    balance = fields.Integer()
    
class AuthorizedPerson(models.Model):
    _name = "authorized.person"
    _description = 'PSIT Authorized Person'
    
    name = fields.Char('Authorized Person Name')
    mobile = fields.Char()
    contact_id = fields.Many2one('contractor.contractor')