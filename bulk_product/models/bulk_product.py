from odoo import models, fields, api
from datetime import date


class BulkProduct(models.Model):
	_name="bulk.product"

	name = fields.Char(string="Name")
	user_id = fields.Many2one(string="User",comodel_name="res.partner")
	email = fields.Char(string="Email")
	bulk_product_ids = fields.Many2many(string="Bulk Products",comodel_name="product.product",domain="[('detailed_type','=','product')]")


class SaleOrder(models.Model):
	_inherit="sale.order"

	bulk_product_id = fields.Many2one(string="Bulk Product",comodel_name="bulk.product")

	@api.onchange('bulk_product_id')
	def insert_product(self): 
		product =[]
		for sale_order in self.bulk_product_id.bulk_product_ids:
			product.append((0,0,{
				'product_id':sale_order.id,
				'product_uom_qty':1
				}))
		
		self.write(
				{
				'order_line':product
				})	

			
		for product in self.order_line:
			product._update_description()


		my_product = self.env['product.template'].search([('detailed_type','=','consu' and 'product')])

		print("--------------------------------------------",my_product)