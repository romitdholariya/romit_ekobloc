import frappe


# @frappe.whitelist()
# def get_stock_quantity(qty,conversion_factor):
#     if conversion_factor:
#         stock_qty = int(float(qty) * float(conversion_factor))
        # return stock_qty


# def before_save(self,method):
#     for i in self.items:
#         if i.conversion_factor:
#             decimal_part= i.stock_qty % 1
#             if decimal_part >= 0.5:
#                 i.stock_qty = int(i.stock_qty) + 1
#             else:
#                 i.stock_qty = int(i.stock_qty)

    # self.stock_qty=int(self.stock_qty)

def truck_update(self,method):
    # frappe.db.set_value("Truck",self.truck_name,"load",1)
    doc = frappe.get_doc("Truck",self.truck_name)
    doc.load = 1
    doc.save()
    frappe.db.commit()
