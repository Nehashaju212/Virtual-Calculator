import cv2
from matplotlib import pyplot as plt
image = cv2.imread('your_image.jpg')
plt.imshow( cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # Threshold the image
plt.imshow(binary_image, cmap='gray')
plt.show()
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
diameters = []
for contour in contours:
    (x, y), radius = cv2.minEnclosingCircle(contour)
    diameter = 2 * radius
    diameters.append(diameter)
result_image = image.copy()
cv2.drawContours(result_image, contours, -1, (0, 255, 0), 2)
for diameter in diameters:
    cv2.putText(result_image, f"Diameter: {diameter}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
plt.show()
