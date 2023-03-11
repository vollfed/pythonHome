import skimage
import skimage.viewer
import sys


# Create the plugin and give it a name
canny_plugin = skimage.viewer.plugins.Plugin(image_filter=skimage.feature.canny)
canny_plugin.name = "Canny Filter Plugin"

# Add sliders for the parameters
canny_plugin += skimage.viewer.widgets.Slider(
    name="sigma", low=0.0, high=7.0, value=2.0
)
canny_plugin += skimage.viewer.widgets.Slider(
    name="low_threshold", low=0.0, high=1.0, value=0.1
)
canny_plugin += skimage.viewer.widgets.Slider(
    name="high_threshold", low=0.0, high=1.0, value=0.2
)

filename = "./filesForTests/cannyTest2.jpg"

image = skimage.io.imread(fname=filename, as_gray=True)
#image1 = skimage.io.imread(fname=filename, as_gray=False)
#viewer = skimage.viewer.ImageViewer(image1)
viewer = skimage.viewer.ImageViewer(image)
viewer += canny_plugin
viewer.show()

