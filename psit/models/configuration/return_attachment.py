from openerp import models, fields

class ReturnAttachmentType(models.Model):
    _name = 'return.attachment.type'
    _description = "Return Attachment"

    name = fields.Char('Name', required=True)