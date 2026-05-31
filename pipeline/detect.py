import json

from tracker import SimpleTracker
from emit import create_event


tracker = SimpleTracker()

events = []

visitor = tracker.new_visitor()

events.append(
    create_event(
        visitor,
        "ENTRY"
    )
)

events.append(
    create_event(
        visitor,
        "ZONE_ENTER",
        "SKINCARE"
    )
)

events.append(
    create_event(
        visitor,
        "ZONE_DWELL",
        "SKINCARE",
        30000
    )
)

events.append(
    create_event(
        visitor,
        "EXIT"
    )
)

with open(
    "data/generated_events.json",
    "w"
) as f:

    json.dump(
        events,
        f,
        indent=2
    )

print(
    f"Generated {len(events)} events"
)