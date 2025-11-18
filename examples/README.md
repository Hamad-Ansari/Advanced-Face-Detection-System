# Examples Directory

This directory contains practical examples demonstrating various features of the Advanced Face Detection System.

## Available Examples

### 1. Basic Detection (`basic_detection.py`)
Simple face detection using MediaPipe with confidence scoring.

**Features:**
- Real-time face detection
- Confidence score display
- Bounding box visualization

**Run:**
```bash
python examples/basic_detection.py
```

## Coming Soon

### 2. Age Gender Detection
Example showing age and gender prediction on detected faces.

### 3. Multi-Face Tracking
Demonstration of tracking multiple faces simultaneously.

### 4. Landmarks Visualization
Example showing 468 facial landmarks detection.

### 5. Video Processing
Process video files instead of live camera feed.

### 6. Image Batch Processing
Process multiple images in a directory.

## Usage Tips

### Running Examples
```bash
# From project root
python examples/basic_detection.py

# Or make executable and run directly
chmod +x examples/basic_detection.py
./examples/basic_detection.py
```

### Modifying Examples
Feel free to modify these examples to:
- Change detection parameters
- Add custom visualizations
- Integrate with your own projects
- Test different camera sources

### Common Parameters

**Camera Selection:**
```python
cap = cv2.VideoCapture(0)  # 0 for default camera
cap = cv2.VideoCapture(1)  # 1 for external camera
```

**Detection Confidence:**
```python
face_detection = mp_face_detection.FaceDetection(
    min_detection_confidence=0.5  # 0.0 to 1.0
)
```

**Model Selection:**
```python
# 0: Short-range model (within 2 meters)
# 1: Full-range model (within 5 meters)
face_detection = mp_face_detection.FaceDetection(
    model_selection=1
)
```

## Creating Your Own Examples

Template structure:
```python
#!/usr/bin/env python3
"""
Your Example Name
Description of what it does
"""

import cv2
import mediapipe as mp

def main():
    # Your code here
    pass

if __name__ == "__main__":
    main()
```

## Troubleshooting

**Camera not opening:**
```python
# Try different camera indices
for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera found at index {i}")
        break
```

**Low FPS:**
```python
# Reduce resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
```

## Contributing Examples

Have a cool example? Submit a pull request!

**Guidelines:**
- Keep examples simple and focused
- Add clear comments
- Include docstrings
- Test before submitting
- Update this README

## Resources

- [MediaPipe Documentation](https://google.github.io/mediapipe/)
- [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)
- [Main Project README](../README.md)

## License

All examples are licensed under MIT License, same as the main project.
