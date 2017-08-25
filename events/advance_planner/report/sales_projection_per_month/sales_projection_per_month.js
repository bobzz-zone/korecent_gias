// Copyright (c) 2016, Ros@gmail.com and contributors
// For license information, please see license.txt

frappe.query_reports["Sales Projection Per Month"] = {
	"filters": [
                {
                   "fieldname":"company",
                   "label":__("Company"),
                   "fieldtype": "Link",
                   "options": "Company",
                   "default": frappe.defaults.get_user_default("Company")
                },
                {
                   "fieldname":"date",
                   "label":__("Month"),
                   "fieldtype":"Select",
                   "options": ["January","February","March","April","May","June","July","August","Septamber","October","November","December"]
                },
                {
                   "fieldname":"year",
                   "label":__("Year"),
                   "fieldtype":"Link",
                   "options": "Fiscal Year"
                },
                {
                   "fieldname":"item_code",
                   "label":__("Item Code"),
                   "fieldtype":"Link",
                   "options": "Item"
                },
                {
                   "fieldname":"branch_name",
                   "label":__("Branch name"),
                   "fieldtype":"Link",
		   "options": "Branch"
                },
                {
                   "fieldname":"sales_projection_quantity",
                   "label":__("Sales Projection Quantity"),
                   "fieldtype":"Float"
                }
     



	]
}
