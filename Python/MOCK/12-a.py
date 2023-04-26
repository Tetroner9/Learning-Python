from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the image file
image = Image.open('image.jpg')

# Split the image into its color space planes
r, g, b = image.split()

# Create histograms for each color space plane
r_hist = np.array(r.histogram())
g_hist = np.array(g.histogram())
b_hist = np.array(b.histogram())

# Plot the histograms
fig, ax = plt.subplots()
ax.bar(range(256), r_hist, color='red', alpha=0.5)
ax.bar(range(256), g_hist, color='green', alpha=0.5)
ax.bar(range(256), b_hist, color='blue', alpha=0.5)
ax.set_xlabel('Pixel intensity')
ax.set_ylabel('Frequency')
ax.set_title('Color space histograms')
plt.show()

