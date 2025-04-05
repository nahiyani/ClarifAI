import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects_in_video(video_path, frame_skip=30):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    detections_summary = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_skip == 0:
            results = model(frame)
            labels = results[0].names
            detected = [labels[int(cls)] for cls in results[0].boxes.cls]
            detections_summary.append((frame_count, detected))

        frame_count += 1

    cap.release()
    return detections_summary
