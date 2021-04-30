# -*- coding: utf-8 -*-
# Copyright (c) 2020, Valiantsystems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.integrations.utils import (
    create_request_log,
    make_post_request,
    create_payment_gateway,
)
from frappe.utils import get_url, call_hook_method, cint, get_datetime


class AFSPaymentSettings(Document):
    def validate(self):
        create_payment_gateway("AFS Payment")
        call_hook_method("payment_gateway_enabled", gateway="AFS Payment")

    def get_payment_url(self, **kwargs):
        integration_request = create_request_log(kwargs, "Host", "AFS Payment")
        return get_url(
            "./afs_payment_checkout?token={0}".format(integration_request.name)
        )
