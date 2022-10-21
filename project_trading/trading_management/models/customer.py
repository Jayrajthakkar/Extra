from odoo import models, fields, api

class Customer(models.Model):
	_name = 'trading.customer'
	_description = 'This model stores the data about the customer information'

	name = fields.Char(string='Name')
	contact_phone = fields.Char(string='Number')
	email = fields.Char(string='Email')
	address = fields.Text(string='Address')