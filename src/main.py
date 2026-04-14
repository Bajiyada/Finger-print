# main.py

import cv2
from fingerprint import Fingerprint
from preprocess import enhance_image, binarize_image

def main():
    # Initialize the Fingerprint object
    fingerprint_processor = Fingerprint()

    # Load an image (replace 'path_to_image' with the actual image path)
    image_path = 'path_to_image'
    image = cv2.imread(image_path)

    # Preprocess the image
    enhanced_image = enhance_image(image)
    binary_image = binarize_image(enhanced_image)

    # Capture and process the fingerprint
    fingerprint_processor.capture_fingerprint(binary_image)
    features = fingerprint_processor.extract_features()

    # Output the extracted features
    print("Extracted Features:", features)

if __name__ == "__main__":
    main()