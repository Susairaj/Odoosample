from openerp import models, fields, api

class StoreAccess(models.Model):
    _name = 'store.access'
    
    user_id = fields.Many2one('res.users', 'User', required=True)
    store_id = fields.Many2one('store.store', 'Store')
    email = fields.Char(related='user_id.email')
    user_rel_id = fields.Integer('User Id', compute='get_user_id')
    modules = fields.Char('Modules', compute='get_modules')
    is_issues = fields.Boolean('Issues')
    is_receiving = fields.Boolean('Receiving')
    is_supplier = fields.Boolean('Supplier')
    is_contractor = fields.Boolean('Contractors')
    is_materials = fields.Boolean('Materials')
    is_returns = fields.Boolean('Returns')
    is_site_inspector = fields.Boolean('Site Inspector')
    is_view_attachments = fields.Boolean('View Attachments')
    is_reports = fields.Boolean('Reports')
    
    @api.one
    @api.depends('user_id')
    def get_user_id(self):
        if self.user_id:
            self.user_rel_id = self.user_id.id
    
    @api.one
    @api.depends('is_issues', 'is_receiving', 'is_supplier', 'is_contractor', 'is_materials', 'is_returns', 'is_site_inspector', 'is_view_attachments', 'is_reports')
    def get_modules(self):
        modules = ""
        if self.is_issues:
            modules = modules + 'Issues, '
        if self.is_receiving:
            modules = modules + 'Receiving, '
        if self.is_supplier:
            modules = modules + 'Supplier, '
        if self.is_contractor:
            modules = modules + 'Contractor, '
        if self.is_materials:
            modules = modules + 'Materials, '
        if self.is_returns:
            modules = modules + 'Returns, '
        if self.is_site_inspector:
            modules = modules + 'Site Inspector'
        if self.is_view_attachments:
            modules = modules + 'View Attachments'
        if self.is_reports:
            modules = modules + 'Reports'
        self.modules = modules