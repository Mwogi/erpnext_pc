# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "performance_contracting"
app_title = "Performance Contracting"
app_publisher = "Thomas Mwogi"
app_description = "Tracking performance contracts for the organization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "erp@mtrh.go.ke"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/performance_contracting/css/performance_contracting.css"
# app_include_js = "/assets/performance_contracting/js/performance_contracting.js"

# include js, css files in header of web template
# web_include_css = "/assets/performance_contracting/css/performance_contracting.css"
# web_include_js = "/assets/performance_contracting/js/performance_contracting.js"

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
# get_website_user_home_page = "performance_contracting.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "performance_contracting.install.before_install"
# after_install = "performance_contracting.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "performance_contracting.notifications.get_notification_config"

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
# 		"performance_contracting.tasks.all"
# 	],
# 	"daily": [
# 		"performance_contracting.tasks.daily"
# 	],
# 	"hourly": [
# 		"performance_contracting.tasks.hourly"
# 	],
# 	"weekly": [
# 		"performance_contracting.tasks.weekly"
# 	]
# 	"monthly": [
# 		"performance_contracting.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "performance_contracting.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "performance_contracting.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "performance_contracting.task.get_dashboard_data"
# }

