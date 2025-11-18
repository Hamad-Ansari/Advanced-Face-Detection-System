# Installation Guide

## System Requirements

### Minimum Requirements
- Python 3.7 or higher
- 4GB RAM
- Webcam or camera device
- Windows 10, macOS 10.14, or Ubuntu 18.04+

### Recommended Requirements
- Python 3.9+
- 8GB RAM
- Dedicated GPU (for better performance)
- HD webcam (720p or higher)

## Step-by-Step Installation

### 1. Python Installation

**Windows:**
```bash
# Download Python from python.org and install
# Make sure to check "Add Python to PATH"
python --version  # Verify installation
```

**macOS:**
```bash
# Using Homebrew
brew install python3
python3 --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/Hamad-Ansari/Advanced-Face-Detection-System.git
cd Advanced-Face-Detection-System
```

### 3. Create Virtual Environment

```bash
# Create virtual environment
python -m venv face_detection_env

# Activate virtual environment
# Windows:
face_detection_env\Scripts\activate
# macOS/Linux:
source face_detection_env/bin/activate
```

### 4. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# For development (optional):
pip install pytest black flake8
```

### 5. Download AI Models

The models directory should contain the following files:

**Required Model Files:**
- `age_net.caffemodel` (~44 MB)
- `age_deploy.prototxt` (~2 KB)
- `gender_net.caffemodel` (~44 MB)
- `gender_deploy.prototxt` (~2 KB)

**Download from:** 
- https://github.com/opencv/opencv_extra/tree/master/testdata/dnn
- Or: https://github.com/Isfhan/age-gender-detection

**Directory structure after download:**
```
models/
├── age_net.caffemodel
├── age_deploy.prototxt
├── gender_net.caffemodel
└── gender_deploy.prototxt
```

### 6. Test Installation

```bash
python run.py
```

If everything is installed correctly, you should see:
- Camera window opens
- Face detection working
- UI controls visible

## Troubleshooting

### Common Installation Issues

**Issue: "No module named cv2"**
```bash
Solution: pip install opencv-python
```

**Issue: "No module named mediapipe"**
```bash
Solution: pip install mediapipe
```

**Issue: "Camera not found"**
```bash
Solution: 
1. Check camera permissions
2. Close other applications using camera
3. Try different camera index in code (change 0 to 1)
```

**Issue: "Models not found"**
```bash
Solution: 
1. Verify models are downloaded in models/ directory
2. Check file names match exactly
3. Ensure files are not corrupted (check file sizes)
```

## Platform-Specific Notes

### Windows
- May need to install Visual C++ Redistributable
- Windows Defender might flag the executable
- Grant camera permissions in Windows Settings

### macOS
- May need to grant camera permissions in System Preferences
- Install Xcode command line tools if needed:
  ```bash
  xcode-select --install
  ```

### Linux
- May need to install additional packages:
  ```bash
  sudo apt install libgl1-mesa-glx libglib2.0-0
  ```

## Verification

To verify your installation is complete:

1. **Check Python packages:**
   ```bash
   pip list | grep -E "(opencv|mediapipe|numpy)"
   ```

2. **Verify models:**
   ```bash
   ls -la models/
   ```

3. **Test camera:**
   ```bash
   python -c "import cv2; print('OpenCV version:', cv2.__version__)"
   ```

## Next Steps

After successful installation:
1. Read the [README.md](README.md) for usage instructions
2. Check out [CONTRIBUTING.md](CONTRIBUTING.md) if you want to contribute
3. Explore the Jupyter notebooks in the `notebooks/` directory

For additional help, please create an issue on GitHub.
