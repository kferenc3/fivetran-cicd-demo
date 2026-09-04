from fivetran_connector_sdk import Connector
from fivetran_connector_sdk import Logging as log
from fivetran_connector_sdk import Operations as op


TICKETS = [
    {
        "ticket_id": "TICKET-1001",
        "subject": "Unable to sign in",
        "priority": "high",
        "status": "open",
        "updated_at": "2026-09-01T10:00:00Z",
    },
    {
        "ticket_id": "TICKET-1002",
        "subject": "Feature request",
        "priority": "low",
        "status": "closed",
        "updated_at": "2026-09-01T11:30:00Z",
    },
]


def schema(configuration: dict):
    return [
        {
            "table": "tickets",
            "primary_key": ["ticket_id"],
        }
    ]


def update(configuration: dict, state: dict):
    log.info("Producing dummy support tickets")

    for ticket in TICKETS:
        yield op.upsert(table="tickets", data=ticket)

    yield op.checkpoint(state={"processed_records": len(TICKETS)})


connector = Connector(update=update, schema=schema)