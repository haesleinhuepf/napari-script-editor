import napari
from skimage.filters import threshold_otsu

if 'viewer' not in globals():
    viewer = napari.Viewer()

# get all selected image layers from the viewer
selected_image_layers = [layer for layer in viewer.layers.selection
                         if isinstance(layer, napari.layers.Image)]

# the first image from the selected image layers
image = selected_image_layers[0].data

# segment the image
labels_image = image > threshold_otsu(image)

# add the result to the viewer
viewer.add_labels(labels_image)
