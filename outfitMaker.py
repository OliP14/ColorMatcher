import cv2 as cv
import sys
import matplotlib.pyplot as plt
import array 

# Converts rgb color values to their respective hexadecimal code
# Needed to make comparing used colors easier when keeping count of colors used in photo
# Makes using any() function easier for comparing
def rgbToHex(r, g, b):
    rHex = hex(r)
    gHex = hex(g)
    bHex = hex(b)
    hexPixel = rHex + gHex + bHex
    return hexPixel


# Read the image
img = cv.imread(cv.samples.findFile("testPhoto.jpeg"))
if img is None:
    sys.exit("Could not read the image.")

# Display the image on a graph
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

# Parse through pixel values
imgHeight = img.shape[0]
imgWidth = img.shape[1]
colorList = [] # Used to keep a list of the colors used
countList = [] # Used to keep a list of the amount of times each color is used
for y in range(0, 900): #imgHeight
    for x in range(0, 900): #imgWidth
        px = img[x, y]
        #print(img[950, 0])
        # print(px) # Prints rgb color values
        # print(rgbToHex(px[0], px[1], px[2])) # Prints hex color codes

        px = rgbToHex(px[0], px[1], px[2]) # Convert px value to hex code

        # If the pixel color is in colorList, then increment the colorCount by 1
        # If pixel color is not in colorList, add the color to colorList, set count to 1
        # if any(colorList) == px:
            # countList.index(colorCount[px]) + 1
        # else:
            # colorList.append(px)
            # countList.append(1) # Will this add a new index with value 1 to the countList?

        
        # New method of checking if color is in colorList
        if px in colorList:
            pxIndex = colorList.index(px)
            countList[pxIndex] += 1
        else:
            colorList.append(px)
            countList.append(1)
        
# Print out the colorList and countList
for x in range(len(colorList)):
    print("Color: ", colorList[x], " Count: ", countList[x])

# cv.imshow("Display window", img)
# k = cv.waitKey(0)
# if k == ord("s"):
    # cv.imwrite("testPhoto.png", img)