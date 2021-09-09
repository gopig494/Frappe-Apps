# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "employee_management"
app_title = "Employee Management"
app_publisher = "Gopi"
app_description = "This app is used to manage the dta of employees"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "App@gmail.com"
app_license = "MIT"

website_route_rules = [
    {"from_route": "/payment-report", "to_route": "paymentreport"},
    {"from_route": "/order-payment", "to_route": "paymentcards"},
    {"from_route": "/payment", "to_route": "temp"},
    # {"from_route": "/orderss", "to_route": "ord"}

]

# web_include_css = "/assets/employee_management/js/order.css"
# abc = 'i am hoooks'
# app_include_js = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"
# web_include_js = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# web_include_js = "/assets/employee_management/js/register.js"
app_include_js = [  "/assets/employee_management/js/product_assessment_test.js",
					"/assets/employee_management/js/produc_varient_new.js",
                    "/assets/employee_management/js/detail_display.js",
                    "/assets/employee_management/js/product.js"
                  ]
# app_include_js = "/assets/employee_management/js/frappe-datatable.min.js"
# app_include_js = "/assets/employee_management/js/product_assessment_test.js"
# app_include_css = "https://unpkg.com/frappe-datatable/dist/frappe-datatable.min.css"
#app_include_js = "https://unpkg.com/frappe-datatable/dist/frappe-datatable.min.js"
# app_include_js ="https://unpkg.com/sortablejs@1.7.0/Sortable.min.js"
# include js, css files in header of web template
# web_include_css = "https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"
# web_include_js = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"
# web_include_js ="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"
# include js in page
# page_js = {"sam" : ""}

# include js in doctype views
# doctype_js = {"Product values": "public/js/register.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "employee_management.utils.get_home_page"

# Generators
# ----------


# automatically create page for each record of this doctype
website_generators = ["Orderss"]

# Installation
# ------------

# before_install = "employee_management.install.before_install"
# after_install = "employee_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "employee_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }

# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events
# doc_events = {
# "Customers": {
#     	"validate": "employee_management.employee_management.sam.customer_validate",
# 	},

# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }
#
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"employee_management.tasks.all"
# 	],
# 	"daily": [
# 		"employee_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"employee_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"employee_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"employee_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "employee_management.install.before_tests"

# Overriding Methods
# ------------------------------

# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "employee_management.event.get_events"
# }

# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "employee_management.task.get_dashboard_data"
# }
fixtures = ['Valiant']