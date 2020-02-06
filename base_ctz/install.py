# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _


@frappe.whitelist()
def setup_defaults():
    if "System Manager" not in frappe.get_roles():
        frappe.throw(_("Only allowed for System Managers"))
    _update_settings()
    frappe.db.set_value("Libermatic Settings", None, "setup_complete", 1)


def _update_settings():
    def update(doctype, params):
        doc = frappe.get_single(doctype)
        doc.update(params)
        doc.save(ignore_permissions=True)

    for args in settings().items():
        update(*args)


def settings():
    return {
        "Buying Settings": {"supp_master_name": "Naming Series"},
        "Selling Settings": {"cust_master_name": "Naming Series"},
        "Stock Settings": {"item_naming_by": "Naming Series"},
    }
