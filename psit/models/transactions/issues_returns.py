from openerp import models, fields, api, _

''' Issues Returns - Sathish Kumar'''
class IssuesReturns(models.Model):
    _name = 'issues.returns'
    
    name = fields.Char('ID')
    date = fields.Date('Date')
    mrn_no = fields.Char('MRN #')
    memo = fields.Text('Memo')
    reason = fields.Char('Reason')
    contractor_id = fields.Many2one('res.users', 'Contractor', required=True)   
    block_id = fields.Many2one('blocks.blocks', 'Block')
    location_id = fields.Many2one('locations.locations','Location')
    materials_ids = fields.One2many('issues.return.material', 'issues_return_id', 'Materials')
    issue_return_attachment_ids = fields.One2many('issue.return.attachment', 'issue_return_id', 'Attachment')
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)
    @api.model
    def default_get(self, fields_name):
        issue_type = [];
        data = super(IssuesReturns, self).default_get(fields_name)
        for record in self.env['receiving.attachment.type'].search([]):
           issue_type.append((2, record.id, {'issue_return_attach_type_id':record.id}))
        data['issue_return_attachment_ids'] = issue_type
        return data
    
    @api.model
    def create(self, vals):
        total_available = 0.0;
        for record in vals.get('materials_ids'):
            material_id = self.env['material.material'].search([('id', '=', record[2]['material_material_id'])])
            total_available = material_id.available_units + record[2]['quantity']
            material_id.write({'available_units':total_available})
        vals.update({'name':self.env['ir.sequence'].get('issues.returns')})
        return super(IssuesReturns, self).create(vals)
    
    @api.multi
    def write(self, vals):
        total_available = 0.0; total = 0.0;
        for material in vals.get('materials_ids'):
            if material[1] and material[2]:
                issue_return_material = self.env['issues.return.material'].search([('id', '=', material[1])])
                material_material = self.env['material.material'].search([('id', '=', issue_return_material.material_material_id.id)])
                if issue_return_material.quantity < material[2]['quantity']:
                    total = material[2]['quantity'] - issue_return_material.quantity
                    material_material.write({'available_units':material_material.available_units + total})
                elif issue_return_material.quantity > material[2]['quantity']:
                    total =  issue_return_material.quantity - material[2]['quantity']
                    material_material.write({'available_units':material_material.available_units - total})
            elif material[1] == False and material[2]:
                 material_id = self.env['material.material'].search([('id', '=', material[2]['material_material_id'])])
                 total_available = material_id.available_units + material[2]['quantity']
                 material_id.write({'available_units':total_available})
        return super(IssuesReturns, self).write(vals)
    
class IssueReturnAttachment(models.Model):
    _name = 'issue.return.attachment'
    _description = "Issue Return Attachments"
    
    issue_return_id = fields.Many2one('issues.returns', 'Attachment')
    issue_return_attach_type_id = fields.Many2one('receiving.attachment.type', 'Name')
    issue_return_attachment_ids = fields.Many2many('ir.attachment', 'issue_return_attachment_rel', 'issue_return_attachment_id', 'issues_returns_id', 'Upload')
    
class IssuesReturnMaterial(models.Model):
    _name = 'issues.return.material'
    _description = 'Issues Return Material'
    
    @api.onchange('material_material_id')
    def onchange_material_id(self):
         if self.material_material_id:
             self.material_no = self.env['material.material'].search([('id', '=', self.material_material_id.id)]).unique_id
     
    issues_return_id = fields.Many2one('issues.returns', 'Issues Returns')
    material_no = fields.Char('ID', readonly=True)
    material_material_id = fields.Many2one('material.material', 'Name', domain="[('store_id.active_store','=',True)]", required=True)
    quantity = fields.Float('Quantity', required=True)
    
""" End """ 