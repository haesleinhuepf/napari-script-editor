import napari
import warnings
from skimage.measure import regionprops
import matplotlib.pyplot as plt

if 'viewer' not in globals():
    viewer = napari.Viewer()

# first selected image and label layers from the viewer
image_layers = [
            layer for layer in viewer.layers.selection
            if isinstance(layer, napari.layers.Image)
        ]
label_layers = [
            layer for layer in viewer.layers.selection
            if isinstance(layer, napari.layers.Image)
         ]
if len(image_layers) != 1 or len(label_layers) != 1:
    warnings.warn("Please select one image and one labels layer!")
image = image_layers[0].data
labels = label_layers[0].data

# determine size and shape
stats = regionprops(labels, image)
area = [s['area'] for s in stats]
aspect_ratio = [s['minor_axis_length'] / s['major_axis_length'] for s in stats]

# plot size against shape
plt.scatter(area, aspect_ratio)
plt.show()
