from ultralytics import YOLO
from tracker import CentroidTracker

import cv2

model = YOLO("yolov8n.pt")

tracker = CentroidTracker()

VIDEO_PATH = r"data\CAM 5.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

while True:

    success, frame = cap.read()

    if not success:
        break

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

    tracked = tracker.update(
        detections
    )

    for object_id, center in tracked.items():

        cx, cy = center

        cv2.circle(
            frame,
            (cx, cy),
            5,
            (0, 0, 255),
            -1
        )

        cv2.putText(
            frame,
            f"VIS_{object_id}",
            (cx, cy - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

    cv2.imshow(
        "Tracked Visitors",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()