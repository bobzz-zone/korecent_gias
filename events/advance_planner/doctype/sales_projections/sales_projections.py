# -*- coding: utf-8 -*-
# Copyright (c) 2015, Ros@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class SalesProjections(Document):
	pass

@frappe.whitelist()
def get_items(product_category = None):
	if not product_category:
		return []
	data = frappe.db.get_values("Item", filters={"item_group":product_category}, fieldname="*", as_dict = True)
	if  not data:
		return []
	temp = []
	for item in data:
		temp_dict = {}
		temp_dict['item_code'] = item['item_code']
		temp_dict['product_category'] = item['item_group']
		temp.append(temp_dict)
		del temp_dict
	return temp
