# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Export_csv',
    'version' : '1.2',
    'summary': 'Export_csv',
    'sequence': 10,
    'description': """Export_csv""",
    'category': 'Extra',
    'website': 'https://www.odoo.com',
    'depends' : ['sale','base'],
    'data':['security/ir.model.access.csv',
            'wizard/export_date_view.xml',
            'wizard/o2m_datafill.xml',
            'views/export_view.xml',
            'views/res_config_view.xml',
            'views/partner.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}