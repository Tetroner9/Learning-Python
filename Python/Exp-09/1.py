import cv2
from colormath.color_objects import sRGBColor, CMYKColor
from colormath.color_conversions import convert_color
import numpy as np
import matplotlib.pyplot as plt

# a
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

histogram, bins = np.histogram(image.ravel(), 256, [0, 256])

# Plot the histogram
plt.hist(image.ravel(), 256, [0, 256])
plt.xlabel('Intensity Value')
plt.ylabel('Frequency')
plt.title('Image Histogram')
plt.show()

# b
image = cv2.imread('image.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image_rgb_color = sRGBColor(*image_rgb[0, 0, :])

image_cmyk_color = convert_color(image_rgb_color, CMYKColor)

image_cmyk = np.array(image_cmyk_color.get_value_tuple(), dtype=np.uint8)

image_cmyk = cv2.cvtColor(image_cmyk, cv2.COLOR_RGB2BGR)

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(image_rgb)
plt.title('RGB Image')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(image_cmyk, cv2.COLOR_BGR2RGB))
plt.title('CMYK Image')

plt.show()

# c
image = cv2.imread('image.jpg')

b, g, r = cv2.split(image)

hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

plt.figure(figsize=(8, 6))
plt.plot(hist_b, color='b', label='Blue')
plt.plot(hist_g, color='g', label='Green')
plt.plot(hist_r, color='r', label='Red')
plt.title('Color Space Histograms')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# d
image = cv2.imread('image.jpg', 0)

equ = cv2.equalizeHist(image)

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(equ, cmap='gray')
plt.title('Equalized Image')
plt.show()

# e
image = cv2.imread('image.jpg', 0)

edges = cv2.Canny(image, 100, 200)

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Edge-Detected Image')
plt.show()

# f
image = cv2.imread('image.jpg')

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

pixels = image.reshape((-1, 3))

pixels = np.float32(pixels)

num_clusters = 5
max_iterations = 10
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, max_iterations, 1.0)

_, labels, centers = cv2.kmeans(pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

segmented_image = labels.reshape(image.shape[:2])

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(segmented_image, cmap='nipy_spectral')
plt.title('Segmented Image')
plt.show()
