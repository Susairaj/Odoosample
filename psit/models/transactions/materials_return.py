from openerp import models, fields, api, _

class MaterialReturn(models.Model):
    _name = 'materials.return'
    _description = "Materials Receiving"
    
    name = fields.Char('ID')
    return_date = fields.Date('Date', required=True)
    mrn_number = fields.Char('MRN #', required=True)
    memo = fields.Text('Memo')
    supplier_id = fields.Many2one('res.partner', 'Supplier', required=True)
    return_reason = fields.Many2one('materials.return.reason','Reason', required=True)
    material_ids = fields.One2many('materials.return.quantity', 'material_return_qty_id', 'Material')
    return_attachment_ids = fields.One2many('return.attachment', 'return_attachment_id', 'Attachment')
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)
    
    @api.model
    def create(self, vals):
        total= 0.0;
        vals.update({'name':self.env['ir.sequence'].get('materials.return')})
        return_quantities = vals.get('material_ids')
        for record in return_quantities:
            material_obj = self.env['material.material'].search([('id', '=', record[2]['material_id'] )])
            total= material_obj.available_units - record[2]['material_qty']
            material_obj.write({'available_units':total})
        return super(MaterialReturn, self).create(vals)
     
    @api.multi
    def write(self, vals):
        total= 0.0;
        if vals.get('material_ids'):
            return_quantities = vals.get('material_ids')
            for record in return_quantities:
                material_id = record[1]
                if record[1] and record[2]:
                    material_return_qty= record[2]['material_qty']
                    material_re_obj = self.env['materials.return.quantity'].search([('id', '=', material_id )])
                    material_obj = self.env['material.material'].search([('id', '=', material_re_obj.material_id.id )])
                    material_qty_obj = self.env['materials.return.quantity'].search([('id', '=', material_re_obj.id )])
                    if material_qty_obj.material_qty<material_return_qty:
                        add_master = material_return_qty - material_qty_obj.material_qty
                        total= material_obj.available_units - add_master
                        self.env['material.material'].browse([material_obj.id]).write({'available_units':total})
                    elif material_qty_obj.material_qty>material_return_qty:
                        substract_master =  material_qty_obj.material_qty - material_return_qty 
                        total= material_obj.available_units + substract_master
                        self.env['material.material'].browse([material_obj.id]).write({'available_units':total}) 
                elif record[1]== False and record[2]:
                    material_obj = self.env['material.material'].search([('id', '=', record[2]['material_id'])])
                    total = material_obj.available_units + record[2]['material_qty']
                    self.env['material.material'].browse([material_obj.id]).write({'available_units':total})
        return super(MaterialReturn, self).write(vals)
    
#     @api.model
#     def default_get(self, fields_name):
#         issue_type = [];
#         data = super(MaterialReturn, self).default_get(fields_name)
#         for record in self.env['return.attachment.type'].search([]):
#             issue_type.append((1, record.id,{'return_attachmen_type_id': record.id}))
#         data['return_attachment_ids'] = issue_type
#         return data

class ReturnAttachment(models.Model):
    _name = 'return.attachment'
    _description = "Materials Returns Reason"

    return_attachment_id = fields.Many2one('materials.receiving', 'Materials Receiving')
    return_attachmen_type_id = fields.Many2one('return.attachment.type', 'Name', required=True)
    return_attachment_ids = fields.Many2many('ir.attachment', 'return_attachment_rel', 'return_attachment_id', 'materials_return_id', 'Upload')
        
class MaterialReturnQty(models.Model):
    _name = 'materials.return.quantity'
    _description = "Materials Return Quantity"
    _rec_name = 'material_id'
    
    material_return_qty_id = fields.Many2one('materials.return', 'Receiving Material')
    material_id = fields.Many2one('material.material', 'Name', required=True, domain="[('store_id.active_store','=',True)]")
    material_unique_id = fields.Char('ID', related='material_id.unique_id', readonly=True) 
    material_qty = fields.Float('Qty', required=True)
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)