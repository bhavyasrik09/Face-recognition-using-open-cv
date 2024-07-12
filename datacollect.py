import cv2
import os

# Print OpenCV version
print("OpenCV Version:", cv2.__version__)

# Absolute path to the Haar cascade file
cascPath = "C:/Users/user/Desktop/all folders/Face Recognition/Face Recognition System/Face Recognition System/haarcascade_frontalface_default.xml"

# Debugging: Check if the file exists and can be opened
if not os.path.isfile(cascPath):
    print(f"Error: File not found at {cascPath}")
else:
    print(f"File found at {cascPath}")

try:
    with open(cascPath, 'r') as file:
        print("File opened successfully")
except Exception as e:
    print(f"Error opening file: {e}")

# Load the Haar cascade file
faceCascade = cv2.CascadeClassifier(cascPath)

# Debugging: Check if the cascade was loaded successfully
if faceCascade.empty():
    print(f"Failed to load cascade classifier from {cascPath}")
else:
    print("Cascade classifier loaded successfully")

# Example usage of faceCascade to ensure it works
try:
    # Load a test image (you can replace this with the actual path to a test image)
    test_image_path = "C:/Users/user/Desktop/all folders/Face Recognition/Face Recognition System/Face Recognition System/test.jpg"
    if not os.path.isfile(test_image_path):
        print(f"Test image not found at {test_image_path}")
    else:
        image = cv2.imread(test_image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = faceCascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30), 
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        print(f"Detected {len(faces)} faces")
except Exception as e:
    print(f"Error during face detection: {e}")

# Face detection from webcam and saving images
video = cv2.VideoCapture(0)  # Open webcam
count = 0

nameID = str(input("Enter Your Name: ")).lower()
path = 'images/' + nameID

isExist = os.path.exists(path)

if isExist:
    print("Name Already Taken")
    nameID = str(input("Enter Your Name Again: "))
else:
    os.makedirs(path)

while True:
    ret, frame = video.read()
    if not ret:
        break
    
    # Perform face detection using faceCascade
    faces = faceCascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)
    
    for x, y, w, h in faces:
        count = count + 1
        img_name = os.path.join(path, f"{count}.jpg")
        print("Creating Images........." + img_name)
        cv2.imwrite(img_name, frame[y:y+h, x:x+w])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    
    cv2.imshow("WindowFrame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if count > 500:  # Limit to 500 images
        break

video.release()
cv2.destroyAllWindows()
