from odoo import models, fields, api

class SaleOrder(models.Model):
	_inherit = 'sale.order'
	_description = 'This model stores the data about the sales information'
		