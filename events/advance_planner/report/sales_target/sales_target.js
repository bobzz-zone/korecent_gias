// Copyright (c) 2016, Ros@gmail.com and contributors
// For license information, please see license.txt

frappe.query_reports["Sales Target"] = {
	"filters": [
		{
                   "fieldname":"company",
                   "label":__("Company"),
                   "fieldtype": "Link",
                   "options": "Company",
                   "default": frappe.defaults.get_user_default("Company")
                },
                {
                   "fieldname":"from_date",
                   "label":__("From Date"),
                   "fieldtype":"Date"
                },
                {
                   "fieldname":"due_date",
                   "label":__("To Date"),
                   "fieldtype":"Date"
                },
                {
                   "fieldname":"item_code",
                   "label":__("Item Code"),
                   "fieldtype":"Link",
                   "options": "Item"
                },
                {
                   "fieldname":"branch",
                   "label":__("Branch name"),
                   "fieldtype":"Link",
                   "options": "Branch"
                }

	]
}
