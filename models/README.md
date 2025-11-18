# AI Models Directory

This directory contains the pre-trained Caffe models for age and gender detection.

## Required Files

The following model files are required for the face detection system to work:

1. **age_net.caffemodel** (~44 MB)
   - Pre-trained CNN model for age classification
   - Classifies faces into 8 age ranges

2. **age_deploy.prototxt** (~2 KB)
   - Network architecture definition for age detection
   - Defines the layers and structure of the age model

3. **gender_net.caffemodel** (~44 MB)
   - Pre-trained CNN model for gender classification
   - Binary classification: Male/Female

4. **gender_deploy.prototxt** (~2 KB)
   - Network architecture definition for gender detection
   - Defines the layers and structure of the gender model

## Download Instructions

### Option 1: OpenCV Model Zoo
Download from the official OpenCV repository:
```
https://github.com/opencv/opencv_extra/tree/master/testdata/dnn
```

### Option 2: Alternative Source
```
https://github.com/Isfhan/age-gender-detection
```

### Option 3: Direct Links
You can also download directly from these links:
- Age Model: [age_net.caffemodel](https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/age_net.caffemodel)
- Age Prototxt: [age_deploy.prototxt](https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/age_deploy.prototxt)
- Gender Model: [gender_net.caffemodel](https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/gender_net.caffemodel)
- Gender Prototxt: [gender_deploy.prototxt](https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/gender_deploy.prototxt)

## Installation

After downloading, place all four files in this `models/` directory:

```
models/
├── age_net.caffemodel
├── age_deploy.prototxt
├── gender_net.caffemodel
├── gender_deploy.prototxt
└── README.md (this file)
```

## Model Details

### Age Detection Model
- **Architecture**: CNN (Convolutional Neural Network)
- **Input Size**: 227x227 pixels
- **Output Classes**: 8 age ranges
  - (0-2), (4-6), (8-12), (15-20), (25-32), (38-43), (48-53), (60-100)
- **Framework**: Caffe
- **Accuracy**: ~50-60% (varies by dataset)

### Gender Detection Model
- **Architecture**: CNN (Convolutional Neural Network)
- **Input Size**: 227x227 pixels
- **Output Classes**: 2 (Male, Female)
- **Framework**: Caffe
- **Accuracy**: ~90-95% (varies by dataset)

## Verification

To verify the models are correctly placed, run:

```bash
ls -lh models/
```

You should see all four files with the correct sizes:
- age_net.caffemodel: ~44 MB
- age_deploy.prototxt: ~2 KB
- gender_net.caffemodel: ~44 MB
- gender_deploy.prototxt: ~2 KB

## Troubleshooting

**Issue: Models not loading**
- Verify file names match exactly (case-sensitive)
- Check file sizes to ensure complete downloads
- Ensure files are not corrupted

**Issue: Low accuracy**
- Models work best with frontal face images
- Ensure good lighting conditions
- Face should be clearly visible and not occluded

## License

These models are from the OpenCV project and are available under the Apache 2.0 License.

## Credits

- Original models from OpenCV DNN module
- Trained on Adience dataset for age/gender classification
