from openerp import models, fields


class MaterialCategories(models.Model):
    _name = "material.categories"
    _description = 'PSIT materials categories'
    
    name = fields.Char('Name', required=1)
    description = fields.Text('Description')