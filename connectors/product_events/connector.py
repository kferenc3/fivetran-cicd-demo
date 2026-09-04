from fivetran_connector_sdk import Connector
from fivetran_connector_sdk import Logging as log
from fivetran_connector_sdk import Operations as op


EVENTS = [
    {
        "event_id": "EVT-1003",
        "user_id": "USER-002",
        "event_name": "dashboard_opened",
        "occurred_at": "2026-09-01T10:15:00Z",
    },
    {
        "event_id": "EVT-1001",
        "user_id": "USER-001",
        "event_name": "application_opened",
        "occurred_at": "2026-09-01T09:00:00Z",
    },
    {
        "event_id": "EVT-1002",
        "user_id": "USER-001",
        "event_name": "report_viewed",
        "occurred_at": "2026-09-01T09:05:00Z",
    },
]


def schema(configuration: dict):
    return [
        {
            "table": "events",
            "primary_key": ["event_id"],
        }
    ]


def update(configuration: dict, state: dict):
    log.info("Producing dummy product events")

    for event in EVENTS:
        yield op.upsert(table="events", data=event)

    yield op.checkpoint(state={"processed_records": len(EVENTS)})


connector = Connector(update=update, schema=schema)