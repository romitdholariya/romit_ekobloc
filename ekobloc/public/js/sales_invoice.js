// frappe.ui.form.on('Payment Entry', {
//     customer:function(frm){
//         frappe.call({
//             method:"ekobloc.the_block.doc_events.sales_invoice.get_outstanding_amount",
//             args:{
//                 company:frm.doc.company,
//                 date: frm.doc.posting_date,
//                 party: frm.doc.customer

//             },
//             callback: function(r){
//                 if(r.message){
//                     frm.set_value("customer_outstanding_amount",r.message)
//                 }
//             }
//         })
//     }
// })

frappe.ui.form.on('Sales Invoice', {
    customer: function(frm) {
        if (frm.doc.posting_date && frm.doc.company && frm.doc.customer) {
       

        frappe.call({
            method: "ekobloc.the_block.doc_events.sales_invoice.get_outstanding_amount",
            args: {
                company: frm.doc.company,
                date: frm.doc.posting_date,
                party: frm.doc.customer
            },
            callback: function(r) {
                if (r.message) {
                    frm.set_value("customer_outstanding_amount", r.message);
                }
            }
        })
    }
    }
})
