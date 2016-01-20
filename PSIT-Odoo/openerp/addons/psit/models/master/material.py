from openerp import models, fields, api, _

class MaterialMaterial(models.Model):
    _name = "material.material"
    _description = 'PSIT materials'
    _rec_name = "material_id"
    
    @api.one
    @api.depends('material_id')
    def get_material_qty(self):
        total = 0.0; issue_total = 0.0; return_count = 0.0; total_return = 0.0
        store = self.env['store.store'].search([('active_store', '=', True)])
        if store.id:
            for record in self.env['materials.receiving'].search([('store_id', '=', store.id)]):
                for receiveing in self.env['receiving.quantity.material'].search([('material_receive_id', '=', record.id),('material_id', '=', self.id)]):
                    total += receiveing.accepted_qty
            for material_record in self.env['materials.return'].search([('store_id', '=', store.id)]):
                 for returns in self.env['materials.return.quantity'].search([('material_return_qty_id', '=', material_record.id),('material_id', '=', self.id)]):
                    total -= returns.material_qty
            for issue_record in self.env['issues.issues'].search([('store_id', '=', store.id)]):
                for issues in self.env['issues.material'].search([('issues_issues_id', '=', issue_record.id),('material_material_id', '=', self.id)]):
                    issue_total += issues.issued_qty
            for issue_return in self.env['issues.returns'].search([('store_id', '=', store.id)]):
                for returns_record in self.env['issues.return.material'].search([('issues_return_id', '=', issue_return.id),('material_material_id', '=', self.id)]):
                    issue_total -= returns_record.quantity
            total_count = total - issue_total
            self.material_count = total_count
    
    # Added by Nivas M (This field is used to filter the records based on selected store.)
    store_id = fields.Many2one('store.store', string='Selected Store', readonly=True, default=lambda self: self.env.user.active_store_id)
    
    image = fields.Binary('Image')       
    material_id = fields.Many2one('material.configuration', 'Name', required=True)
    unique_id = fields.Char('ID', related='material_id.unique_id', readonly=True)
    
    category_id = fields.Many2one('material.categories','Category', required=True)
    unit_id = fields.Many2one('materials.units', 'Unit')
    # Added by Muthu
    boq = fields.Float('BoQ')
    is_sets = fields.Boolean('Sets')
    
    alert_units = fields.Char('Alert Units')    
    location_id = fields.Many2one('locations.locations','Location', required=True, domain="[('store_id.active_store','=',True)]")
    
    description = fields.Text('Description')
    
    available_units = fields.Float('Available Units')
    
    material_ids = fields.One2many('boq.material', 'boq_material_id', 'Materials Details')
    
    
    
    # need to remove the following fields
    date = fields.Datetime('DateTime')
    qty = fields.Integer('Quantity')
    material_count = fields.Float('Store Available Qty', compute='get_material_qty')
    
    
    @api.model
    def create(self, vals):
        ctx = dict(self._context or {})
        if ctx.get('material_type') == 1:
            vals.update({'is_sets': True})
        else:
            vals.update({'is_sets': False})
        
        res = super(MaterialMaterial, self).create(vals)
        for boq_mat in res.material_ids:
            if boq_mat:
                self.env['boq.boq'].create({'material_id': boq_mat.material_id.id, 'quantity': boq_mat.qty, 'date_created': boq_mat.date})
        return res

    @api.multi
    def unlink(self):
        for mat_mat in self:
            boq_object = self.env['boq.material'].search([('id', '=',mat_mat.id)])
            for boq_mat in boq_object:
                boq_mat.unlink()
        return super(MaterialMaterial, self).unlink()