# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt
def execute(filters=None):
	columns, data = ["Item:link/Item:200","Total Qty:Float:100","Qty Percent:Percent:100","Total Sales:Currency:200","Sales Percent:Percent:100","Total Cost:Currency:200","Cost Percent:Percent:100"], []
	result = frappe.db.sql("""select cr.item_code , sum(cr.amount) , sum(cr.qty),sum(cr.cost) 
		from `tabContribution Result` cr join `tabContribution Tool` p on cr.parent=p.name
		where p.docstatus=1 and (p.date between "{}" and "{}") group by cr.item_code 
		""".format(filters.get("from_date"),filters.get("to_date")),as_list=1)
	total_cost=0
	total_qty=0
	total_sales=0
	for row in result:
		total_cost=flt(row[3])
		total_qty=flt(row[2])
		total_sales=flt(row[1])
	for row in result:
		data.append([row[0],row[1],((flt(row[1])/total_qty)*100),row[2],((flt(row[2])/total_sales)*100),row[3],((flt(row[3])/total_cost)*100)])
	return columns, data
