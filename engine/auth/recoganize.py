from sys import flags
import time
import os
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    print("OpenCV not available due to NumPy compatibility issues")
    CV2_AVAILABLE = False
try:
    import pyautogui as p
except ImportError:
    print("PyAutoGUI not available")
    p = None


def AuthenticateFace():

    flag = ""
    if not CV2_AVAILABLE:
        print("OpenCV not available due to NumPy compatibility issues. Skipping face authentication.")
        return 1  # Skip face auth if OpenCV not available
    
    try:
        # Local Binary Patterns Histograms
        recognizer = cv2.face.LBPHFaceRecognizer_create()
    except AttributeError:
        print("OpenCV face module not available. Install opencv-contrib-python")
        return 1  # Skip face auth if module not available

    # Check if trainer file exists
    trainer_path = 'engine\\auth\\trainer\\trainer.yml'
    if not os.path.exists(trainer_path):
        print(f"Trainer file not found: {trainer_path}")
        print("Please train the face recognition model first")
        return 1
    
    try:
        recognizer.read(trainer_path)  # load trained model
    except Exception as e:
        print(f"Failed to load trainer model: {e}")
        return 1
    
    cascadePath = "engine\\auth\\haarcascade_frontalface_default.xml"
    if not os.path.exists(cascadePath):
        print(f"Cascade file not found: {cascadePath}")
        return 1
    
    # initializing haar cascade for object detection approach
    faceCascade = cv2.CascadeClassifier(cascadePath)
    if faceCascade.empty():
        print("Failed to load face cascade classifier")
        return 1

    font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type


    id = 2  # number of persons you want to Recognize


    names = ['Unknown', 'User']  # names, leave first empty bcz counter starts from 0


    # Try multiple camera initialization methods
    cam = None
    for camera_index in [0, 1, 2]:
        try:
            # Try with DirectShow backend first (Windows)
            cam = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
            if cam.isOpened():
                ret, test_frame = cam.read()
                if ret:
                    print(f"Camera {camera_index} opened successfully with DSHOW")
                    break
                else:
                    cam.release()
            
            # Try without backend
            cam = cv2.VideoCapture(camera_index)
            if cam.isOpened():
                ret, test_frame = cam.read()
                if ret:
                    print(f"Camera {camera_index} opened successfully")
                    break
                else:
                    cam.release()
                    
        except Exception as e:
            print(f"Camera {camera_index} error: {e}")
            if cam:
                cam.release()
            cam = None
    
    if not cam or not cam.isOpened():
        print("No camera available. Skipping face authentication.")
        return 1  # Skip face auth if no camera
    
    # Set camera properties
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cam.set(cv2.CAP_PROP_FPS, 30)

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    # Balanced security variables
    recognition_count = 0
    required_recognitions = 2  # Need 2 successful recognitions
    max_attempts = 100  # Reasonable attempts
    attempt_count = 0
    
    # Extended timeout for security
    start_time = time.time()
    timeout = 30  # 30 seconds timeout

    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to read from camera")
            time.sleep(0.1)
            continue
            
        attempt_count += 1
        
        # Auto-close after timeout
        if time.time() - start_time > timeout:
            print("Face authentication timeout")
            flag = 0
            break

        # Enhanced image preprocessing for better recognition
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Apply histogram equalization for better lighting conditions
        converted_image = cv2.equalizeHist(converted_image)

        # Improved face detection parameters
        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.05,
            minNeighbors=3,
            minSize=(30, 30),
            maxSize=(300, 300),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Extract face region with padding for better recognition
            face_roi = converted_image[y:y+h, x:x+w]
            
            # Resize face for consistent recognition
            face_roi = cv2.resize(face_roi, (100, 100))
            
            # Predict with improved face region
            id, confidence = recognizer.predict(face_roi)

            # Improved confidence threshold
            if confidence < 85:  # More lenient for better detection
                # Safe array access
                if id < len(names):
                    recognized_name = names[id]
                else:
                    recognized_name = "User"
                    
                accuracy = "{0}%".format(round(100 - confidence))
                recognition_count += 1
                
                # Display success indicator
                cv2.putText(img, f"Recognized: {recognition_count}/{required_recognitions}", 
                           (10, 30), font, 0.7, (0, 255, 0), 2)
                
                # Success after multiple recognitions
                if recognition_count >= required_recognitions:
                    flag = 1
                    break
            else:
                recognized_name = "Unknown"
                accuracy = "{0}%".format(round(100 - confidence))
                recognition_count = 0  # Reset count on failed recognition

            cv2.putText(img, str(recognized_name), (x+5, y-5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x+5, y+h-5), font, 1, (255, 255, 0), 1)

            cv2.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x+5, y+h-5), font, 1, (255, 255, 0), 1)

        # Display security instructions
        cv2.putText(img, "SECURE MODE: Only trained face allowed", (10, img.shape[0]-40), 
                   font, 0.6, (0, 0, 255), 2)
        cv2.putText(img, "Look directly at camera", (10, img.shape[0]-20), 
                   font, 0.5, (255, 255, 255), 1)
        cv2.putText(img, "Authentication required to continue", (10, img.shape[0]-5), 
                   font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Jarvis Face Authentication', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:  # ESC key - exit application
            flag = 0
            break
        if flag == 1:
            break
            
        # Max attempts reached
        if attempt_count >= max_attempts:
            print("Max attempts reached")
            flag = 0
            break
            

    # Do a bit of cleanup
    
    cam.release()
    cv2.destroyAllWindows()
    return flag