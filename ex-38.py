import cv2

# Load the pre-trained face detector model from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load an image from file or capture from a camera
# For example, to capture from the camera, you can use cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()

# Load an image from file
image_path ='C:/Users/pradeep bhonasu/OneDrive/Pictures/Saved Pictures/Alone-Boys-Whatsapp-DP-Wallpaper-Free-Download.jpg'
frame = cv2.imread(image_path)

# Convert the image to grayscale for face detection
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Perform face detection
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the result
cv2.imshow('Face Detection', frame)

# Wait for a key event and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
