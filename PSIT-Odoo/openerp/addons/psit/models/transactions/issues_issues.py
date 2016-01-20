from openerp import models, fields, api, _

class IssuesIssues(models.Model):
    _name = 'issues.issues'
    _description = 'Issues Details'
    
    # Added by Nivas M (This field is used to filter the records based on selected store.)    
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)
    name = fields.Char('ID')
    date = fields.Date('Date')
    issue_challan_no = fields.Char('Issue Challan #')
    indent_no = fields.Char('Indent Number')
    indent_receive_no = fields.Date('Indent Receiving Date')
    memo = fields.Text('Memo')
    contractor_id = fields.Many2one('res.users', 'Contractor', required=True)
    block_id = fields.Many2one('blocks.blocks', 'Block')
    location_id = fields.Many2one('locations.locations','Location')
    materials_ids = fields.One2many('issues.material', 'issues_issues_id', 'Materials')
    issue_attachment_ids = fields.One2many('issue.attachment', 'attachment_id', 'Attachment')
    
    @api.model
    def create(self, vals):
        boq = 0.0;
        for record in vals.get('materials_ids'):
            material_id = self.env['material.material'].search([('id', '=', record[2]['material_material_id'])])
            total_boq = material_id.available_units - record[2]['issued_qty']
            material_id.write({'available_units':total_boq})
        vals.update({'name':self.env['ir.sequence'].get('issues.issues')})
        return super(IssuesIssues, self).create(vals)
    
    @api.multi
    def write(self, vals):
        total_available = 0.0; total = 0.0;
        for material in vals.get('materials_ids'):
            if material[1] and material[2]:
                issue_material = self.env['issues.material'].search([('id', '=', material[1])])
                material_material = self.env['material.material'].search([('id', '=', issue_material.material_material_id.id)])
                if issue_material.issued_qty < material[2]['issued_qty']:
                    total = material[2]['issued_qty'] - issue_material.issued_qty
                    material_material.write({'available_units':material_material.available_units - total})
                elif issue_material.issued_qty > material[2]['issued_qty']:
                    total =  issue_material.issued_qty - material[2]['issued_qty']
                    material_material.write({'available_units':material_material.available_units + total})
            elif material[1] == False and material[2]:
                 material_id = self.env['material.material'].search([('id', '=', material[2]['material_material_id'])])
                 total_available = material_id.available_units - material[2]['issued_qty']
                 material_id.write({'available_units':total_available})
        return super(IssuesIssues, self).write(vals)
    
class IssueAttachment(models.Model):
    _name = 'issue.attachment'
    _description = "Issue Attachments"

    attachment_id = fields.Many2one('issues.issues', 'Attachment')
    issue_attach_type_id = fields.Many2one('issue.attachment.type', 'Name', required=True)
    issue_attachment_ids = fields.Many2many('ir.attachment', 'issue_attachment_rel', 'issue_attachment_id', 'issues_issues_id', 'Upload')
    
class IssuesMaterial(models.Model):
    _name = 'issues.material'
    _description = 'Issues Material'
    
    @api.onchange('material_material_id')
    def onchange_material_id(self):
         if self.material_material_id:
             self.material_no = self.env['material.material'].search([('id', '=', self.material_material_id.id)]).unique_id
             
    issues_issues_id = fields.Many2one('issues.issues', 'Issues')
    material_no = fields.Char('ID', readonly=True)
    material_material_id = fields.Many2one('material.material', 'Name', required=True, domain="[('store_id.active_store','=',True)]")
    requested_qty = fields.Float('Quantity Requested')
    issued_qty = fields.Float('Quantity Issued', required=True)

LEVEL = [
    ('default', 'Default'),
    ('level1', 'Level 1'),
    ('level2', 'Level 2'),
    ('level3', 'Level 3'),
    ('level4', 'Level 4'),
    ('level5', 'Level 5'),
         
]   
    