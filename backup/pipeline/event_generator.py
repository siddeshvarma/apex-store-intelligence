import json
import uuid
from datetime import datetime


class EventGenerator:

    def __init__(self):

        self.previous_positions = {}

        self.generated_events = []

    def emit_entry(self, visitor_id):

        event = {
            "event_id": str(uuid.uuid4()),
            "store_id": "STORE_BLR_002",
            "camera_id": "CAM_5",
            "visitor_id": f"VIS_{visitor_id}",
            "event_type": "ENTRY",
            "timestamp": datetime.utcnow().isoformat(),
            "zone_id": None,
            "dwell_ms": 0,
            "is_staff": False,
            "confidence": 0.9,
            "metadata": {}
        }

        self.generated_events.append(event)

        print(
            f"ENTRY -> VIS_{visitor_id}"
        )

    def save(self):

        with open(
            "data/events_from_video.json",
            "w"
        ) as f:

            json.dump(
                self.generated_events,
                f,
                indent=2
            )