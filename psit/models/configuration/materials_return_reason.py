from openerp import models, fields

class MaterialReturnReason(models.Model):
    _name = 'materials.return.reason'
    _description = "Materials Returns Reason"

    name = fields.Char('Reason Title', required=True)
    description = fields.Text('Description')