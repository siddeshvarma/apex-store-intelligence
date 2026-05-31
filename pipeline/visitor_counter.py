from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

VIDEO_PATH = r"data\CAM 5.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

frame_count = 0

max_people = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame_count += 1

    if frame_count % 10 != 0:
        continue

    frame = cv2.resize(
        frame,
        (960, 540)
    )

    results = model(
        frame,
        verbose=False
    )

    people = 0

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            if cls == 0:
                people += 1

    max_people = max(
        max_people,
        people
    )

    print(
        f"Frame {frame_count}: {people} people"
    )

print(
    f"Max people detected: {max_people}"
)

cap.release()