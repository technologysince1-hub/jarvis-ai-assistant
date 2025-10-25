#!/usr/bin/env python3
"""
Simple Phone Camera Setup - No ADB Required
"""

def setup_simple_phone_camera():
    print("📱 Simple Phone Camera Setup")
    print("=" * 30)
    
    print("\n🎯 Easiest Method: DroidCam")
    print("1. Download DroidCam Client for PC:")
    print("   https://www.dev47apps.com/droidcam/windows/")
    print("2. Install DroidCam app on your phone from Play Store")
    print("3. Connect both to same WiFi network")
    print("4. Open DroidCam on phone, note the IP address")
    print("5. Open DroidCam Client on PC, enter phone IP")
    print("6. Click 'Start' - phone camera will appear as webcam")
    
    print("\n🎯 Alternative: Phone Link (Windows 11 only)")
    print("1. Open Microsoft Store, install 'Phone Link'")
    print("2. Install 'Link to Windows' on your phone")
    print("3. Follow pairing instructions")
    print("4. In Phone Link settings, enable camera access")
    
    print("\n🎯 Quick Test: Use Phone as Webcam")
    print("1. Install 'EpocCam' or 'iVCam' on phone")
    print("2. Install companion software on PC")
    print("3. Phone will appear as regular webcam")
    
    print("\n✅ After Setup:")
    print("Run: python gemini_live_test.py")
    print("System will automatically detect and use phone camera!")
    
    # Check current cameras
    print("\n🔍 Current Available Cameras:")
    import cv2
    
    for i in range(6):
        try:
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                ret, frame = cap.read()
                if ret and frame is not None:
                    h, w = frame.shape[:2]
                    print(f"  ✅ Camera {i}: {w}x{h} pixels")
                else:
                    print(f"  ⚠️ Camera {i}: Detected but no image")
                cap.release()
            else:
                print(f"  ❌ Camera {i}: Not available")
        except:
            print(f"  ❌ Camera {i}: Error")
    
    print(f"\n🚀 Gemini Live will use the best available camera automatically!")

if __name__ == "__main__":
    setup_simple_phone_camera()