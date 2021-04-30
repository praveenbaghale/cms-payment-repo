# -*- coding: utf-8 -*-
# Copyright (c) 2020, Valiantsystems and contributors
# For license information, please see license.txt

""""
### Redirect for payment

Example:

	payment_details = {
		"amount": 600,
		"title": "Payment for bill : 111",
		"description": "payment via cart",
		"reference_doctype": "Payment Request",
		"reference_docname": "PR0001",
		"payer_email": "NuranVerkleij@example.com",
		"payer_name": "Nuran Verkleij",
		"order_id": "111",
		"currency": "BHD",
		"payment_gateway": "AFS Payment",
	}

	# Redirect the user to this url
	url = controller().get_payment_url(**payment_details)
"""

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.integrations.utils import (
    create_request_log,
    make_post_request,
    create_payment_gateway,
)
from frappe.utils import get_url, call_hook_method, cint, get_datetime


class AFSSettings(Document):
    def validate(self):
        create_payment_gateway("AFS Payment")
        call_hook_method("payment_gateway_enabled", gateway="AFS Payment")

    def get_payment_url(self, **kwargs):
        integration_request = create_request_log(kwargs, "Host", "AFS Payment")
        return get_url(
            "./afs_payment_checkout?payment_request={0}".format(
                integration_request.name
            )
        )
