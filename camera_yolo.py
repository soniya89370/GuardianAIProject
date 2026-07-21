import cv2
import csv
from datetime import datetime
from ultralytics import YOLO
import os
import pyttsx3
import time


# ---------------- YOLO MODEL ----------------

model = YOLO("yolov8n.pt")


# ---------------- VOICE ALERT ----------------

engine = pyttsx3.init()

engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)



# ---------------- DANGEROUS OBJECTS ----------------

DANGER_OBJECTS = [
    "knife",
    "scissors",
    "baseball bat",
    "gun"
]


last_alert = ""
last_time = 0



# ---------------- HISTORY ----------------

os.makedirs("data", exist_ok=True)

history_file = "data/history.csv"


if not os.path.exists(history_file):

    with open(history_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Date",
                "Time",
                "Object"
            ]
        )



def save_history(object_name):

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time_now = now.strftime("%I:%M %p")


    with open(history_file,"a",newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                date,
                time_now,
                object_name
            ]
        )



# ---------------- CAMERA ----------------


cap = cv2.VideoCapture(0)


if not cap.isOpened():

    cap = cv2.VideoCapture(1)



if not cap.isOpened():

    print("Camera open nahi ho raha")
    exit()



print("GuardianAI Camera Started")



# ---------------- MAIN LOOP ----------------


while True:


    ret, frame = cap.read()


    if not ret:

        print("Frame nahi mil raha")
        break



    results = model(frame)



    for box in results[0].boxes:


        confidence = float(box.conf[0])


        if confidence < 0.50:

            continue



        class_id = int(box.cls[0])


        object_name = model.names[class_id]



        if object_name in DANGER_OBJECTS:


            # Bounding Box

            x1,y1,x2,y2 = map(
                int,
                box.xyxy[0]
            )


            cv2.rectangle(
                frame,
                (x1,y1),
                (x2,y2),
                (0,0,255),
                3
            )



            cv2.putText(
                frame,
                "DANGER: "+object_name,
                (x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                3
            )



            print(
                "WARNING!",
                object_name,
                "Detected"
            )



            # Voice Alert after 5 seconds gap

            current_time = time.time()


            if (
                last_alert != object_name
                or current_time-last_time > 5
            ):


                message = (
                    "Warning! "
                    + object_name
                    + " detected"
                )


                engine.say(message)

                engine.runAndWait()



                save_history(object_name)



                last_alert = object_name

                last_time = current_time




    cv2.imshow(
        "GuardianAI - Smart Safety Camera",
        frame
    )



    # ESC button

    if cv2.waitKey(1)==27:

        break




cap.release()

cv2.destroyAllWindows()