import cv2
import os

VIDEO_PATH = r"data\CAM 5.mp4"

print("Current folder:", os.getcwd())
print("Video exists:", os.path.exists(VIDEO_PATH))

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Failed to open video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"FPS: {fps}")
print(f"Frames: {frame_count}")

success, frame = cap.read()

if success:
    print("First frame shape:", frame.shape)
else:
    print("Could not read first frame")

cap.release()