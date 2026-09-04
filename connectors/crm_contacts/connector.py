"""Dummy CRM connector that makes no external API calls."""

from fivetran_connector_sdk import Connector
from fivetran_connector_sdk import Logging as log
from fivetran_connector_sdk import Operations as op


CONTACTS = (
    {
        "contact_id": "contact_1001",
        "name": "Ada Lovelace",
        "email": "ada@example.test",
        "segment": "enterprise",
        "updated_at": "2026-01-15T09:00:00Z",
    },
    {
        "contact_id": "contact_1002",
        "name": "Grace Hopper",
        "email": "grace@example.test",
        "segment": "growth",
        "updated_at": "2026-01-15T09:05:00Z",
    },
)


def schema(configuration: dict):
    """Declare the tables produced by the connector."""
    del configuration

    return [
        {
            "table": "contacts",
            "primary_key": ["contact_id"],
        }
    ]


def update(configuration: dict, state: dict):
    """Emit deterministic demo records without contacting a source."""
    del configuration

    log.info("Emitting dummy CRM contacts")

    for contact in CONTACTS:
        op.upsert(
            table="contacts",
            data=contact,
        )

    op.checkpoint(
        {
            **state,
            "last_demo_batch": "2026-01-15T09:05:00Z",
        }
    )


connector = Connector(
    update=update,
    schema=schema,
)