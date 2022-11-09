# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Sale_Extended',
    'version' : '1.2',
    'summary': 'Sale_Extended System',
    'sequence': 10,
    'description': """Sale_Extended System""",
    'category': 'Extra',
    'website': 'https://www.odoo.com',
    'depends' : [],
    'data': ['security/ir.model.access.csv',
             # 'data/mail.xml'   
            # 'views/sale_extended.xml',
            'views/city_view.xml',
            'views/city_inherit_view.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
