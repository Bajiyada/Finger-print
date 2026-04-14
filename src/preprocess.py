def enhance_image(image):
    # Apply histogram equalization to enhance the contrast of the image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    enhanced_image = cv2.equalizeHist(gray_image)
    return enhanced_image

def binarize_image(image, threshold=127):
    # Convert the enhanced image to a binary image using a threshold
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image