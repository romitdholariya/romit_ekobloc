import frappe

@frappe.whitelist()
def party_name(self,method):
    for i in self.accounts:
        if i.party_type == "Customer":
            i.party_name = frappe.db.get_value("Customer",i.party,"customer_name")
            # frappe.throw(i.cust_party_name)
        elif i.party_type == "Supplier":
            i.party_name = frappe.db.get_value("Supplier",i.party,"supplier_name")
            # frappe.throw(i.cust_party_name)