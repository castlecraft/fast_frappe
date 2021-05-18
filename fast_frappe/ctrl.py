import os

import frappe


def init_frappe():
    site = os.environ.get("SITE_NAME", "test.localhost")
    frappe.init(site=site)
    frappe.connect()


def destroy_frappe():
    frappe.destroy()
