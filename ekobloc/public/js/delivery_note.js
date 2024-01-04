frappe.ui.form.on('Delivery Note Item', {
    uom: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
        if (d.stock_qty) {
        var stockQtyRounded = parseFloat(d.stock_qty).toFixed(2);
        
        // Check the value after the decimal point
        var decimalPart = parseFloat("0." + stockQtyRounded.toString().split(".")[1]);
        
        // If the value after the decimal point is greater than or equal to 0.5, add 1 to stockQtyInt
        var stockQtyInt = parseInt(d.stock_qty);
        if (decimalPart >= 0.5) {
            stockQtyInt += 1;
        }
        
        // Update the stock_qty field with the rounded and adjusted value
        frappe.model.set_value(cdt, cdn, 'stock_qty', stockQtyInt);
    
            // var stockQtyInt = parseInt(d.stock_qty);
            // frappe.model.set_value(cdt, cdn, 'stock_qty', stockQtyInt);
        }
    }
});

frappe.ui.form.on('Delivery Note',{
    setup:function(frm){
        frm.set_query('truck_name',function(){
            return{
                filters:[
                    ["load", '=', 0]
                ]
            }
        })
    }
})

// setup: function(frm) {
//     // Set a query filter on the "address" link field
//     frm.set_query('address', function() {
//         return {
//             filters: [
//                 ['Dynamic Link', 'link_doctype', '=', 'Company'],
//                 ['Dynamic Link', 'link_name', '=', frm.doc.company]
//             ]
//         };
//     });



// frappe.ui.form.on('Delivery Note Item', {
//     uom: function(frm, cdt, cdn) {
//         updateStockQty(frm, cdt, cdn);
//     },
//     stock_qty: function(frm, cdt, cdn) {
//         updateStockQty(frm, cdt, cdn);
//     }
//     // qty: function(frm, cdt, cdn) {
//     //     console.log("Qty field change event triggered.");
        
//         // Rest of your code...
//     // }
// });

// function updateStockQty(frm, cdt, cdn) {
//     var d = locals[cdt][cdn];
//     if (d.stock_qty) {
//         var newStockQty = d.qty * d.conversion_factor;
//         var stockQtyRounded = parseFloat(newStockQty).toFixed(2);
//         var decimalPart = parseFloat("0." + stockQtyRounded.toString().split(".")[1]);
//         var stockQtyInt = parseInt(newStockQty);
//         if (decimalPart >= 0.5) {
//             stockQtyInt += 1;
//         }
//         frappe.model.set_value(cdt, cdn, 'stock_qty', stockQtyInt);
//     }
// }


// frappe.ui.form.on('Delivery Note Item', {
//     uom: function(frm, cdt, cdn) {
//         updateStockQty(frm, cdt, cdn);
//     },
//     qty: function(frm, cdt, cdn) {
//         updateStockQty(frm, cdt, cdn);
//     }
// });

// function updateStockQty(frm, cdt, cdn) {
//     var d = locals[cdt][cdn];
//     if (d.stock_qty) {
//         // Round the stock_qty value to 2 decimal places
//         var stockQtyRounded = parseFloat(d.stock_qty).toFixed(2);
        
//         // Check the value after the decimal point
//         var decimalPart = parseFloat("0." + stockQtyRounded.toString().split(".")[1]);
        
//         // If the value after the decimal point is greater than or equal to 0.5, add 1 to stockQtyInt
//         var stockQtyInt = parseInt(d.stock_qty);
//         if (decimalPart >= 0.5) {
//             stockQtyInt += 1;
//         }
        
//         // Update the stock_qty field with the rounded and adjusted value
//         frappe.model.set_value(cdt, cdn, 'stock_qty', stockQtyInt);
//     }
// }





// frappe.ui.form.on('Delivery Note Item', {
//     uom: function(frm, cdt, cdn) {
//         updateStockQty(frm, cdt, cdn);
//     },
//     qty: function(frm, cdt, cdn) {
//         updateStockQty(frm, cdt, cdn);
//     }
// });

// function updateStockQty(frm, cdt, cdn) {
//     var d = locals[cdt][cdn];
//     // if (d.stock_qty) {
//         var stockQtyInt = parseInt(d.stock_qty);
//         frappe.model.set_value(cdt, cdn, 'stock_qty', stockQtyInt);
//     // }
// }





    // qty: function(frm, cdt, cdn) {
    //     var d = locals[cdt][cdn];
    //     if (d.stock_qty) {
    //         var newStockQty = d.qty * d.conversion_factor;
    //         var stockQtyRounded = parseFloat(newStockQty).toFixed(2);
    //         var decimalPart = parseFloat("0." + stockQtyRounded.toString().split(".")[1]);
    //         var stockQtyInt = parseInt(newStockQty);
    //         if (decimalPart >= 0.5) {
    //             stockQtyInt += 1;
    //         }
    //         frappe.model.set_value(cdt, cdn, 'stock_qty',stockQtyInt );
    //     }
    // }
    // qty: function(frm, cdt, cdn) {
    //     var d = locals[cdt][cdn];
        
    //     if ( d.stock_uom && d.uom && d.conversion_factor ) {
            
    //         frappe.call({
    //             method:"ekobloc.the_block.doc_events.delivery_note.get_stock_quantity",
    //             args:{
    //                 conversion_factor:d.conversion_factor,
    //                 qty:d.qty
    //             },
    //             callback: function(r) {
    //                 if (r.message) {
    //                     console.log("Qty field change event triggered.");
    //                     console.log(r);
    //                     frappe.model.set_value(cdt, cdn, 'stock_qty', r.message);
    //                 }
    //             }

    //         })
            // var stockQtyInt = parseInt(d.stock_qty);
            // frappe.model.set_value(cdt, cdn, 'stock_qty', stockQtyInt);
    //     }
    // }
// });

// frappe.ui.form.on('Delivery Note Item', {
//     uom:function(frm, cdt, cdn){
//         var d = frappe.get_doc(cdt,cdn);
//         // frappe.model.get_value(cdt, cdn, 'stock_qty')
//         if (d.stock_qty){
//         frappe.model.set_value(cdt, cdn, 'stock_qty', int(d.stock_qty))
//         }
//     }
    // party: function(frm, cdt, cdn) {
    //     var d = frappe.get_doc(cdt, cdn);
    //     if (d.party_type && d.party) {
    //         frappe.call({
    //             method: "mehta.mehta_group.doc_events.journal_entry.get_party_name",
    //             args: {
    //                 company: frm.doc.company,
    //                 party_type: d.party_type,
    //                 party: d.party
    //             },
    //             callback: function(r) {
    //                 if (r.message) {
    //                     frappe.model.set_value(cdt, cdn, 'cust_party_name', r.message);
    //                 }
    //             }
    //         }); 
    //     }
    // }
// });
