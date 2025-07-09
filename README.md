# 👤 Face Recognition Attendance System

A Python-based real-time face recognition system using a webcam to automate attendance tracking and store it in a CSV file.

---

## 📌 Features

- Capture and save face images via webcam
- Real-time face recognition using `face_recognition` and `OpenCV`
- Automatically records attendance (Name, Date, Time)
- Stores attendance in `attendance.csv`
- Simple CLI interface with live video feed

---

## 📁 Project Structure

.
├── capture_image.py # Script to capture a single face image
├── checking.py # Face recognition + attendance tracking
├── attendance.csv #  Sample CSV attendance log
├── requirements.txt # Python dependencies
├── README.md # You're reading this!
└── Data #saved images are present here
