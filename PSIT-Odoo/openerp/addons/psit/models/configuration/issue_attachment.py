from openerp import models, fields

class IssueAttachmentType(models.Model):
    _name = 'issue.attachment.type'
    _description = "Issue Attachment"

    name = fields.Char('Name', required=True)