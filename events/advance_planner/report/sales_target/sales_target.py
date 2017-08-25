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
	sales_invoices = get_sales_invoices(filters)
	total_st = []
	sales_target_qty = 0.0
	grand_total = 0.0
        for d in items:
		if d.sales_target_quantity:
			sales_target_qty += flt(d.sales_target_quantity)
                data.append([d.company, d.branch, d.posting_date, d.item_code, d.sales_target_quantity, d.si_name, "", "Sales Target" ])

	for d in sales_invoices:
		if d.grand_total:
			grand_total += flt(d.grand_total)
		data.append([d.company, d.branch, d.posting_date, d.item_code, "", d.name, d.grand_total, "Sales Invoice"])
	data.append(["", "", "", _("Total"), sales_target_qty, "", grand_total, ""])
       	return columns, data 		
	
	
		

def get_condition(filters):
        condition = ""
        if filters.get("company"): condition += "  and company=%(company)s"
        if filters.get("from_date") and filters.get("due_date"): condition += " and posting_date BETWEEN %(from_date)s AND %(due_date)s"
        if filters.get("branch"):  condition += " and branch=%(branch)s"
        if filters.get("item_code"): condition += " and item_code=%(item_code)s"
        #if filters.get("sales_target_quantity"): condition += " and sales_target_quantity=%(sales_target_quantity)s"
        return condition


def get_columns():
        "Return columns based on filters"
        columns  = [
                _("Company")+":Link/Company:120", _("Branch Name")+":Link/Branch:120", _("Posting Date")+":Date:120", _("Item Code")+":Link/Item:150",
                _("Sales Target Quantity")+":Data:200", _("Invoice")+":Data:200", _("Amount")+":Data:200", _("Type")+":Data:200"
	]
	return columns

def get_data(filters):
        condition = get_condition(filters)
        data_list = frappe.db.sql("""SELECT  ST.company, ST.branch, ST.due_date, ST.posting_date, IST.item_code, IST.sales_target_quantity
                                FROM `tabSales Target` ST, `tabItem Sales Target` IST
                                WHERE ST.name = IST.parent AND ST.docstatus  = 1  AND IST.docstatus = 1  %s """%condition, filters, as_dict = 1)
        return data_list


def get_sales_invoices(filters):
	condition = get_condition(filters)
	sales_invoices = frappe.db.sql("""SELECT SI.company, SI.branch, SI.posting_date, SI.name, SI.grand_total, SII.item_code FROM 
					`tabSales Invoice` SI INNER JOIN `tabSales Invoice Item` SII  ON SI.name = SII.parent WHERE SI.docstatus = 1 
					AND SII.docstatus = 1 %s """%condition, filters, as_dict = 1)
	return sales_invoices

