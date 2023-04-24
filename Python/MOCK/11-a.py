import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

histogram, bins = np.histogram(image.ravel(), 256, [0, 256])

# Plot the histogram
plt.hist(image.ravel(), 256, [0, 256])
plt.xlabel('Intensity Value')
plt.ylabel('Frequency')
plt.title('Image Histogram')
plt.show()
