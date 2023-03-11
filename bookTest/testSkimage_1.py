import numpy as np
import matplotlib.pyplot as plt
import skimage

from scipy import ndimage as ndi
from skimage import feature
from skimage import viewer

filename = "./filesForTests/cannyTest2.jpg"

# load and display original image as grayscale
im = skimage.io.imread(fname=filename, as_gray=True)

# Compute the Canny filter for two values of sigma
edges1 = feature.canny(im, sigma=0.3)
edges2 = feature.canny(im, sigma=0.8)

# display results
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)

ax1.imshow(im, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('noisy image', fontsize=20)

ax2.imshow(edges1, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title(r'Canny filter, $\sigma=0.3$', fontsize=20)

ax3.imshow(edges2, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title(r'Canny filter, $\sigma=0.8$', fontsize=20)

fig.tight_layout()

plt.show()