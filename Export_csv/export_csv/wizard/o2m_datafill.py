from odoo import models,fields,api


class OneToMany(models.TransientModel):
	_name = 'o2m.data.wizard'
	_description ='this table store Quotation data'
	
	quote_id = fields.Many2one(string='Quotation',comodel_name='sale.order',domain=[('state','=','draft')])
	product_ids = fields.One2many(string='Quotation',comodel_name='product.wizard',inverse_name='quote_id')
	partner_ids = fields.Many2many(string='Partner',comodel_name='res.partner')



	def add_data(self):
		print(self.quote_id)
		add_products=[]
		for records in self.product_ids:
			add_products.append((0,0,{'product_id':records.product_id.id,
					'product_uom_qty':records.quantity,'price_unit':records.price}
					))
			print("__________________",add_products)
		self.quote_id.write(
			{'order_line':add_products,
			 'partner_ids':[(6,0,self.partner_ids.ids)]
				
			})
	




class Product(models.TransientModel):
	_name = 'product.wizard'
	_description ='this table store product data'


	quote_id = fields.Many2one(string='Quotation',comodel_name='o2m.data.wizard')
	product_id = fields.Many2one(string='Product',comodel_name='product.product')
	quantity= fields.Integer(string='Quantity')
	price = fields.Float(string='Price')


 
