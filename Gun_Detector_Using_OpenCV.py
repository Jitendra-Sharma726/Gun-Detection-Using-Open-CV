import cv2
import imutils

# Load the cascade classifier for gun detection
gun_cascade = cv2.CascadeClassifier('cascade.xml')  # Provide the path to your trained cascade XML file

# Initialize the camera
camera = cv2.VideoCapture(0)  # Use 0 for the default camera or specify the camera index

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    
    # Resize the frame
    frame = imutils.resize(frame, width=500)
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect guns in the grayscale frame
    guns = gun_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100))
    
    # Draw bounding boxes around the detected guns
    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Gun Detection', frame)
    
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
