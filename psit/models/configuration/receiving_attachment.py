from openerp import models, fields

class ReceivingAttachmentType(models.Model):
    _name = 'receiving.attachment.type'
    _description = "Receiving Attachment"

    name = fields.Char('Name', required=True)