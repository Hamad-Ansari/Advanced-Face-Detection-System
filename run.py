#!/usr/bin/env python3
"""
Advanced Face Detection System - Main Launcher
Author: Hamad Ansari
Description: Entry point for the face detection application
"""

import sys
import cv2
import mediapipe as mp
import numpy as np
from pathlib import Path

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_modules = {
        'cv2': 'opencv-python',
        'mediapipe': 'mediapipe',
        'numpy': 'numpy'
    }
    
    missing = []
    for module, package in required_modules.items():
        try:
            __import__(module)
        except ImportError:
            missing.append(package)
    
    if missing:
        print("❌ Missing required packages:")
        for package in missing:
            print(f"   - {package}")
        print("\n💡 Install with: pip install -r requirements.txt")
        return False
    return True

def check_models():
    """Check if AI models are present"""
    models_dir = Path('models')
    required_files = [
        'age_net.caffemodel',
        'age_deploy.prototxt',
        'gender_net.caffemodel',
        'gender_deploy.prototxt'
    ]
    
    missing = []
    for file in required_files:
        if not (models_dir / file).exists():
            missing.append(file)
    
    if missing:
        print("❌ Missing model files in models/ directory:")
        for file in missing:
            print(f"   - {file}")
        print("\n💡 Download models from:")
        print("   https://github.com/opencv/opencv_extra/tree/master/testdata/dnn")
        return False
    return True

def main():
    """Main application entry point"""
    print("=" * 60)
    print("🚀 Advanced Face Detection System")
    print("   Author: Hamad Ansari")
    print("=" * 60)
    print()
    
    # Check dependencies
    print("🔍 Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    print("✅ All dependencies installed")
    
    # Check models
    print("🔍 Checking AI models...")
    if not check_models():
        print("\n⚠️  Running without age/gender detection")
        print("   Download models to enable this feature")
    else:
        print("✅ All models found")
    
    print()
    print("🎮 Keyboard Controls:")
    print("   Q - Quit application")
    print("   S - Toggle face detection")
    print("   A - Toggle age/gender detection")
    print("   L - Toggle landmarks")
    print()
    print("📹 Starting camera...")
    
    try:
        # Initialize MediaPipe Face Detection
        mp_face_detection = mp.solutions.face_detection
        mp_drawing = mp.solutions.drawing_utils
        
        # Initialize camera
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Error: Could not open camera")
            print("💡 Check camera permissions and ensure no other app is using it")
            sys.exit(1)
        
        # Set camera properties
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        # Initialize face detection
        face_detection = mp_face_detection.FaceDetection(
            model_selection=1,
            min_detection_confidence=0.5
        )
        
        # Load age/gender models if available
        age_net = None
        gender_net = None
        
        if check_models():
            try:
                age_net = cv2.dnn.readNet(
                    'models/age_net.caffemodel',
                    'models/age_deploy.prototxt'
                )
                gender_net = cv2.dnn.readNet(
                    'models/gender_net.caffemodel',
                    'models/gender_deploy.prototxt'
                )
                print("✅ Age/Gender models loaded successfully")
            except Exception as e:
                print(f"⚠️  Could not load models: {e}")
        
        # Age and gender lists
        age_list = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', 
                    '(25-32)', '(38-43)', '(48-53)', '(60-100)']
        gender_list = ['Male', 'Female']
        
        # Control flags
        show_detection = True
        show_age_gender = True
        
        print("✅ Application started successfully!")
        print("   Press 'Q' to quit")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Error: Could not read frame")
                break
            
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Convert to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            if show_detection:
                # Detect faces
                results = face_detection.process(rgb_frame)
                
                if results.detections:
                    for detection in results.detections:
                        # Get bounding box
                        bboxC = detection.location_data.relative_bounding_box
                        ih, iw, _ = frame.shape
                        x = int(bboxC.xmin * iw)
                        y = int(bboxC.ymin * ih)
                        w = int(bboxC.width * iw)
                        h = int(bboxC.height * ih)
                        
                        # Draw rectangle
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        
                        # Get confidence score
                        confidence = detection.score[0]
                        cv2.putText(frame, f'Conf: {confidence:.2f}', 
                                  (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                                  0.5, (0, 255, 0), 2)
                        
                        # Age and gender prediction
                        if show_age_gender and age_net and gender_net:
                            try:
                                # Extract face ROI
                                face_roi = frame[max(0, y):min(y + h, ih), 
                                               max(0, x):min(x + w, iw)]
                                
                                if face_roi.size > 0:
                                    # Prepare blob
                                    blob = cv2.dnn.blobFromImage(
                                        face_roi, 1.0, (227, 227),
                                        (78.4263377603, 87.7689143744, 114.895847746),
                                        swapRB=False
                                    )
                                    
                                    # Predict gender
                                    gender_net.setInput(blob)
                                    gender_preds = gender_net.forward()
                                    gender = gender_list[gender_preds[0].argmax()]
                                    
                                    # Predict age
                                    age_net.setInput(blob)
                                    age_preds = age_net.forward()
                                    age = age_list[age_preds[0].argmax()]
                                    
                                    # Display predictions
                                    label = f'{gender}, {age}'
                                    cv2.putText(frame, label, (x, y + h + 25),
                                              cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                              (255, 255, 0), 2)
                            except Exception as e:
                                pass
            
            # Display status
            status_text = "Detection: ON" if show_detection else "Detection: OFF"
            cv2.putText(frame, status_text, (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            if age_net and gender_net:
                age_status = "Age/Gender: ON" if show_age_gender else "Age/Gender: OFF"
                cv2.putText(frame, age_status, (10, 60),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            # Show frame
            cv2.imshow('Advanced Face Detection System', frame)
            
            # Handle keyboard input
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == ord('Q'):
                print("\n👋 Shutting down...")
                break
            elif key == ord('s') or key == ord('S'):
                show_detection = not show_detection
                status = "ON" if show_detection else "OFF"
                print(f"🔄 Face detection: {status}")
            elif key == ord('a') or key == ord('A'):
                show_age_gender = not show_age_gender
                status = "ON" if show_age_gender else "OFF"
                print(f"🔄 Age/Gender detection: {status}")
        
        # Cleanup
        cap.release()
        cv2.destroyAllWindows()
        face_detection.close()
        print("✅ Application closed successfully")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
