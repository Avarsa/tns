from . import __version__ as app_version

app_name = "tns"
app_title = "The Narrative Scribe"
app_publisher = "The Narrative Scribe"
app_description = "A transformative, AI-powered tool built with the Frappe framework, The Narrative Scribe guides users through self-authoring exercises to foster personal growth. It leverages AI for sentiment analysis, providing insightful feedback on user narratives and fostering self-awareness and goal-setting."
app_email = "tech@narrativescribe.org"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tns/css/tns.css"
# app_include_js = "/assets/tns/js/tns.js"

# include js, css files in header of web template
# web_include_css = "/assets/tns/css/tns.css"
# web_include_js = "/assets/tns/js/tns.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tns/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "tns.utils.jinja_methods",
#	"filters": "tns.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "tns.install.before_install"
# after_install = "tns.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tns.uninstall.before_uninstall"
# after_uninstall = "tns.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tns.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"tns.tasks.all"
#	],
#	"daily": [
#		"tns.tasks.daily"
#	],
#	"hourly": [
#		"tns.tasks.hourly"
#	],
#	"weekly": [
#		"tns.tasks.weekly"
#	],
#	"monthly": [
#		"tns.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "tns.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "tns.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "tns.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tns.utils.before_request"]
# after_request = ["tns.utils.after_request"]

# Job Events
# ----------
# before_job = ["tns.utils.before_job"]
# after_job = ["tns.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"tns.auth.validate"
# ]
