from openerp import models, fields

class SiteInspector(models.Model):
    _name = 'site.inspector' 
    _rec_name = 'date'
    
    contractor_id = fields.Many2one('contractor.contractor', 'Contractor Type', required=True)
    block_id = fields.Many2one('blocks.blocks', 'Block', domain="[('store_id.active_store','=',True)]")
    location_id = fields.Many2one('locations.locations','Location', domain="[('store_id.active_store','=',True)]")
    
    date = fields.Datetime('Date', required=True)
    site_material_ids = fields.One2many('site.inspector.materials', 'site_materials_id', 'Name', required=True)
    
class SiteInspectorMaterials(models.Model):
    _name = 'site.inspector.materials' 
    _rec_name = 'material_id'

    site_materials_id = fields.Many2one('site.inspector', 'Site Inspector')
    
    quantity = fields.Float('Quantity')        
    block_id = fields.Many2one('blocks.blocks', 'Block', domain="[('store_id.active_store','=',True)]")
    location_id = fields.Many2one('locations.locations','Village', domain="[('store_id.active_store','=',True)]")
    material_category_id = fields.Many2one('material.categories','Material Category', required=True)
    material_code = fields.Char('Material Code')
    material_id = fields.Many2one('material.material', 'Material Name', required=True, domain="[('store_id.active_store','=',True)]")   
    unit_id = fields.Many2one('materials.units', 'Unit')
    cumulative_issues_till_date = fields.Integer('Cumulative Issues till date')
    cumulative_returns_till_date = fields.Integer('Cumulative Returns till date')
    total_net_issues = fields.Integer('Total Net Issues')
    consumption_till_previous_updation = fields.Integer('Consumption till previous updation')
    previous_updation_date = fields.Date('Previous Updation Date')
    updated_by = fields.Many2one('res.partner','Updated By', domain="[('store_id.active_store','=',True)]")
    balance_with_contractor = fields.Float('Balance with Contractor')