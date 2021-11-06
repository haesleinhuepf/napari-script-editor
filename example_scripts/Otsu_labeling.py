import napari

if 'viewer' not in globals():
    viewer = napari.Viewer()


def otsu_labeling(image):
    """
    Thresholds an image using the Otsu (1979)
    technique and connected component labeling to segment objects

    See also
    --------
    .. [1] https://doi.org/10.1109/TSMC.1979.4310076
    """
    from skimage.filters import threshold_otsu
    from skimage.measure import label

    # binarize
    binary = image > threshold_otsu(image)

    # label
    return label(binary)


# get all selected image layers from the viewer
selected_image_layers = [layer for layer in viewer.layers.selection
                         if isinstance(layer, napari.layers.Image)]

# the first image from the selected image layers
image = selected_image_layers[0].data

# segment the image
labels_image = otsu_labeling(image)

# add the result to the viewer
viewer.add_labels(labels_image)
