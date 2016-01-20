from openerp import fields, models

class ResCompany(models.Model):
    _inherit = "res.company"
    _description = 'PSIT Company'
    
    manual_id = fields.Char('Unique Manual Id', required=True)
    business_type = fields.Char('Business Type')
    description = fields.Text()