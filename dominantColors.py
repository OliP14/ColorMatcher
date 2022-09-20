import matplotlib.image as img
import matplotlib.pyplot as plt
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
import pandas as pd

img = img.imread('testPhoto.jpeg')

r = []
g = []
b = []
for row in img:
	for temp_r, temp_g, temp_b in row:
		r.append(temp_r)
		g.append(temp_g)
		b.append(temp_b)

img_df = pd.DataFrame({'red' : r,
						'green' : g,
						'blue' : b})

img_df['scaled_color_red'] = whiten(img_df['red'])
img_df['scaled_color_blue'] = whiten(img_df['blue'])
img_df['scaled_color_green'] = whiten(img_df['green'])

cluster_centers, _ = kmeans(img_df[['scaled_color_red',
									'scaled_color_blue',
									'scaled_color_green']], 3)

dominant_colors = []

red_std, green_std, blue_std = img_df[['red',
										'green',
										'blue']].std()

for cluster_center in cluster_centers:
	red_scaled, green_scaled, blue_scaled = cluster_center
	dominant_colors.append((
		red_scaled * red_std / 255,
		green_scaled * green_std / 255,
		blue_scaled * blue_std / 255
	))

plt.imshow([dominant_colors])
plt.show()