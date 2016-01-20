from openerp import models, fields, api

LEVEL = [
    ('default', 'Default'),
    ('level1', 'Level 1'),
    ('level2', 'Level 2'),
    ('level3', 'Level 3'),
    ('level4', 'Level 4'),
    ('level5', 'Level 5'),
         
]

class InterStore(models.Model):
    _name = 'inter.store'
    _description = 'Inter store details'
    
    # Added by Muthu
    @api.model
    def default_get(self, fields):
        rec = super(InterStore, self).default_get(fields)
        rec['country_id'] = self.env['res.country'].search([('name', '=', 'India')]).id
        return rec
    
    store_keeper_id = fields.Char('Full Name', required=True)
    name = fields.Char('ID')
    business_title = fields.Char('Business Title')
    mobile = fields.Char('Mobile')
    phone = fields.Char('Phone')
    authorized_person1_id = fields.Many2one('res.users', 'Name(1)')
    authorized_person2_id = fields.Many2one('res.users', 'Name(2)')
    authorized_person3_id = fields.Many2one('res.users', 'Name(3)')
    mobile1 = fields.Char('Mobile')
    mobile2 = fields.Char('Mobile')
    mobile3 = fields.Char('Mobile')
    address = fields.Text('Address')
    city = fields.Char('City')
    state_id = fields.Many2one('res.country.state', 'State/Province', domain="[('country_id.name','=','India')]")
    country_id = fields.Many2one('res.country', 'Country', readonly=True, store=True)
    email = fields.Char('Email')
    price_level = fields.Selection(LEVEL, 'Price Level')
    notes = fields.Text('Notes')
    
    @api.model
    def create(self, vals):
        vals.update({'name':self.env['ir.sequence'].get('inter.store')})
        return super(InterStore, self).create(vals)