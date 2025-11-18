# Quick Start Guide

Get up and running with Advanced Face Detection System in 5 minutes!

## 🚀 Fast Installation

```bash
# 1. Clone the repository
git clone https://github.com/Hamad-Ansari/Advanced-Face-Detection-System.git
cd Advanced-Face-Detection-System

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python run.py
```

## 📥 Download Models (Optional but Recommended)

For age and gender detection, download these files to the `models/` directory:

**Quick Download Commands:**
```bash
cd models

# Download age detection model
wget https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/age_net.caffemodel
wget https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/age_deploy.prototxt

# Download gender detection model
wget https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/gender_net.caffemodel
wget https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/gender_deploy.prototxt

cd ..
```

**Or download manually:**
- Visit: https://github.com/opencv/opencv_extra/tree/master/testdata/dnn
- Download all 4 files to `models/` directory

## 🎮 Basic Usage

### Run the Application
```bash
python run.py
```

### Keyboard Controls
| Key | Action |
|-----|--------|
| `Q` | Quit |
| `S` | Toggle face detection |
| `A` | Toggle age/gender detection |

## 🐍 Python Code Example

```python
import cv2
import mediapipe as mp

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(
    model_selection=1,
    min_detection_confidence=0.5
)

# Open camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect faces
    results = face_detection.process(rgb_frame)
    
    # Draw detections
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x, y = int(bboxC.xmin * iw), int(bboxC.ymin * ih)
            w, h = int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## 📊 Features Overview

### ✅ What Works Out of the Box
- Real-time face detection
- Multi-face tracking
- Confidence scoring
- Mirror mode camera

### 🔧 Requires Model Download
- Age prediction (8 ranges)
- Gender classification
- Advanced analytics

## 🐛 Common Issues

### Camera Not Working?
```bash
# Try different camera index
# In run.py, change:
cap = cv2.VideoCapture(0)  # Try 1, 2, etc.
```

### Import Errors?
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Low FPS?
```bash
# Reduce resolution in run.py:
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
```

## 📚 Next Steps

1. **Explore Notebooks**: Check `notebooks/` for tutorials
2. **Read Full Docs**: See [README.md](README.md) for details
3. **Customize**: Modify `run.py` for your needs
4. **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## 💡 Pro Tips

- Use good lighting for better detection
- Keep face frontal for age/gender accuracy
- Close other camera apps before running
- Update graphics drivers for better performance

## 🆘 Need Help?

- **Documentation**: [README.md](README.md)
- **Installation Issues**: [INSTALLATION.md](INSTALLATION.md)
- **Bug Reports**: [GitHub Issues](https://github.com/Hamad-Ansari/Advanced-Face-Detection-System/issues)
- **Email**: mrhammadzahid24@gmail.com

---

**Ready to go? Run `python run.py` and start detecting faces! 🎉**
