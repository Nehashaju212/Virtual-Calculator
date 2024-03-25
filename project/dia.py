import cv2
import numpy as np

def find_diameter(image_path, object_color):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image to extract the object
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area
    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour

    # Find the minimum enclosing circle of the contour
    ((x, y), radius) = cv2.minEnclosingCircle(max_contour)

    # Calculate the diameter
    diameter = 2 * radius

    # Draw the contour and circle on the image
    cv2.drawContours(image, [max_contour], -1, (0, 255, 0), 2)
    cv2.circle(image, (int(x), int(y)), int(radius), (0, 0, 255), 2)

    # Show the image
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Return the diameter
    return diameter

# Example usage
image_path = 'path_to_your_image.jpg'
object_color = (0, 0, 255)  # Specify the color of the object you want to find (in BGR format)

diameter = find_diameter(image_path, object_color)
print('Diameter:', diameter)
