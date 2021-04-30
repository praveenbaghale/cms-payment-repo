from frappe import _


def get_data():
    def make_item(type, name, label, is_query_report=None):
        return {
            "type": type,
            "name": name,
            "label": _(label),
            "is_query_report": is_query_report,
        }

    def make_section(label, items):
        return {"label": _(label), "items": items}

    return [
        make_section(
            "Setup",
            [
                make_item("doctype", "AFS Payment Settings", "AFS Payment Settings"),
            ],
        ),
    ]