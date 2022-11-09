from odoo import models,fields,api
import csv 

class ExportDate(models.TransientModel):
	_name = 'export.date.wizard'
	_description ='this table store export date data'
	_rec_name = 'start_date'

	start_date = fields.Date(string='Start Date',required=True)
	end_date = fields.Date(string='End Date',required=True)



	
	def action_export(self):
		print("------------button click-------------------")
		result = self.env['sale.order'].search([('state','=',self.env.user.company_id.state.split(','))])

		header=['Sr_No','Customer','Quotation','Salesperson','Total']
		

		f = open('/home/odoo/Desktop/Export_csv/export.csv','w')
		writer = csv.writer(f)
		writer.writerow(header)

		sr_no=0		
		for record in result:
			if record.date_order.date()>self.start_date and  record.date_order.date()<self.end_date:
				data=[]
				sr_no +=1
				data.append(sr_no)
				data.append(record.partner_id.name)
				data.append(record.date_order)
				data.append(record.user_id.name)
				data.append(record.	amount_total)
		
			writer.writerow(data)
		f.close()


 
			