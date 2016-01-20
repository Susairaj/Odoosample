
{
    'name': 'Project Site Inventory Tracker',
    'version': '0.1',
    'category': 'Inventory',
    'sequence': 3,
    'summary': 'Project Site Inventory Tracker',    
    'description': 'Project Site Inventory Tracker.',
    'author': 'Brand Equity Solutions',
    'depends' : ['base','board'],
    'data' : [
              # Configuration
              'views/configuration/issue_attachment_view.xml',
              'views/configuration/material_configuration_view.xml',
              'views/configuration/materials_units_view.xml',
              'views/configuration/price_level_view.xml',
              'views/configuration/receiving_attachment_view.xml',
              'views/configuration/return_attachment_view.xml',
              'views/configuration/return_reason_view.xml',
              
              # demo
              'views/demo/attachment_type_demo.xml',
              'views/demo/material_demo_data.xml',
              'views/demo/states_demo_data.xml',
              
              # Master
              'views/master/supplier_view.xml',
              'views/master/res_company_view.xml',
              'views/master/blocks_view.xml',
              'views/master/contractor_view.xml',
              'views/master/location_view.xml',
              'views/master/materials_categories_view.xml',
              'views/master/material_view.xml',
              'views/master/material_sets_view.xml',
              'views/master/boq_view.xml',
              'views/master/project_view.xml',
              'views/master/store_access_view.xml',              
              
              # Site Inspector
              'views/site_inspector/site_inspector_view.xml',
              
              # Transactions
              'views/transactions/inter_store_view.xml',
              'views/transactions/issues_returns_view.xml',
              'views/transactions/issues_view.xml',
              'views/transactions/material_receiving_view.xml',
              'views/transactions/material_return_view.xml',
              'views/transactions/receiving_inter_store_transfer_view.xml',
              'views/transactions/sequence.xml',
              
              'views/show_menus_view.xml',
              'views/master/store_view.xml',
              'views/menu.xml',
              'views/webclient_templates.xml',              
              
              #
#               # Moses
#               'views/master/states_demo_data.xml',
#               'views/master/blocks_view.xml',
#               'views/master/location_view.xml',
#               'views/master/material_view.xml',
#               'views/master/receiving_inter_store_transfer_view.xml',
#               
#               # Muthu
#               'views/master/res_company_view.xml',
#               'views/master/supplier_view.xml',
#               'views/master/contractor_view.xml',
#               'views/master/material_demo_data.xml',
#               'views/master/store_access_view.xml',
#               
#               #Sathish
#               'views/master/sequence.xml',
#               'views/master/issues_view.xml',
#               'views/master/inter_store_view.xml',
#               'views/master/issues_returns_view.xml',
#               
#               # Susai
#               'views/master/project_view.xml',
#               'views/master/material_receiving_view.xml',
#               'views/master/material_return_view.xml',
#               'views/master/material_return_reason_view.xml',
#               'views/master/site_inspector_view.xml',
#               'views/show_menus_view.xml',
#               'views/master/store_view.xml',
#               'views/master/attachment_type_demo.xml',
#               
#               'views/master/store_configuration_view.xml',
#               'views/menu.xml',
#               'views/master/webclient_templates.xml',
    ],
    'qweb' : [
        "static/src/xml/*.xml",
    ],
    'demo' : [],
    'test' : [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
