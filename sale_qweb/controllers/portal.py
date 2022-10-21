from odoo import http
from odoo.http import request

class UserPage(http.Controller):
	
	@http.route(route='/users',type="http",auth="public",website=True)
	def userpage(self,**kw):
		users = request.env['res.users'].search([])
		print(users)
		return request.render('sale_qweb.user_template_page',{'users':users})
	@http.route(route='/customer',type='http',auth='public',website=True)
	def customer_page(self,**kw):
		customers = request.env['res.partner'].search([])
		return request.render('sale_qweb.customer_template_page',{'customers':customers})