from sqlalchemy.orm import Session
from app.models import EventTable


def calculate_heatmap(db: Session, store_id: str):

    events = (
        db.query(EventTable)
        .filter(EventTable.store_id == store_id)
        .all()
    )

    zones = {}

    for event in events:

        if not event.zone_id:
            continue

        zone = event.zone_id

        if zone not in zones:
            zones[zone] = {
                "visits": 0,
                "dwell": 0
            }

        zones[zone]["visits"] += 1
        zones[zone]["dwell"] += event.dwell_ms

    return {
        "store_id": store_id,
        "zones": zones,
        "data_confidence": "LOW"
        if len(events) < 20
        else "HIGH"
    }