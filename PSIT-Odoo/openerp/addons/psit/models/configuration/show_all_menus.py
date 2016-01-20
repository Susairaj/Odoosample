from openerp import models, fields
    
class show_menus(models.Model):
    _name = 'show.all_menus' 
    
    name = fields.Char('Text')
