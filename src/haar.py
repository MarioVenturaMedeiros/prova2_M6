import numpy as np
import cv2
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_cascade2 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture("../video/la_cabra.mp4")

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to grayscale (required for face detection)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1   , minNeighbors=15, minSize=(50, 50))
    faces2 = face_cascade2.detectMultiScale(gray_frame, scaleFactor=1.1   , minNeighbors=15, minSize=(50, 50))

    # Blur the detected faces and keep the rest of the frame as it is
    for (x, y, w, h) in faces:
        # Get the region of interest (ROI) where the face is located
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    for (x, y, w, h) in faces2:
        # Get the region of interest (ROI) where the face is located
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Display the frame
    cv2.imshow('Live Video Stream with Face Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()