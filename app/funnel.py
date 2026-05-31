from sqlalchemy.orm import Session
from app.models import EventTable


def calculate_funnel(db: Session, store_id: str):

    events = (
        db.query(EventTable)
        .filter(EventTable.store_id == store_id)
        .all()
    )

    visitors = {}

    for event in events:

        if event.is_staff:
            continue

        vid = event.visitor_id

        if vid not in visitors:
            visitors[vid] = {
                "entry": False,
                "zone": False,
                "billing": False
            }

        if event.event_type == "ENTRY":
            visitors[vid]["entry"] = True

        if event.event_type in [
            "ZONE_ENTER",
            "ZONE_DWELL"
        ]:
            visitors[vid]["zone"] = True

        if event.event_type == "BILLING_QUEUE_JOIN":
            visitors[vid]["billing"] = True

    entry_count = sum(v["entry"] for v in visitors.values())
    zone_count = sum(v["zone"] for v in visitors.values())
    billing_count = sum(v["billing"] for v in visitors.values())

    return {
        "entry": entry_count,
        "zone_visit": zone_count,
        "billing_queue": billing_count,
        "purchase": 0
    }