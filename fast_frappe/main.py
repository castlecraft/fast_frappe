import frappe
from typing import Optional

from fastapi import FastAPI
from fast_frappe.ctrl import init_frappe, destroy_frappe

app = FastAPI()


@app.get("/")
def read_root():
    init_frappe()
    available_doctypes = frappe.get_list("DocType")
    settings = frappe.get_single("System Settings")
    destroy_frappe()
    return {
        "available_doctypes": available_doctypes,
        "settings": settings.as_dict(),
    }
