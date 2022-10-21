from odoo import models, fields, api

class Order(models.Model):
	_name = 'trading.order'
	_description = 'This model stores the data about the purchase information'
	_rec_name = 'customer_id'

	customer_id = fields.Many2one(comodel_name='trading.customer',string='Customer')
	product_ids = fields.Many2many(comodel_name='trading.product',string='Product')
	quantity = fields.Integer(string='Quantity')
	price = fields.Integer(string='price')
	total = fields.Integer(string='Gross total')


	# @api.onchange('product_id')
	# def check_price(self):
	# 	self.price = self.product_id.prices


