from sqlalchemy.orm import Session

from app.models import EventTable
from app.models import EventSchema


def save_event(db: Session, event: EventSchema):

    existing = (
        db.query(EventTable)
        .filter(EventTable.event_id == event.event_id)
        .first()
    )

    if existing:
        return False

    row = EventTable(
        event_id=event.event_id,
        store_id=event.store_id,
        camera_id=event.camera_id,
        visitor_id=event.visitor_id,
        event_type=event.event_type,
        timestamp=event.timestamp,
        zone_id=event.zone_id,
        dwell_ms=event.dwell_ms,
        is_staff=event.is_staff,
        confidence=event.confidence,
        metadata_json=event.metadata
    )

    db.add(row)
    db.commit()

    return True