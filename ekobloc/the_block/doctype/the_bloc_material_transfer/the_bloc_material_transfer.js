// Copyright (c) 2023, Prashant Kamble and contributors
// For license information, please see license.txt

frappe.ui.form.on('THE Bloc Material Transfer', {
	// refresh: function(frm) {
		onload:function(frm){
			frm.set_query('item_code',function(){
				return{
					filters:{
						'item_group':'All Item Groups'

					}
				}
			});
			frm.fields_dict['the_bloc_table_material_transfer'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
				return {
					filters: {
						'item_group': 'Products'
					}
				};
			};
		}
		// onload: function(frm) {
		// 	frm.fields_dict['the_bloc_table_material_transfer'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
		// 		return {
		// 			filters: {
		// 				'item_group': 'Products'
		// 			}
		// 		};
		// 	};
		// }

	// }
});


// frappe.ui.form.on('The Bloc Table Material Transfer', {
// 	the_bloc_table_material_transfer_add: function(frm, cdt, cdn) {
// 		var child = locals[cdt][cdn];
// 		// frappe.model.set_value(cdt, cdn, 'item_code', '');
// 		frappe.model.set_query(cdt, cdn, 'item_group', 'All Item Groups');
// 	}
// });


// frappe.ui.form.on('The Bloc Table Material Transfer', {
// 	// refresh: function(frm) {
// 		item_code:function(frm,cdt,cdn){
// 			var d = locals[cdt][cdn]
// 		return{
// 			filters:{
// 				'item_group':'All Item Groups'

// 			}
// 		}
		
// 	}
// 		// setup:function(frm){
// 		// 	frm.set_query('item_code',function(doc, cdt, cdn){
// 		// 		return{
// 		// 			filters:{
// 		// 				'item_group':'All Item Groups'

// 		// 			}
// 		// 		}
// 		// 	});
// 		// }

// 	// }
// });
