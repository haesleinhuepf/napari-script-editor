import napari
if 'viewer' not in globals():
    viewer = napari.Viewer()

layers = list(viewer.layers)
for layer in layers:
    viewer.layers.remove(layer)
