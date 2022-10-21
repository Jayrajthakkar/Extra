
{
    'name': 'Sale Management',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'This is Sale Management System',
    'description': """
    This is Sale Management System.
    """,
    'sequence':-500,
    'depends': ['sale','sale_management','website'],
    'data':['report/qweb_header_inherit.xml',
            'report/action_sale_report.xml',
            'report/template_sale_report.xml',
            'views/controller_usr_template.xml',
            'views/controller_order_template.xml',],
    'installable':True,
    'auto_install':False,
    'application':True,
    'license': 'LGPL-3',
}