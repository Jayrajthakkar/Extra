from odoo import models,fields,api

class Partner(models.Model):
	_inherit='sale.order'

	partner_ids = fields.Many2many(string='Partners',comodel_name='res.partner')
	product_id = fields.Many2one(string='Product',comodel_name='product.product')
	quantity = fields.Float(string='Quantity') 




	@api.onchange('product_id','quantity')
	def add_data(self):
		print('customer name',self.partner_id.name) 
		
		if self.product_id not in self.order_line.product_id:
			add_product=[(0,0,{'product_id':self.product_id,'product_uom_qty':self.quantity})]
			self.write({'order_line':add_product})
		
		else:
			for record_order in self.order_line:
				print("----",record_order.product_id.name,record_order.product_uom_qty,'line id is',record_order.id)
				if self.product_id.id == record_order.product_id.id:
					add_product = [(1,record_order.id,{'product_uom_qty':self.quantity})]

					self.write({'order_line':add_product})
				
		
			
		
		# print('Method Call',self.product_id,self.quantity)
		# print('customer name',self.partner_id.name)
		# print('product name and quantity ',self.product_id.name,self.quantity)
		# # print(self.product_id)

		# if self.product_id  in self.order_line.product_id :

		# 	print(self.order_line.product_id.ids)
			
		# 	add_product =[(1,self.product_id.id,{'product_uom_qty':self.quantity})]
		# 	print("----------",add_product)
		# 	self.write({'order_line':add_product})


		# else:

		# 	add_product =[(0,0,{'product_id':self.product_id.id,'product_uom_qty':self.quantity})]

		# 	print("===========",add_product)


		# 	self.write(
		# 		{'order_line':add_product})