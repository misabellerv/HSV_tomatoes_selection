import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

tomatoes = cv.imread('../images/tomatoes.png')
tomatoes = cv.cvtColor(tomatoes, cv.COLOR_BGR2RGB)

r, g, b = cv.split(tomatoes)

fig = plt.figure(figsize=(12, 6))  
ax1 = fig.add_subplot(121, projection="3d")  

pixel_colors = tomatoes.reshape((np.shape(tomatoes)[0]*np.shape(tomatoes)[1], 3))
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()

ax1.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
ax1.set_xlabel("Red")
ax1.set_title('RGB color space - Tomatoes')
ax1.set_ylabel("Green")
ax1.set_zlabel("Blue")

hsv_ball = cv.cvtColor(tomatoes, cv.COLOR_RGB2HSV)
h, s, v = cv.split(hsv_ball)

ax2 = fig.add_subplot(122, projection="3d") 
ax2.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
ax2.set_xlabel("Hue")
ax2.set_title('HSV color space - Tomatoes')
ax2.set_ylabel("Saturation")
ax2.set_zlabel("Value")

plt.tight_layout() 
plt.savefig('rgb_and_hsv_tomato.jpg')
plt.show()
