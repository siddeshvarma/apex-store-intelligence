from sqlalchemy.orm import Session
from app.models import EventTable


def get_anomalies(db: Session, store_id: str):

    events = (
        db.query(EventTable)
        .filter(EventTable.store_id == store_id)
        .all()
    )

    anomalies = []

    queue_count = len(
        [
            e for e in events
            if e.event_type == "BILLING_QUEUE_JOIN"
        ]
    )

    if queue_count > 10:
        anomalies.append(
            {
                "type": "QUEUE_SPIKE",
                "severity": "WARN",
                "suggested_action":
                "Open another billing counter"
            }
        )

    if len(events) == 0:
        anomalies.append(
            {
                "type": "DEAD_STORE",
                "severity": "INFO",
                "suggested_action":
                "Verify camera feed"
            }
        )

    return anomalies