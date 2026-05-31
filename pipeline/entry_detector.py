from ultralytics import YOLO
from tracker import CentroidTracker
from event_generator import EventGenerator

import cv2

VIDEO_PATH = r"data\CAM 5.mp4"

ENTRY_LINE_Y = 270

model = YOLO("yolov8n.pt")

tracker = CentroidTracker()

events = EventGenerator()

seen_entries = set()

customer_count = 0

cap = cv2.VideoCapture(VIDEO_PATH)

frame_number = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame_number += 1

    # Skip frames for speed
    if frame_number % 3 != 0:
        continue

    frame = cv2.resize(
        frame,
        (960, 540)
    )

    results = model(
        frame,
        verbose=False
    )

    detections = []

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            if cls != 0:
                continue

            confidence = float(box.conf[0])

            if confidence < 0.60:
                continue

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            detections.append(
                (x1, y1, x2, y2)
            )

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

    tracked_objects = tracker.update(
        detections
    )

    cv2.line(
        frame,
        (0, ENTRY_LINE_Y),
        (960, ENTRY_LINE_Y),
        (0, 0, 255),
        3
    )

    for visitor_id, center in tracked_objects.items():

        cx, cy = center

        cv2.circle(
            frame,
            (cx, cy),
            5,
            (255, 0, 0),
            -1
        )

        cv2.putText(
            frame,
            f"VIS_{visitor_id}",
            (cx, cy - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

        if (
            cy > ENTRY_LINE_Y
            and visitor_id not in seen_entries
        ):

            seen_entries.add(
                visitor_id
            )

            customer_count += 1

            events.emit_entry(
                visitor_id
            )

            print(
                f"ENTRY -> VIS_{visitor_id}"
            )

            print(
                f"TOTAL CUSTOMERS: {customer_count}"
            )

    cv2.putText(
        frame,
        f"Customers: {customer_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow(
        "Store Entry Detection",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()

events.save()

cv2.destroyAllWindows()

print(
    f"Finished. Total Customers: {customer_count}"
)

print(
    f"Events Generated: {len(events.generated_events)}"
)