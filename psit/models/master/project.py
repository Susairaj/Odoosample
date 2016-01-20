from openerp import models, fields

"""  Author : Susai S  """ 
class ProjectProject(models.Model):
    _name = "project.project"
    _description = "Projects"

    name = fields.Char('Name', required=True)
    project_manual_id = fields.Char('Unique Manual Id', required=True)
    company_id = fields.Many2one('res.company', 'Company', required=True)
    project_type = fields.Char('Type')
    description = fields.Text('Description')