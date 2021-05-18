FROM frappe/erpnext-worker:develop

COPY . /home/frappe/frappe-bench/apps/fast_frappe

USER root

RUN /home/frappe/frappe-bench/env/bin/pip install -e /home/frappe/frappe-bench/apps/fast_frappe && \
    chown -R frappe:frappe /home/frappe/frappe-bench

USER frappe

CMD ["/home/frappe/frappe-bench/env/bin/uvicorn", "fast_frappe.main:app", "--port 3000", "--host 0.0.0.0"]

EXPOSE 3000
