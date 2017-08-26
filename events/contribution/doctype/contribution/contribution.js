// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt
// cur_frm.add_fetch(link_field, source_fieldname, target_fieldname);
cur_frm.add_fetch("invoice","base_total","total_sales");
frappe.ui.form.on('Contribution', {
	refresh: function(frm) {

	}
});
