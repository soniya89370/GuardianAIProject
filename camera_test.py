import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera open nahi ho raha")
else:
    print("Camera successfully open!")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Frame nahi mil raha")
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()