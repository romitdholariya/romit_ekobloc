// Copyright (c) 2023, Prashant Kamble and contributors
// For license information, please see license.txt

frappe.ui.form.on('Request For Material', {
	// refresh: function(frm) {

	// }
	onload:function(frm){
	frm.fields_dict['items'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
				return {
					filters: {
						'item_group': '11 FG'
					}
				};
			};
            var currentDate = frappe.datetime.get_today();

        // Set the value of the "transaction_date" field to the current date
            cur_frm.set_value("transaction_date", currentDate);
        // frm.set_value("transaction_date",today())
            frappe.call({
                method:"ekobloc.the_block.doctype.request_for_material.request_for_material.get_customer_name",
                callback:function(r){
                    if(r.message){
                        frm.set_value("customer",r.message)
                    }
                }
            })

    
		},

        setup: function(frm) {
            // Set a query filter on the "address" link field
            frm.set_query('address', function() {
                return {
                    filters: [
                        ['Dynamic Link', 'link_doctype', '=', 'Company'],
                        ['Dynamic Link', 'link_name', '=', frm.doc.company]
                    ]
                };
            });

            // frm.set_query('address', function() {
            //     return {
            //         filters: [
            //             ['Dynamic Link', 'link_doctype', '=', 'Company'],
            //             ['Dynamic Link', 'link_name', '=', frm.doc.company]
            //         ]
            //     };
            // });
        }
        // setup:function (frm){
        //        frm.doc.set_query("address",function(){
        //         return{
        //             filters: [
        //             ['Dynamic Link', 'link_doctype', '=', 'Customer'],
        //             ['Dynamic Link', 'link_name', '=', frm.doc.customer]
        //         ]
        //         };
        //        });
        //     }
            // frappe.call({
            //     method:"ekobloc.the_block.doctype.request_for_material.request_for_material.get_customer_name",
            //     callback:function(r){
            //         if(r.message){
            //             frm.set_value("customer",r.message)
            //         }
            //     }
            // })
});

// setup:function frm(){
//     frappe.call({
//         method:"ekobloc.the_block.doctype.request_for_material.request_for_material.get_customer_name",
//         callback:function(r){
//             if(r.message){
//                 frm.set_value("customer",r.message)
//             }
//         }
//     })
// }
frappe.ui.form.on('Request For Material', 'address', function(frm) {
    if (frm.doc.address) {
        return frm.call({
            method: "frappe.contacts.doctype.address.address.get_address_display",
            args: {
                "address_dict": frm.doc.address

            },
            callback: function(r) {
                if (r.message) {
                    frm.set_value("delivery_address", r.message);
                }
            }
        });
    } else {
        frm.set_value("delivery_address", "");
    }
});

// frappe.ui.form.on('Request For Material', {
    // setup: function(frm) {
    //     // Set a query filter on the "address" link field
    //     frm.set_query('address', function() {
    //         return {
    //             filters: [
    //                 ['Dynamic Link', 'link_doctype', '=', 'Customer'],
    //                 ['Dynamic Link', 'link_name', '=', frm.doc.customer]
    //             ]
    //         };
    //     });
    // }
// });

