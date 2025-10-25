import cv2
import os

try:
    # Create samples directory if it doesn't exist
    os.makedirs('engine\\auth\\samples', exist_ok=True)
    
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)
    
    detector = cv2.CascadeClassifier('engine\\auth\\haarcascade_frontalface_default.xml')
    
    print("=== Jarvis Face Training ===")
    print("Instructions:")
    print("1. Look directly at the camera")
    print("2. Move your head slightly for different angles")
    print("3. Press ESC to stop early")
    print("4. 100 samples will be captured automatically")
    print()
    
    face_id = input("Enter your user ID (use 1 for main user): ")
    
    print(f"Starting face capture for user ID {face_id}...")
    print("Position your face in the camera frame...")
    
    count = 0
    
    while True:
        ret, img = cam.read()
        if not ret:
            print("Error: Could not read from camera")
            break
            
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Apply histogram equalization for better detection
        converted_image = cv2.equalizeHist(converted_image)
        
        faces = detector.detectMultiScale(
            converted_image, 
            scaleFactor=1.1, 
            minNeighbors=5,
            minSize=(100, 100)
        )
        
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            count += 1
            
            # Save face sample with better quality
            face_sample = converted_image[y:y+h, x:x+w]
            face_sample = cv2.resize(face_sample, (200, 200))  # Consistent size
            
            cv2.imwrite(f"engine\\auth\\samples\\face.{face_id}.{count}.jpg", face_sample)
            
            # Show progress
            cv2.putText(img, f"Samples: {count}/100", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(img, "Press ESC to stop", (10, 70), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.imshow('Jarvis Face Training - Look at Camera', img)
        
        k = cv2.waitKey(100) & 0xff
        if k == 27:  # ESC key
            break
        elif count >= 100:
            break
    
    print(f"\nCapture completed! {count} samples saved.")
    print("Now run 'py engine/auth/trainer.py' to train the model.")
    
except Exception as e:
    print(f"Error: {e}")
    print("Make sure your camera is working and not used by other applications.")
    
finally:
    try:
        cam.release()
        cv2.destroyAllWindows()
    except:
        pass