# -*- coding: utf-8 -*-
# Copyright (c) 2015, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import  flt
class Contribution(Document):
	def calculate(self):
		if self.total_cost<=0:
			frappe.throw("Please set the cost")
		if not self.total_cost:
			frappe.throw("Please set the cost")
		if not self.items:
			frappe.throw("Please select the invoice")
		cost = self.total_cost
		devided = self.devided
		total_sales=0
		total_qty=0
		invoices=""
		for row in self.items:
			total_sales+=flt(row.total_sales)
			if invoice=="":
				invoice=""" "{}" """.format(row.invoice)
			else:
				invoice = """{} ,"{}"" """.format(invoice,row.invoice)
		items = frappe.db.sql("""select item_code, sum(qty),sum(amount) from `tabSales Invoice Item` where parrent IN ({}) group by item_code """.format(invoice),as_list=1)
		if devided=="qty":
			for row in items:
				total_qty+=flt(row[1])
		self.result=[]
		for row in items:
			cr = self.append('result', {})
			cr.item_code = row[0]
			cr.qty = row[1]
			cr.amount = row[2]
			per=0
			add=0
			if devided=="qty":
				per = (flt(row[1])/total_qty)*100
				add=(flt(row[1])/total_qty)*cost
			else:
				per = (flt(row[2])/total_sales)*100
				add=(flt(row[2])/total_sales)*cost
			cr.cost = add
			cr.percent = cost