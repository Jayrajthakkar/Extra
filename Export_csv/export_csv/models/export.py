from odoo import models,fields,api

class Export(models.Model):
	_name = 'export.sale'
	_description ='this table store export sale data'

	partner_ids = fields.Many2many(comodel_name='res.partner',string='Partner')