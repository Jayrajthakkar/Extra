from odoo import models, fields, api

class Product(models.Model):
	_name = 'trading.product'
	_description = 'This model stores the data about the product information'

	name = fields.Char(string='Name')
	quantity=fields.Char(string='Quantity')
	buy_price = fields.Integer(string='price')
	sale_price = fields.Integer(string='price')
	category = fields.Selection([('Ghee & Oils','Ghee & Oils'),('Dry Fruits','Dry Fruits'),('Flour','Flour'),('Grains','Grains'),('Rice','Rice'),('Salt Sugar & Jaggery','Salt Sugar & Jaggery'),('Spices','Spices'),('Papad','Papad')])
	order_ids = fields.One2many(comodel_name='trading.order',inverse_name='customer_id',string='Order')


