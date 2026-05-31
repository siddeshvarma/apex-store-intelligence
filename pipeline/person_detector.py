from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

VIDEO_PATH = r"data\CAM 5.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

frame_count = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame_count += 1

    # Process every 5th frame for speed
    if frame_count % 5 != 0:
        continue

    # Resize frame
    frame = cv2.resize(
        frame,
        (960, 540)
    )

    # Run YOLO detection
    results = model(
        frame,
        verbose=False
    )

    person_count = 0

    for result in results:

        boxes = result.boxes

        for box in boxes:

            cls = int(box.cls[0])

            # COCO class 0 = person
            if cls != 0:
                continue

            person_count += 1

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            confidence = float(box.conf[0])

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Person {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

    cv2.putText(
        frame,
        f"People: {person_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow(
        "YOLO Person Detection",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()