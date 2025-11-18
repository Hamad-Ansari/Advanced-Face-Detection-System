# Jupyter Notebooks

This directory contains interactive Jupyter notebooks demonstrating various features of the Advanced Face Detection System.

## Available Notebooks

### 1. Basic Face Detection (`1_face_detection.ipynb`)
- Introduction to face detection with OpenCV
- Haar Cascade vs MediaPipe comparison
- Real-time face detection basics
- Performance optimization tips

### 2. AI-Powered Detection (`2_ai_powered_detection.ipynb`)
- Age and gender prediction
- Loading and using Caffe models
- Understanding CNN predictions
- Confidence scoring

### 3. All-in-One Detection (`3_all_in_one_detection.ipynb`)
- Combining multiple detection features
- Face landmarks (468 points)
- 3D face mesh visualization
- Multi-face tracking

### 4. Full Feature Application (`4_full_feature_app.ipynb`)
- Complete system integration
- AR filters implementation
- Professional UI components
- Performance monitoring

## Getting Started

### Prerequisites
```bash
pip install jupyter notebook
pip install -r ../requirements.txt
```

### Running Notebooks

1. **Start Jupyter Notebook**
```bash
jupyter notebook
```

2. **Navigate to notebooks directory**
3. **Open any notebook and run cells sequentially**

## Notebook Structure

Each notebook follows this structure:
1. **Introduction** - Overview and objectives
2. **Setup** - Import libraries and initialize
3. **Implementation** - Step-by-step code
4. **Examples** - Practical demonstrations
5. **Exercises** - Try it yourself sections
6. **Summary** - Key takeaways

## Tips for Using Notebooks

- Run cells in order from top to bottom
- Restart kernel if you encounter errors
- Modify parameters to experiment
- Save your work frequently
- Use markdown cells for notes

## Creating Your Own Notebooks

Feel free to create your own notebooks exploring:
- Custom face filters
- Different detection algorithms
- Performance benchmarking
- Integration with other libraries

## Troubleshooting

**Issue: Kernel dies when running camera**
```python
# Solution: Use smaller image size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
```

**Issue: Models not loading**
```python
# Solution: Check model paths
import os
print(os.path.exists('../models/age_net.caffemodel'))
```

## Resources

- [Jupyter Documentation](https://jupyter.org/documentation)
- [MediaPipe Guide](https://google.github.io/mediapipe/)
- [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)

## Contributing

Have an interesting notebook to share? Please submit a pull request!

## License

All notebooks are licensed under MIT License, same as the main project.
