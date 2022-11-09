from odoo import models,fields,api

class  CityData(models.Model):
	_name = 'city.city'
	_description='This table store cities data'
	_rec_name='city'


	city = fields.Char(string='City')
	state_id = fields.Many2one(string='State',comodel_name='res.country.state')



class city_select(models.Model):
	_inherit ='res.partner'


	city_id= fields.Many2one(comodel_name='city.city',string='City',domain='[("state_id","=?",state_id)]')
