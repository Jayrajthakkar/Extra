from odoo import models,fields,api

class ResConfig(models.TransientModel):
	_inherit='res.config.settings'


	state_check = fields.Char(related='company_id.state',string='Set State',readonly=False)
