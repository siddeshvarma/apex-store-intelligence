from ultralytics import YOLO
import cv2

VIDEO_PATH = r"data\CAM 5.mp4"

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(VIDEO_PATH)

seen_ids = set()
customer_count = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.resize(frame, (960, 540))

    results = model.track(
        frame,
        persist=True,
        classes=[0],   # person only
        verbose=False
    )

    if len(results) > 0 and results[0].boxes.id is not None:

        boxes = results[0].boxes
        track_ids = boxes.id.int().cpu().tolist()

        for box, track_id in zip(boxes.xyxy, track_ids):

            x1, y1, x2, y2 = map(int, box)

            if track_id not in seen_ids:
                seen_ids.add(track_id)
                customer_count += 1

                print(
                    f"New Visitor: VIS_{track_id} | Total Customers={customer_count}"
                )

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"VIS_{track_id}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 0, 0),
                2
            )

    cv2.putText(
        frame,
        f"Unique Visitors: {customer_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow("YOLO Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print(f"Final Visitor Count: {customer_count}")