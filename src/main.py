#!/usr/bin/env python3
"""
Photo Viewer Pro - Main Application
A Python application for viewing and processing images using OpenCV.
"""

import cv2
import numpy as np
import os
import sys
from pathlib import Path


def load_image(image_path):
    """Load an image using OpenCV."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image: {image_path}")
    
    return image

def save_image(image, save_path):
    """Save an image using OpenCV."""
    cv2.imwrite(save_path, image)
    print(f"Image saved to: {save_path}")


def display_image(image, window_name="Photo Viewer Pro"):
    """Display an image using OpenCV."""
    cv2.imshow(window_name, image)
    print("Press any key to close the image window...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    """Main application entry point."""
    print("Photo Viewer Pro - Development Environment")
    print("OpenCV version:", cv2.__version__)
    print("NumPy version:", np.__version__)
    print("Python version:", sys.version)
    print("\nEnvironment is ready for development!")
    print("You can now start coding in the src/ directory. Thank you for using Photo Viewer Pro!\n")
    
    # Example: Load and display a sample image if provided
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        try:
            image = load_image(image_path)
            print(f"Loaded image: {image_path}")
            print(f"Image shape: {image.shape}")
            # convert to gray image
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            save_image(gray_image, "changed/output_image.jpg")

            display_image(image)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("\nUsage: python main.py <image_path>")


if __name__ == "__main__":
    main()
