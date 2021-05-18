## Fast Frappe

FastAPI using Frappe Framework

Use example to build microservice or serverless function

### Installation

Install as python app in frappe-bench python `env`

```shell
cd ~/frappe-bench
git clone https://github.com/castlecraft/fast_frappe apps/fast_frappe
./env/bin/pip install -e apps/fast_frappe
```

### Serve

Using `uvicorn`

```shell
cd ~/frappe-bench
. ./env/bin/activate
cd frappe-bench/sites
SITE_NAME=function.local uvicorn fast_frappe.main:app --port 3000
```

### Check Response

```
curl -s http://localhost:3000 | jq .
```

### Description

The app consists of 2 files:

`main.py`:

```python
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
```

and `ctrl.py`:

```python
import os

import frappe


def init_frappe():
    site = os.environ.get("SITE_NAME", "test.localhost")
    frappe.init(site=site)
    frappe.connect()


def destroy_frappe():
    frappe.destroy()
```
### License

MIT