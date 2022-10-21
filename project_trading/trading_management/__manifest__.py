# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Trading Management',
    'version' : '1.2',
    'summary': 'Trading Management System',
    'sequence': 10,
    'description': """Trading Management System""",
    'category': 'Trading',
    'website': 'https://www.odoo.com',
    'depends' : ['base_setup'],
    'data': ['security/ir.model.access.csv',
             'views/customer.xml',
             'views/product.xml',
             'views/order.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
