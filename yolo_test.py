from ultralytics import YOLO
import cv2

# Load YOLO Model
model = YOLO("yolov8n.pt")

# Dangerous Objects
DANGER_OBJECTS = [
    "knife",
    "scissors",
    "baseball bat"
]

def detect_objects(frame):

    results = model(frame)

    annotated_frame = results[0].plot()

    # Check detected objects
    for box in results[0].boxes:

        cls = int(box.cls[0])
        label = model.names[cls]

        if label in DANGER_OBJECTS:

            print("🚨 DANGER DETECTED :", label)

            cv2.putText(
                annotated_frame,
                "DANGER DETECTED!",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                3
            )

    return annotated_frame