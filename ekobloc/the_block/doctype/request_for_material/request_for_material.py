# Copyright (c) 2023, Prashant Kamble and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from ekobloc.the_block.doc_events.permission import get_user_roles

class RequestForMaterial(Document):
	pass


	# def before_save(self):
	# 	user_name = frappe.session.user
	# 	user_full_name = frappe.db.get_value("User",user_name,"full_name")
	# 	doc = frappe.db.get_list("Customer",filters={'customer_name':user_full_name},pluck="name")[0]
	# 	c_name = frappe.db.get_value("Customer",doc,"customer_name")
	# 	self.customer = c_name






@frappe.whitelist()
def get_customer_name():
	# name = frappe.db.get_value("Customer",customer_name,"customer_name")
	# doc = frappe.db.get_list("Dynamic Link",filters={"link_doctype":"Customer","link_name":name},fields=["parent"],pluck="parent")
	# return doc

	user_name = frappe.session.user
	user_role = get_user_roles(user_name)
	if user_name != "Administrator" and "Customer User" in user_role:
		user_full_name = frappe.db.get_value("User",user_name,"full_name")
		doc = frappe.db.get_list("Customer",filters={'customer_name':user_full_name},pluck="name")[0]
		c_name = frappe.db.get_value("Customer",doc,"customer_name")
		return c_name
