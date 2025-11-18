"""
Setup script for Advanced Face Detection System
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="advanced-face-detection",
    version="1.0.0",
    author="Hamad Ansari",
    author_email="mrhammadzahid24@gmail.com",
    description="Professional real-time face detection system with AI-powered age/gender prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hamad-Ansari/Advanced-Face-Detection-System",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "opencv-python>=4.8.0",
        "opencv-contrib-python>=4.8.0",
        "mediapipe>=0.10.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "Pillow>=10.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "jupyter>=1.0.0",
        ],
        "full": [
            "face_recognition>=1.3.0",
            "dlib>=19.24.0",
            "keras>=2.13.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "face-detection=run:main",
        ],
    },
    include_package_data=True,
    keywords=[
        "face-detection",
        "computer-vision",
        "mediapipe",
        "opencv",
        "age-detection",
        "gender-detection",
        "deep-learning",
        "ai",
        "machine-learning",
    ],
    project_urls={
        "Bug Reports": "https://github.com/Hamad-Ansari/Advanced-Face-Detection-System/issues",
        "Source": "https://github.com/Hamad-Ansari/Advanced-Face-Detection-System",
        "Documentation": "https://github.com/Hamad-Ansari/Advanced-Face-Detection-System/blob/main/README.md",
    },
)
