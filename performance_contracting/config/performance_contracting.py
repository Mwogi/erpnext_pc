from __future__ import unicode_literals
from frappe import _


def get_data():
	pc_setup = {
		"label": _("PC Setup"),
		"icon": "octicon octicon-briefcase",
		"items": [
			{
				"name": "Activity Categories",
				"type": "doctype",
				"label": _("Activity Categories"),
				"description": _("Activity Categories")
			},
			{
				"name": "Indicators",
				"type": "doctype",
				"label": _("Indicators"),
				"description": _("Indicators")
			}
		]
	}

	return [
		pc_setup
	]
