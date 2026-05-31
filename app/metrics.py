from sqlalchemy.orm import Session
from app.models import EventTable


def calculate_metrics(db: Session, store_id: str):

    events = (
        db.query(EventTable)
        .filter(EventTable.store_id == store_id)
        .all()
    )

    visitors = set()

    dwell_total = 0
    dwell_count = 0

    queue_events = 0

    for event in events:

        if event.is_staff:
            continue

        visitors.add(event.visitor_id)

        if event.event_type == "ZONE_DWELL":
            dwell_total += event.dwell_ms
            dwell_count += 1

        if event.event_type == "BILLING_QUEUE_JOIN":
            queue_events += 1

    avg_dwell = 0

    if dwell_count > 0:
        avg_dwell = dwell_total / dwell_count

    return {
        "store_id": store_id,
        "unique_visitors": len(visitors),
        "avg_dwell_ms": avg_dwell,
        "queue_depth": queue_events,
        "conversion_rate": 0
    }