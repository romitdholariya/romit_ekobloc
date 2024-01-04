# def get_permission_query_conditions(user):
# 	if not user:
# 		user = frappe.session.user
# 	return """(`tabEvent`.`event_type`='Public' or `tabEvent`.`owner`={user})""".format(
# 		user=frappe.db.escape(user),
# 	)
import frappe
import json


@ frappe.whitelist()
def get_permission_query_conditions_customer(user):
    if not user:
        user = frappe.session.user
    # if user != "Administrator":
    user_name = frappe.db.get_value("User",user,"full_name")
    user_role = get_user_roles(user)
    if user_name != "Administrator" and "Customer User" in user_role :
        return """(`tabCustomer`.`customer_name`={user_name})""".format(
            user_name=frappe.db.escape(user_name),
    )


@ frappe.whitelist()
def get_permission_query_conditions_material(user):
    if not user:
        user = frappe.session.user
    # if user != "Administrator":
    user_name = frappe.db.get_value("User",user,"full_name")
    user_role = get_user_roles(user)
    if user_name != "Administrator" and "Customer User" in user_role :
        return """(`tabRequest For Material`.`owner`={user})""".format(
            user=frappe.db.escape(user),
    )

@ frappe.whitelist()
def get_permission_query_conditions_item(user):
    if not user:
        user = frappe.session.user
    user_name = frappe.db.get_value("User",user,"full_name")
    user_role = get_user_roles(user)
    if user_name != "Administrator" and "Customer User" in user_role :
        return """(`tabItem`.`item_group`='11 FG')"""
    else:
        return ""

@ frappe.whitelist()
def get_permission_query_conditions_address(user):
    if not user:
        user = frappe.session.user
    # if user != "Administrator":
    user_name = frappe.db.get_value("User",user,"full_name")
    user_role = get_user_roles(user)
    if user_name != "Administrator" and "Customer User" in user_role :
        return """(`tabAddress`.`name` IN (SELECT `parent` FROM `tabDynamic Link` WHERE  `link_name`={user_name}))""".format(
    user_name=frappe.db.escape(user_name),
)
    #     return """(`tabAddress`.`links` where (`tabDynamic Link`.`link_name`)={user_name})""".format(
    #         user_name=frappe.db.escape(user_name),
    # )

# def get_permission_query_conditions_item(user):
#     if not user:
#         user = frappe.session.user
#         # if user != "Administrator":

#         return """(`tabItem`.`item_group`='Products')"""
    # if not user:
    #     user = frappe.session.user
    # user_name = frappe.db.get_value("User",user,"full_name")
    # return """(`tabItem`.`item_group`="Products")""".format(
    #     user_name=frappe.db.escape(user_name),
    # )


@frappe.whitelist()
def get_user_roles(user):
    # Get the currently logged-in user
    current_user = frappe.session.user

    # Get the roles of the current user
    user_roles = frappe.get_roles(current_user)

    return user_roles


@frappe.whitelist(allow_guest=True)
def get_material_list():
    doc = frappe.db.get_list("Item")
    return doc

@frappe.whitelist()
def get_customer_list(allow_guest=False,methods="GET"):
    doc = frappe.db.get_list("Customer")
    return doc



@frappe.whitelist(allow_guest=True)
def login(usr, pwd):
    try:
        login_manager=frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response["message"]={
            "success_key":0,
            "message":"Authentication Error!"
        }
        
        return
        
    api_generate = generate_keys(frappe.session.user)
    user = frappe.get_doc("User",frappe.session.user)

    frappe.response["message"]={
        "success_key":1,
        "message":"Authentication Success",
        "sid":frappe.session.sid,
        "api_key":user.api_key,
        "api_secret":api_generate,
        "username":user.username,
        "email":user.email
    }




def generate_keys(user):
    user_details = frappe.get_doc("User",user)
    api_secret = frappe.generate_hash(length=15)

    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key

    user_details.api_secret = api_secret
    user_details.save()

    return api_secret




@frappe.whitelist(methods="POST")
def create_material_request(args):
    input =json.loads(args)
    new_doc = frappe.new_doc("Request For Material")
    for key in input:
        new_doc.set(key,input[key])
    
    new_doc.save()
    frappe.db.commit()

    frappe.clear_messages()
    return new_doc




@frappe.whitelist(methods="POST")
def create_or_edit_material_request(args, doc_name=None):
    input_data = json.loads(args)

    if doc_name:
        existing_doc = frappe.get_doc("Request For Material", doc_name)
        for key in input_data:
            existing_doc.set(key, input_data[key])
        existing_doc.save()
        frappe.db.commit()
        frappe.clear_messages()
        return existing_doc
    else:
        new_doc = frappe.new_doc("Request For Material")
        for key in input_data:
            new_doc.set(key, input_data[key])
        new_doc.save()
        frappe.db.commit()
        frappe.clear_messages()
        return new_doc

# @frappe.whitelist()
# def get_new_order():
#     doc = frappe.get_doc("Request For Material")
#     doc.transaction_date
#     doc.required_by
#     doc.request_no
#     doc.address
#     doc.delivery_address
#     doc.billing_address
#     doc.customer
#     for i in doc.items:


# import frappe

# @frappe.whitelist()
# def get_new_order(args):
#     response = {}

#     doc = frappe.get_doc("Request For Material")
#     response["transaction_date"] = doc.transaction_date
#     response["required_by"] = doc.required_by
#     response["request_no"] = doc.request_no
#     response["address"] = doc.address
#     response["delivery_address"] = doc.delivery_address
#     response["billing_address"] = doc.billing_address
#     response["customer"] = doc.customer

#     response["items"] = []
#     for item in doc.items:
#         item_data = {
#             "item_code": item.item_code,
#             "quantity": item.quantity,
#             "uom":item.uom
#             # Add other item properties as needed
#         }
#         response["items"].append(item_data)

#     return response



# @frappe.whitelist()
# def create_new_order(args):
#     doc = frappe.new_doc("")

@frappe.whitelist()
def create_or_edit_request_for_material(request_data):
    try:
        if "name" in request_data:
            # If "name" is present, fetch the existing document
            doc = frappe.get_doc("Request For Material", request_data["name"])
        else:
            # If "name" is not present, create a new document
            doc = frappe.new_doc("Request For Material")

        # Set values for the document fields
        doc.transaction_date = request_data["transaction_date"]
        doc.required_by = request_data["required_by"]
        doc.address = request_data["address"]
        doc.delivery_address = request_data["delivery_address"]
        doc.billing_address = request_data["billing_address"]
        doc.customer = request_data["customer"]

        # Clear existing items to avoid duplicates during edit
        doc.set("items", [])

        # Add items to the document
        for item_data in request_data["items"]:
            item = doc.append("items", {})
            item.item_code = item_data["item_code"]
            item.quantity = item_data["quantity"]
            # Add other item properties as needed

        doc.save()

        return {
            "status": "success",
            "message": "Request For Material saved successfully",
            "docname": doc.name
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }



