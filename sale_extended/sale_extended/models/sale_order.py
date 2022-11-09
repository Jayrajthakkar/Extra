from odoo import models,fields,api

class SaleOrder(models.Model):
	_inherit=['sale.order']

	sale_price = fields.Float(string='Price')
	sale_date = fields.Date(string='Date')



	def action_view_price(self):
		pass

	



	def _action_confirm(self):

		template_id = self.env.ref('sale.model_sale.order').id
		self.env['mail.template'].browse(template_id).send_mail(self.id,force_send=True)