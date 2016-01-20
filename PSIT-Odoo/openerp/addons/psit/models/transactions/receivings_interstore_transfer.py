from openerp import models, fields, api, _

class ReceivingsInterStoreTransfer(models.Model):
    _name = 'receivings.inter.storetransfer'
    _description = "Receivings Inter Store Transfer"
    
    name = fields.Char('Name')
    supplier_invoice_number = fields.Char('Supplier Invoice #', required=True)
    grn_number = fields.Char('GRN #', required=True)
    receive_date = fields.Date('Date', required=True)
    grn_date = fields.Date('Date', required=True)
    memo = fields.Text('Memo')
    lr_numbrer = fields.Char('LR #')
    item = fields.Char('Items')
    invoice = fields.Char('Invoice')
    packing_list = fields.Char('Packing List')
    inter_store_id = fields.Many2one('inter.store', 'InterStore', required=True)
    material_ids = fields.One2many('interstore.receiving.quantity', 'material_receive_id', 'Materials')
    inter_receiving_attachment_ids = fields.One2many('inter.receiving.attachment', 'attachment_id', 'Attachment')
    
#     @api.model
#     def create(self, vals):
#         vals.update({'name':self.env['ir.sequence'].get('materials.receiving')})
#         return super(MaterialReceiving, self).create(vals)
    
class InterStoreReceivingQuantity(models.Model):
    _name = 'interstore.receiving.quantity'
    _description = 'Inter Receiving Quantity Material'

    material_receive_id = fields.Many2one('receivings.inter.storetransfer', 'Receiving Material')
    material_id = fields.Many2one('material.material', 'Name', required=True)
    material_unique_id = fields.Char('ID', related='material_id.unique_id', readonly=True)
    invoice_qty = fields.Float('Invoice Qty')
    received_qty = fields.Float('Received Qty')
    accepted_qty = fields.Float('Accepted Qty')
    review = fields.Text('Review')
    
        
class InterReceivingAttachmentType(models.Model):
    _name = 'interreceiving.attachment.type'
    _description = "Receiving Attachment"

    name = fields.Char('Name', required=True)