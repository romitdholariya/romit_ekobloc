# Copyright (c) 2023, Prashant Kamble and contributors
# For license information, please see license.txt

import frappe
import requests
import json
from frappe.model.document import Document

class THEBlocMaterialTransfer(Document):
	# pass


	def on_submit(self):

		 # Create a new Stock Entry document
		stock_entry = frappe.new_doc("Stock Entry")
		
		# Set the relevant fields from the Sales Order to the Stock Entry
		# stock_entry.sales_order = self.name
		stock_entry.stock_entry_type="Material Receipt"
		stock_entry.posting_date = self.posting_date
		# Set other required fields as needed
		
		# Iterate over the child item table of the Sales Order
		for item in self.the_bloc_table_material_transfer:
			# Create a new Stock Entry Detail document (child table of Stock Entry)
			stock_entry_item = stock_entry.append("items")
			
			# Set the relevant fields from the Sales Order item to the Stock Entry item
			stock_entry_item.item_code = item.item_code
			stock_entry_item.qty = item.output_qty
			stock_entry_item.s_warehouse = "Stores - MS"
			stock_entry_item.t_warehouse = "Site Warehouse - MS"

			
			# Set other required fields as needed


		stock_entry1 = frappe.new_doc("Stock Entry")
		
		# Set the relevant fields from the Sales Order to the Stock Entry
		# stock_entry.sales_order = self.name
		stock_entry1.stock_entry_type="Material Receipt"
		stock_entry1.posting_date = self.posting_date
		# Set other required fields as needed
		
		# Iterate over the child item table of the Sales Order
		for item1 in self.the_bloc_table_material_transfer:
			# Create a new Stock Entry Detail document (child table of Stock Entry)
			# if item1.damage_qty != 0:
			stock_entry_item1 = stock_entry1.append("items")
			
			# Set the relevant fields from the Sales Order item to the Stock Entry item
			stock_entry_item1.item_code = item1.item_code
			stock_entry_item1.qty = item1.damage_qty
			stock_entry_item1.s_warehouse = "Stores - MS"
			stock_entry_item1.t_warehouse = "Site Warehouse - MS"

			
			# Set other required fields as needed

		

		stock_entry.insert()
		stock_entry1.insert()
		stock_entry.submit()
		stock_entry1.submit()
		frappe.db.commit()



		# for i in self.the_bloc_table_material_transfer:
			# frappe.throw(i.output_qty)
			# frappe.throw(i.damage_qty)

		
		# 	stock_entry_data_issue = {
		# 	"doctype": "Stock Entry",
		# 	"company": "",
		# 	"posting_date": "2023-07-12",
		# 	"stock_entry_type": "Material Issue",  # or "Material Issue" depending on your use case
		# 	"items": [
		# 		{
		# 			"item_code": i.item_code,
		# 			"s_warehouse":"Site Warehouse - MS",
		# 			"t_warehouse": "Stores - MS",
		# 			"qty": i.output_qty,  # Quantity to be added or subtracted
		# 		}
		# 	]
		# }

		# 	stock_entry_data_receipt = {
		# 	"doctype": "Stock Entry",
		# 	"company": "",
		# 	"posting_date": "2023-07-12",
		# 	"stock_entry_type": "Material Receipt",  # or "Material Issue" depending on your use case
		# 	"items": [
		# 		{
		# 			"item_code": i.item_code,
		# 			"s_warehouse":"Stores - MS",
		# 			"t_warehouse": "Site Warehouse - MS",
		# 			"qty": i.output_qty,  # Quantity to be added or subtracted
		# 		}
		# 	]
		# }



		 # Create a new Stock Entry document
		# stock_entry = frappe.new_doc("Stock Entry")
		
		# # Set the relevant fields from the Sales Order to the Stock Entry
		# # stock_entry.sales_order = self.name
		# stock_entry.stock_entry_type="Material Receipt"
		# stock_entry.posting_date = self.posting_date
		# # Set other required fields as needed
		
		# # Iterate over the child item table of the Sales Order
		# for item in self.the_bloc_table_material_transfer:
		# 	# Create a new Stock Entry Detail document (child table of Stock Entry)
		# 	stock_entry_item = stock_entry.append("items")
			
		# 	# Set the relevant fields from the Sales Order item to the Stock Entry item
		# 	stock_entry_item.item_code = item.item_code
		# 	stock_entry_item.qty = item.output_qty
		# 	stock_entry_item.s_warehouse = "Stores - MS"
		# 	stock_entry_item.t_warehouse = "Site Warehouse - MS"

			
			# Set other required fields as needed
		

		# stock_entry = frappe.new_doc("Stock Entry")
		
		# # Set the relevant fields from the Sales Order to the Stock Entry
		# # stock_entry.sales_order = self.name
		# stock_entry.stock_entry_type="Material Receipt"
		# stock_entry.posting_date = self.posting_date
		# # Set other required fields as needed
		
		# # Iterate over the child item table of the Sales Order
		# for item in self.the_bloc_table_material_transfer:
		# 	# Create a new Stock Entry Detail document (child table of Stock Entry)
		# 	stock_entry_item = stock_entry.append("items")
			
		# 	# Set the relevant fields from the Sales Order item to the Stock Entry item
		# 	stock_entry_item.item_code = item.item_code
		# 	stock_entry_item.qty = item.output_qty
		# 	stock_entry_item.s_warehouse = "Stores - MS"
		# 	stock_entry_item.t_warehouse = "Site Warehouse - MS"

		# Save the Stock Entry document
		# stock_entry.insert()
		# frappe.db.commit()



			# frappe.new_doc("Stock Entry",stock_entry_data_issue)
			# frappe.new_doc("StocK Entry",stock_entry_data_receipt)
			# frappe.db.save()
			# frappe.db.commit()
	

