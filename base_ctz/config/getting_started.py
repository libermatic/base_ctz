# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Data Import and Settings"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Libermatic Settings",
                    "label": _("Libermatic Settings"),
                    "description": _("Run setup scripts"),
                    "settings": 1,
                },
            ],
        },
    ]
