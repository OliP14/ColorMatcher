from sklearn.cluster import KMeans
from PIL import Image, ImageDraw
# from PIL import ImageDraw as draw

# Load image into numpy array
def path_to_img_array(path):
    img = Image.open(path)
    vec = np.array(img)    
    return vec


# Do k-means clustering over ``vec`` to return ``numColors``
def pick_colors(vec, numColors):
    vec = vec.reshape(-1, 3)
    model = KMeans(n_clusters=numColors).fit(vec)
    return model.cluster_centers_


# Make a long rectangle, composed of the colors
# detailed in colorList, a list of (R, G, B) tuples
def show_key_colors(colorList):
    n = len(colorList)

    im = Image.new('RGBA', (100*n, 100))
    for idx, color in enumerate(colorList):
        color = tuple([int(x) for x in color])
        print(color)
        draw = ImageDraw.Draw(im) # You need to create an object that can be used to draw images with
        draw.rectangle([(100*idx, 0), (100*(idx+1), 100*(idx+1))], fill=tuple(color))
    im.show() # Displays the actual colors
    return im


def avg_rgb(picVec):
    fn = lambda arr, i: int(np.average(arr[:, :, i]))
    return fn(picVec, 0), fn(picVec, 1), fn(picVec, 2) 