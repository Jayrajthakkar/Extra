from odoo import http
from odoo.http import request
import base64

class UserPage(http.Controller):
	
	@http.route(route='/users',type="http",auth="public",website=True)
	def userpage(self,**kw):
		users = request.env['res.users'].search([])
		print(users)
		return request.render('sale_qweb.user_template_page',{'users':users})
	
	@http.route(route='/customer/details',type='http',auth='public',website=True)
	def customer_page(self,**kw):
		customers = request.env['res.partner'].search([])
		return request.render('sale_qweb.customer_template_page',{'customers':customers})

	@http.route(route='/customer/form',type='http',auth='public',website=True)
	def customer_form_page(self,**kw):
		return request.render('sale_qweb.partner_template_page',{})

	@http.route(route='/create/partner',type='http',auth='public',website=True)
	def partner_page(self,**kw):
		image = kw.get('image_1920')
		binary_image = base64.b64encode(image.read())
		
		partner_vals = {
		'name':kw.get('name'),
		'phone':kw.get('phone'),
		'email':kw.get('email'),
		'image_1920':binary_image
		}
		partner = request.env['res.partner'].create(partner_vals)


		Attachment = request.env['ir.attachment']
		file_name = kw.get('image_1920').filename
		# file = post.get('attachment')
		attachment_id = Attachment.create({
		'name': file_name,
		'type': 'binary',
		'datas': binary_image,
		'res_model': partner._name,
		'res_id': partner.id
		})
		return request.render('website.contactus_thanks',{})
		