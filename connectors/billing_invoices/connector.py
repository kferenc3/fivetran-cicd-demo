from fivetran_connector_sdk import Connector
from fivetran_connector_sdk import Logging as log
from fivetran_connector_sdk import Operations as op


INVOICES = [
    {
        "invoice_id": "INV-1001",
        "customer_id": "CUST-001",
        "amount": 125.50,
        "currency": "USD",
        "status": "paid",
    },
    {
        "invoice_id": "INV-1002",
        "customer_id": "CUST-002",
        "amount": 89.99,
        "currency": "USD",
        "status": "open",
    },
]


def schema(configuration: dict):
    return [
        {
            "table": "invoices",
            "primary_key": ["invoice_id"],
        }
    ]


def update(configuration: dict, state: dict):
    log.info("Producing dummy invoice records")

    for invoice in INVOICES:
        yield op.upsert(table="invoices", data=invoice)

    yield op.checkpoint(state={"processed_records": len(INVOICES)})


connector = Connector(update=update, schema=schema)