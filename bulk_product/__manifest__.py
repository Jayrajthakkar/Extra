{
    'name': 'Bulk Products',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'This is Bulk Products System',
    'description': """
    This is Bulk Products System.
    """,
    'sequence':-500,
    'depends': ['sale_management'],
    'data':["security/ir.model.access.csv",
    "views/bulk_product_view.xml",
    "views/sale_inherit_view.xml"],
    'installable':True,
    'auto_install':False,
    'application':True,
    'license': 'LGPL-3',
}