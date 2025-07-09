import face_recognition
import cv2
import numpy as np
import os
import csv
from datetime import datetime

CurrentFolder = os.getcwd()
image = os.path.join(CurrentFolder, 'Nikesh.png')
image2 = os.path.join(CurrentFolder, 'Rohit.png')
image3 = os.path.join(CurrentFolder, 'Shiva.png')

video_capture = cv2.VideoCapture(0)

person1_name = "Nikesh"  # loading 1st person image
person1_image = face_recognition.load_image_file(image)
person1_face_encoding = face_recognition.face_encodings(person1_image)[0]

person2_name = "Rohit"  # loading 2nd person image
person2_image = face_recognition.load_image_file(image2)
person2_face_encoding = face_recognition.face_encodings(person2_image)[0]

person3_name = "Shiva"  # loading 1st person image
person3_image = face_recognition.load_image_file(image3)
person3_face_encoding = face_recognition.face_encodings(person3_image)[0]

known_face_encodings = [
    person1_face_encoding,
    person2_face_encoding,
    person3_face_encoding
]

known_face_names = [
    person1_name,
    person2_name,
    person3_name
]

face_locations = []
face_encodings = []
face_names = []
attendance_recorded = set()

csv_file = open('attendance.csv', mode='a', newline='')
fieldnames = ['Name', 'Date', 'Time']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
if os.stat('attendance.csv').st_size == 0:
    writer.writeheader()

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if name not in attendance_recorded and name != "Unknown":
            writer.writerow({'Name': name, 'Date': datetime.today().strftime('%Y-%m-%d'), 'Time': datetime.now().strftime('%H:%M:%S')})
            print("Attendance taken for", name)
            attendance_recorded.add(name)

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Data Saved.")
        break

csv_file.close()
video_capture.release()
cv2.destroyAllWindows()

