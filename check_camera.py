import cv2

for i in range(5):

    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)

    if cap.isOpened():
        print("Camera mil gaya index:", i)
        cap.release()

    else:
        print("Camera nahi mila index:", i)