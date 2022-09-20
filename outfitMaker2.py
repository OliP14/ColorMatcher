from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
from imagetools import (path_to_img_array, pick_colors, show_key_colors)

# Open image (img), put all pixel color values into array (vec)
img = Image.open("testPhoto.jpeg", 'r')
vec = np.array(img)

# Split the vec array into groups of 3 for each RGB pixel value
reshaped = vec.reshape(-1, 3)
plt.imshow(reshaped)

# Pick X amount of the main colors used in the inputted image
colors = pick_colors(vec, 6)
# Print the actual colors chosen above (prints the RGB values)
show_key_colors(colors)


# To Do:
# Make it so it shows the color code of each color in the palette
# Sort colors in palette based off of popularity?
# Start thinking about how to make it create outfits based off of the palette