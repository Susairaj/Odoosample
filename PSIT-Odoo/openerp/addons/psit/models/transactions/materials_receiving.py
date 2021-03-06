from openerp import models, fields, api

class MaterialReceiving(models.Model):
    _name = 'materials.receiving'
    _description = "Materials Receiving"
    
    # Added by Nivas M (This field is used to filter the records based on selected store.)
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)
    
    name = fields.Char('ID')
    item = fields.Char('Items')
    receive_date = fields.Date('Date', required=True)
    supplier_invoice_number = fields.Char('Supplier Invoice #', required=True)
    grn_date = fields.Date('GRN Date')
    grn_number = fields.Char('GRN #', required=True)
    lr_numbrer = fields.Char('LR #', required=True)
    material_ids = fields.One2many('receiving.quantity.material', 'material_receive_id', 'Materials')
    supplier_id = fields.Many2one('res.partner', 'Supplier', required=True)
    receiving_attachment_ids = fields.One2many('receiving.attachment', 'material_receiving_id', 'Attachment')
    
    @api.model
    def create(self, vals):
        vals.update({'name':self.env['ir.sequence'].get('materials.receiving')})
        accepted_quantities = vals.get('material_ids')
        for record in accepted_quantities:
            material_id= record[2]['material_id']
            material_obj = self.env['material.material'].search([('material_id', '=', material_id )])
            material_qty=material_obj.available_units
            total= record[2]['accepted_qty'] + material_qty
            self.env['material.material'].browse([material_id]).write({'available_units':total})
        return super(MaterialReceiving, self).create(vals)
    
    @api.multi
    def write(self, vals):
        total= 0.0;
        if vals.get('material_ids'):
            materials = vals.get('material_ids')
            for material in materials:
                    material_id = material[1]
                    if material[1] and material[2]:
                        material_re_obj = self.env['receiving.quantity.material'].search([('id', '=', material_id )])
                        material_obj = self.env['material.material'].search([('material_id', '=', material_re_obj.material_id.id )])
                        material_qty_obj = self.env['receiving.quantity.material'].search([('id', '=', material_re_obj.id )])
                        if 'accepted_qty' in material[2]:
                            if material_qty_obj.accepted_qty<material[2]['accepted_qty']:
                                add_master = material[2]['accepted_qty'] - material_qty_obj.accepted_qty
                                total= material_obj.available_units + add_master
                                self.env['material.material'].browse([material_obj.id]).write({'available_units':total})
                            elif material_qty_obj.accepted_qty>material[2]['accepted_qty']:
                                substract_master =  material_qty_obj.accepted_qty - material[2]['accepted_qty'] 
                                total= material_obj.available_units - substract_master
                                self.env['material.material'].browse([material_obj.id]).write({'available_units':total}) 
                        elif material[1]== False and material[2]:
                            material_obj = self.env['material.material'].search([('material_id', '=', material[2]['material_id'])])
                            if 'accepted_qty' in material[2]:
                                total = material_obj.available_units + material[2]['accepted_qty']
                                material_obj.write({'available_units':total})
        return super(MaterialReceiving, self).write(vals)

class MaterialReceivingQuantity(models.Model):
    _name = 'receiving.quantity.material'
    _description = 'Receiving Quantity Material'

    @api.onchange('material_type')
    def onchange_material_type(self):
        res = {}
        if self.material_type == 'sets':
            res['domain'] = {'material_id': [('is_sets', '=', True)]}
        else:
            res['domain'] = {'material_id': [('is_sets', '=', False)]}
        return res

    material_receive_id = fields.Many2one('materials.receiving', 'Receiving Material')
    material_id = fields.Many2one('material.material', 'Name', required=True, domain="[('store_id.active_store','=',True)]")
    material_unique_id = fields.Char('ID', related='material_id.unique_id', readonly=True)
    invoice_qty = fields.Float('Invoice Qty')
    received_qty = fields.Float('Received Qty')
    accepted_qty = fields.Float('Accepted Qty', required=True)
    review = fields.Text('Review')
    material_type = fields.Selection([('sets', 'Sets'),('individual', 'Individual')], 'Material Type')
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)
    location_id = fields.Many2one('locations.locations','Location', domain="[('store_id.active_store','=',True)]")
    
class InterReceivingAttachment(models.Model):
    _name = 'inter.receiving.attachment'
    _description = "Materials Receiving Attachments"

    name = fields.Many2one('interreceiving.attachment.type', 'Name', required=True)
    attachment_id = fields.Many2one('receivings.inter.storetransfer', 'Attachment')
    receiving_attachment = fields.Binary('Attachment')
    
class ReceivingAttachment(models.Model):
    _name = 'receiving.attachment'
    _description = "Materials Receiving Attachments"

    material_receiving_id = fields.Many2one('materials.receiving', 'Materials Receiving')
    receiving_attach_type_id = fields.Many2one('receiving.attachment.type', 'Name', required=True)
    receiving_attachment_ids = fields.Many2many('ir.attachment', 'receiving_attachment_rel', 'receiving_attachment_id', 'materials_receiving_id', 'Upload')
       