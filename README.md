# 🚀 Advanced Face Detection System

An advanced real-time face detection system featuring **MediaPipe integration**, **AI-powered age/gender prediction**, **468 facial landmarks**, **AR filters**, and a **professional modern UI**. Built with computer vision and deep learning technologies.

## ✨ Features

### 🎯 **Core Detection Capabilities**
- **MediaPipe Face Detection** - 10x more accurate than traditional Haar cascades
- **Real-time Performance** - Optimized for smooth 30+ FPS processing
- **Multi-face Support** - Detect and track up to 5 faces simultaneously
- **Confidence Scoring** - Advanced confidence metrics for each detection

### 🧠 **AI-Powered Analysis**
- **Age Prediction** - CNN-based age estimation in 8 ranges: (0-2), (4-6), (8-12), (15-20), (25-32), (38-43), (48-53), (60-100)
- **Gender Classification** - Real-time Male/Female prediction
- **Detection Quality Assessment** - Advanced confidence scoring system

### 📍 **Advanced Facial Features**
- **468 Facial Landmarks** - Precise face mesh with MediaPipe
- **3D Face Mesh Visualization** - Real-time 3D facial contours
- **Key Feature Tracking** - Eyes, nose, mouth, eyebrows tracking
- **Facial Geometry Analysis** - Face orientation and dimensions

### 🕶️ **Augmented Reality Filters**
- **Smart Sunglasses Filter** - Auto-adapts to face size and eye distance
- **Mustache Overlay** - Positioned between nose and mouth
- **Hat Filter** - Intelligent forehead placement
- **Alpha Blending** - Realistic transparency effects
- **Real-time Filter Switching** - Instant filter changes via keyboard

### 🎨 **Professional Modern UI**
- **Rounded Design Elements** - Modern, sleek interface
- **Color-coded Status Indicators** - Performance-based visual feedback
- **Real-time Performance Graph** - Live FPS monitoring
- **Categorized Controls** - Organized filter and view options
- **Professional Color Scheme** - Lime green, gold, and dark theme

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.7+
Webcam or camera device
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Hamad-Ansari/Advanced-Face-Detection-System.git
cd Advanced-Face-Detection-System
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Download AI Models**
   
   The pre-trained models are included in the `models/` directory:
   - `age_net.caffemodel` (~44MB)
   - `age_deploy.prototxt` (~2KB)
   - `gender_net.caffemodel` (~44MB)
   - `gender_deploy.prototxt` (~2KB)

4. **Run the application**
```bash
python run.py
```

## 📁 Project Structure

```
Advanced-Face-Detection-System/
├── 📁 models/                    # AI model files
│   ├── age_net.caffemodel
│   ├── age_deploy.prototxt
│   ├── gender_net.caffemodel
│   └── gender_deploy.prototxt
├── 📁 notebooks/                 # Jupyter notebooks
│   ├── 1_face_detection.ipynb
│   ├── 2_ai_powered_detection.ipynb
│   ├── 3_all_in_one_detection.ipynb
│   └── 4_full_feature_app.ipynb
├── 📄 face_detector.py          # Core MediaPipe face detection
├── 📄 landmarks_detector.py     # 468 facial landmarks
├── 📄 age_gender_detector.py    # AI age/gender prediction
├── 📄 ar_filters.py            # AR filters system
├── 📄 ui_manager.py            # Professional UI components
├── 📄 main_app.py              # Main application logic
├── 📄 run.py                   # Application launcher
├── 📄 requirements.txt         # Dependencies
├── 📄 README.md               # This file
├── 📄 INSTALLATION.md         # Detailed installation guide
├── 📄 CONTRIBUTING.md         # Contribution guidelines
└── 📄 LICENSE                 # MIT license
```

## 🎮 Controls & Usage

### **Keyboard Controls**
| Key | Function |
|-----|----------|
| `S` | Toggle Sunglasses Filter |
| `M` | Toggle Mustache Filter |
| `H` | Toggle Hat Filter |
| `L` | Show/Hide 468 Landmarks |
| `F` | Toggle 3D Face Mesh |
| `A` | Enable/Disable Age/Gender Detection |
| `C` | Show/Hide Control Panel |
| `Q` | Quit Application |

### **UI Panels**
- **Left Panel**: Categorized controls (Filters, View Options, System)
- **Right Panel**: System status, performance metrics, detection quality
- **Bottom Right**: Real-time FPS performance graph

## 🔧 Technical Details

### **Core Technologies**
- **MediaPipe** - Google's ML framework for face detection
- **OpenCV** - Computer vision and image processing
- **Deep Learning Models** - CNN-based age/gender classification
- **NumPy** - Numerical computations and array operations

### **Performance Specifications**
- **Detection Accuracy**: 95%+ with MediaPipe
- **Processing Speed**: 25-35 FPS on modern hardware
- **Memory Usage**: ~200MB during operation
- **Supported Resolutions**: 480p to 1080p

### **AI Model Details**
- **Age Detection**: 8-class CNN classifier
- **Gender Detection**: Binary CNN classifier
- **Input Size**: 227x227 pixels
- **Framework**: Caffe models converted for OpenCV DNN

## 📊 Module Documentation

### 1. **face_detector.py**
```python
class MediaPipeFaceDetector:
    """
    Advanced face detection using MediaPipe
    - 10x more accurate than Haar cascades
    - Real-time performance optimization
    - Confidence scoring for each detection
    """
```

### 2. **landmarks_detector.py**
```python
class FacialLandmarksDetector:
    """
    468 facial landmarks detection and visualization
    - Precise face mesh tracking
    - 3D facial contours
    - Key feature point identification
    """
```

### 3. **age_gender_detector.py**
```python
class AgeGenderDetector:
    """
    CNN-based age and gender prediction
    - 8 age ranges classification
    - Binary gender classification
    - Confidence scoring system
    """
```

### 4. **ar_filters.py**
```python
class ARFilters:
    """
    Augmented reality filter system
    - Smart filter positioning
    - Alpha blending effects
    - Adaptive scaling based on face size
    """
```

### 5. **ui_manager.py**
```python
class UIManager:
    """
    Professional modern UI system
    - Rounded design elements
    - Color-coded status indicators
    - Real-time performance monitoring
    """
```

## 🛠️ Development Setup

### **For Contributors**

1. **Fork the repository**
2. **Create a virtual environment**
```bash
python -m venv face_detection_env
source face_detection_env/bin/activate  # Linux/Mac
# or
face_detection_env\Scripts\activate     # Windows
```

3. **Install development dependencies**
```bash
pip install -r requirements.txt
```

4. **Run tests**
```bash
python -m pytest tests/
```

### **Adding New Features**

- **New Filters**: Add methods to `ar_filters.py`
- **UI Improvements**: Modify `ui_manager.py`
- **Detection Features**: Extend `face_detector.py`
- **AI Models**: Update `age_gender_detector.py`

## 🐛 Troubleshooting

### **Common Issues**

**Issue**: "Age/Gender models not found"
```bash
Solution: Ensure models/ directory contains all .caffemodel and .prototxt files
```

**Issue**: "Camera not detected"
```bash
Solution: Check camera permissions and ensure no other app is using the camera
```

**Issue**: "Low FPS performance"
```bash
Solution: Reduce resolution or disable some features (landmarks, filters)
```

**Issue**: "Import errors"
```bash
Solution: Reinstall dependencies with: pip install -r requirements.txt --upgrade
```

## 📈 Performance Optimization

### **Tips for Better Performance**
1. Use a dedicated GPU for faster processing
2. Reduce camera resolution for lower-end systems
3. Disable unused features (landmarks, filters)
4. Close other resource-intensive applications
5. Update graphics drivers

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Hamad Ansari**
- GitHub: [@Hamad-Ansari](https://github.com/Hamad-Ansari)
- Email: mrhammadzahid24@gmail.com

## 🙏 Acknowledgments

- MediaPipe team for the excellent face detection framework
- OpenCV community for computer vision tools
- Original age/gender models from OpenCV model zoo
- Inspiration from various face detection projects

## 📞 Support

For support, email mrhammadzahid24@gmail.com or open an issue in the GitHub repository.

---

⭐ **Star this repository if you find it helpful!**
