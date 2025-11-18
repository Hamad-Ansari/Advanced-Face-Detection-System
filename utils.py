"""
Utility functions for Advanced Face Detection System
Author: Hamad Ansari
"""

import cv2
import numpy as np
from typing import Tuple, List, Optional
import time


class FPSCounter:
    """Calculate and display FPS"""
    
    def __init__(self, window_size: int = 30):
        self.window_size = window_size
        self.frame_times = []
        self.last_time = time.time()
    
    def update(self) -> float:
        """Update FPS calculation"""
        current_time = time.time()
        self.frame_times.append(current_time - self.last_time)
        self.last_time = current_time
        
        if len(self.frame_times) > self.window_size:
            self.frame_times.pop(0)
        
        if len(self.frame_times) > 0:
            avg_time = sum(self.frame_times) / len(self.frame_times)
            return 1.0 / avg_time if avg_time > 0 else 0
        return 0
    
    def get_fps(self) -> float:
        """Get current FPS"""
        if len(self.frame_times) > 0:
            avg_time = sum(self.frame_times) / len(self.frame_times)
            return 1.0 / avg_time if avg_time > 0 else 0
        return 0


def draw_rounded_rectangle(
    img: np.ndarray,
    pt1: Tuple[int, int],
    pt2: Tuple[int, int],
    color: Tuple[int, int, int],
    thickness: int = 2,
    radius: int = 10
) -> np.ndarray:
    """Draw a rounded rectangle"""
    x1, y1 = pt1
    x2, y2 = pt2
    
    # Draw lines
    cv2.line(img, (x1 + radius, y1), (x2 - radius, y1), color, thickness)
    cv2.line(img, (x1 + radius, y2), (x2 - radius, y2), color, thickness)
    cv2.line(img, (x1, y1 + radius), (x1, y2 - radius), color, thickness)
    cv2.line(img, (x2, y1 + radius), (x2, y2 - radius), color, thickness)
    
    # Draw corners
    cv2.ellipse(img, (x1 + radius, y1 + radius), (radius, radius), 180, 0, 90, color, thickness)
    cv2.ellipse(img, (x2 - radius, y1 + radius), (radius, radius), 270, 0, 90, color, thickness)
    cv2.ellipse(img, (x1 + radius, y2 - radius), (radius, radius), 90, 0, 90, color, thickness)
    cv2.ellipse(img, (x2 - radius, y2 - radius), (radius, radius), 0, 0, 90, color, thickness)
    
    return img


def draw_text_with_background(
    img: np.ndarray,
    text: str,
    position: Tuple[int, int],
    font_scale: float = 0.6,
    font_thickness: int = 2,
    text_color: Tuple[int, int, int] = (255, 255, 255),
    bg_color: Tuple[int, int, int] = (0, 0, 0),
    padding: int = 5
) -> np.ndarray:
    """Draw text with background"""
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # Get text size
    (text_width, text_height), baseline = cv2.getTextSize(
        text, font, font_scale, font_thickness
    )
    
    x, y = position
    
    # Draw background rectangle
    cv2.rectangle(
        img,
        (x - padding, y - text_height - padding),
        (x + text_width + padding, y + baseline + padding),
        bg_color,
        -1
    )
    
    # Draw text
    cv2.putText(
        img, text, (x, y),
        font, font_scale, text_color, font_thickness
    )
    
    return img


def resize_with_aspect_ratio(
    image: np.ndarray,
    width: Optional[int] = None,
    height: Optional[int] = None,
    inter: int = cv2.INTER_AREA
) -> np.ndarray:
    """Resize image while maintaining aspect ratio"""
    dim = None
    h, w = image.shape[:2]
    
    if width is None and height is None:
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    
    return cv2.resize(image, dim, interpolation=inter)


def calculate_face_center(bbox: Tuple[int, int, int, int]) -> Tuple[int, int]:
    """Calculate center point of face bounding box"""
    x, y, w, h = bbox
    center_x = x + w // 2
    center_y = y + h // 2
    return center_x, center_y


def calculate_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """Calculate Euclidean distance between two points"""
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def apply_brightness_contrast(
    image: np.ndarray,
    brightness: int = 0,
    contrast: int = 0
) -> np.ndarray:
    """Adjust brightness and contrast of image"""
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow
        
        image = cv2.addWeighted(image, alpha_b, image, 0, gamma_b)
    
    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)
        
        image = cv2.addWeighted(image, alpha_c, image, 0, gamma_c)
    
    return image


def create_gradient_background(
    width: int,
    height: int,
    color1: Tuple[int, int, int] = (50, 50, 50),
    color2: Tuple[int, int, int] = (20, 20, 20)
) -> np.ndarray:
    """Create a gradient background"""
    gradient = np.zeros((height, width, 3), dtype=np.uint8)
    
    for i in range(height):
        ratio = i / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        gradient[i, :] = [b, g, r]
    
    return gradient


def overlay_transparent(
    background: np.ndarray,
    overlay: np.ndarray,
    x: int,
    y: int,
    alpha: float = 1.0
) -> np.ndarray:
    """Overlay a transparent image on background"""
    bg_h, bg_w = background.shape[:2]
    ov_h, ov_w = overlay.shape[:2]
    
    # Ensure overlay fits within background
    if x + ov_w > bg_w:
        ov_w = bg_w - x
        overlay = overlay[:, :ov_w]
    if y + ov_h > bg_h:
        ov_h = bg_h - y
        overlay = overlay[:ov_h, :]
    
    if x < 0 or y < 0:
        return background
    
    # Extract alpha channel if present
    if overlay.shape[2] == 4:
        overlay_rgb = overlay[:, :, :3]
        overlay_alpha = overlay[:, :, 3] / 255.0 * alpha
    else:
        overlay_rgb = overlay
        overlay_alpha = np.ones((ov_h, ov_w)) * alpha
    
    # Blend images
    for c in range(3):
        background[y:y+ov_h, x:x+ov_w, c] = (
            overlay_alpha * overlay_rgb[:, :, c] +
            (1 - overlay_alpha) * background[y:y+ov_h, x:x+ov_w, c]
        )
    
    return background


def get_color_by_confidence(confidence: float) -> Tuple[int, int, int]:
    """Get color based on confidence score"""
    if confidence >= 0.8:
        return (0, 255, 0)  # Green - High confidence
    elif confidence >= 0.6:
        return (0, 255, 255)  # Yellow - Medium confidence
    else:
        return (0, 0, 255)  # Red - Low confidence


def format_time(seconds: float) -> str:
    """Format seconds to readable time string"""
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes}m {secs}s"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        return f"{hours}h {minutes}m"


# Color palette for UI
COLORS = {
    'primary': (0, 255, 0),      # Lime green
    'secondary': (0, 255, 255),  # Yellow
    'accent': (255, 0, 255),     # Magenta
    'success': (0, 255, 0),      # Green
    'warning': (0, 165, 255),    # Orange
    'error': (0, 0, 255),        # Red
    'info': (255, 255, 0),       # Cyan
    'text': (255, 255, 255),     # White
    'background': (30, 30, 30),  # Dark gray
}
