import napari
import warnings
from scipy.ndimage import white_tophat

from qtpy.QtWidgets import QInputDialog

if 'viewer' not in globals():
    viewer = napari.Viewer()

# first selected image and label layers from the viewer
image_layers = [
            layer for layer in viewer.layers.selection
            if isinstance(layer, napari.layers.Image)
        ]
if len(image_layers) != 1:
    warnings.warn("Please select one image layer!")
image = image_layers[0].data

# Ask user for radius
radius, _ = QInputDialog.getInt(
        viewer.window.qt_viewer,
        "Subtract background",
        "radius",
        10
    )

# Apply the filter
filtered = white_tophat(image, size=radius * 2 + 1)

# Save result in a new layer in the viewer
viewer.add_image(filtered, name="Background subtracted "+image_layers[0].name)
