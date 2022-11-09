from odoo import models,fields,api

class ResConfig(models.Model):
	_inherit='res.company'


	state  = fields.Char(string='Set State')
	