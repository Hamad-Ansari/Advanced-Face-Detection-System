#!/usr/bin/env python3
"""
Basic Face Detection Example
Demonstrates simple face detection using MediaPipe
"""

import cv2
import mediapipe as mp

def main():
    """Run basic face detection"""
    print("Starting Basic Face Detection...")
    print("Press 'Q' to quit")
    
    # Initialize MediaPipe Face Detection
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    
    # Create face detection object
    face_detection = mp_face_detection.FaceDetection(
        model_selection=1,  # 0 for short-range, 1 for full-range
        min_detection_confidence=0.5
    )
    
    # Open camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    while True:
        # Read frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break
        
        # Flip frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detect faces
        results = face_detection.process(rgb_frame)
        
        # Draw detections
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
                
                # Get confidence
                confidence = detection.score[0]
                
                # Draw confidence text
                text = f'Confidence: {confidence:.2f}'
                cv2.putText(frame, text, (x, y - 10),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Display frame
        cv2.imshow('Basic Face Detection', frame)
        
        # Check for quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    face_detection.close()
    print("Detection stopped")

if __name__ == "__main__":
    main()
