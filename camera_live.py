import cv2
from yolo_test import detect_objects


def start_camera():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Camera open nahi ho raha.")
        return

    while True:

        ret, frame = cap.read()

        if not ret:
            print("❌ Camera frame nahi mil raha.")
            break

        # YOLO Detection
        frame = detect_objects(frame)

        # Show Live Camera
        cv2.imshow("GuardianAI - Live Detection", frame)

        # Press Q to Exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# Run only when this file is executed directly
if __name__ == "__main__":
    start_camera()