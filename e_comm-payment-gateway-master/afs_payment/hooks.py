# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "afs_payment"
app_title = "AFS Payment"
app_publisher = "Valiantsystems"
app_description = "App for AFS Payment gateway integration"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@valiantsystems.com"
app_license = "Valiantsystems"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/afs_payment/css/afs_payment.css"
# app_include_js = "/assets/afs_payment/js/afs_payment.js"

# include js, css files in header of web template
# web_include_css = "/assets/afs_payment/css/afs_payment.css"
# web_include_js = "/assets/afs_payment/js/afs_payment.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "afs_payment.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "afs_payment.install.before_install"
# after_install = "afs_payment.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "afs_payment.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"afs_payment.tasks.all"
# 	],
# 	"daily": [
# 		"afs_payment.tasks.daily"
# 	],
# 	"hourly": [
# 		"afs_payment.tasks.hourly"
# 	],
# 	"weekly": [
# 		"afs_payment.tasks.weekly"
# 	]
# 	"monthly": [
# 		"afs_payment.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "afs_payment.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "afs_payment.event.get_events"
# }

