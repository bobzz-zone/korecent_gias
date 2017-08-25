# Copyright (c) 2013, Ros@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt , cint , cstr

def execute(filters=None):
	if not filters: filters = {}
	columns  = get_columns()
        
       
	data = []
	items= get_data(filters)
	for d in items:
		data.append([d.company, d.branch_name, d.date, d.year, d.item_code, d.sales_projection_quantity])
	return columns, data
		

def get_condition(filters):
	condition = ""
	if filters.get("company"): condition += "  and company=%(company)s"
	if filters.get("date"): condition += " and date=%(date)s"
	if filters.get("year"): condition +=  " and year=%(year)s"
	if filters.get("branch_name"):  condition += " and branch_name=%(branch_name)s"
	if filters.get("item_code"): condition += " and item_code=%(item_code)s"
	if filters.get("sales_projection_quantity"): condition += " and sales_projection_quantity=%(sales_projection_quantity)s"
	return condition
	

def get_columns():
	"Return columns based on filters"
	columns  = [
		_("Company")+":Data:120", _("Branch Name")+":Link/Branch:120", _("Month")+":Data:100", _("Year")+":Link/Fiscal Year:120", _("Item Code")+":Link/Item:150",
		_("Sales Projection Quantity")+":Data:200"
	]
	return columns

def get_data(filters):
	condition = get_condition(filters)	
	data_list = frappe.db.sql("""SELECT  SP.company, SP.branch_name, SP.date, SP.year, IAP.item_code, IAP.sales_projection_quantity
				FROM `tabSales Projections` SP INNER JOIN  `tabItem Advance Planner` IAP
				ON SP.name = IAP.parent WHERE SP.docstatus  = 1  AND IAP.docstatus = 1  %s """%condition, filters, as_dict = 1)
	return data_list
	
	
