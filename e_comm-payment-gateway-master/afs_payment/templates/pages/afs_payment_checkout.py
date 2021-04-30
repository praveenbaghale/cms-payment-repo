from __future__ import unicode_literals
import frappe
from frappe import _
import requests
import json


def get_context(context):
    payment_request_id = frappe.form_dict.token
    if payment_request_id:
        query_1 = '''
            SELECT 
                name, 
                reference_doctype,
                reference_docname,
                status 
            FROM `tabIntegration Request` 
            WHERE name="{id}"
        '''.format(id=payment_request_id)
        payment_request = frappe.db.sql(
            """{query_1}""".format(query_1=query_1), as_dict=1
        )
        if payment_request:
            if payment_request[0].status == "Queued":
                afs_settings = frappe.get_single("AFS Payment Settings")
                if afs_settings:
                    context.merchant_id = afs_settings.merchant_id
                    context.merchant_name = afs_settings.merchant_name
                    if afs_settings.test_mode == 1:
                        context.merchant_id = "TEST" + afs_settings.merchant_id
                order_info = frappe.get_doc(
                    payment_request[0].reference_doctype,
                    payment_request[0].reference_docname,
                )
                context.order_id = order_info.name
                context.order_total = order_info.grand_total
                context.currency = order_info.currency
                url = (
                    "https://afs.gateway.mastercard.com/api/rest/version/56/merchant/"
                    + context.merchant_id
                    + "/session"
                )
                payload = (
                    '{\r\n "apiOperation": "CREATE_CHECKOUT_SESSION",\r\n"interaction": {"operation":"PURCHASE"},\r\n"order":{\r\n"amount":'
                    + ("%.2f" % order_info.grand_total)
                    + ',\r\n"currency":"BHD",\r\n "id":"ORDER_ID_'
                    + order_info.name
                    + '"\r\n}\r\n}'
                )
                headers = {
                    "authorization": "Basic " + afs_settings.authentication_key,
                    "content-type": "application/json",
                }
                response = requests.request("POST", url, data=payload, headers=headers)
                r = json.loads(response.text)
                session = r.get("session")
                context.session_id = session.get("id")
                context.payment_request_id = payment_request_id
                if order_info:
                    context.company_name = order_info.company
