import uuid
from datetime import datetime


def create_event(
    visitor_id,
    event_type,
    zone_id=None,
    dwell_ms=0
):

    return {
        "event_id": str(uuid.uuid4()),
        "store_id": "STORE_BLR_002",
        "camera_id": "CAM_ENTRY_01",
        "visitor_id": visitor_id,
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        "zone_id": zone_id,
        "dwell_ms": dwell_ms,
        "is_staff": False,
        "confidence": 0.90,
        "metadata": {}
    }