# This script brings a widget with a "Toggle" button to the
# napari viewer. When the user hits the button, all visible
# selected layers become invisible and all invisible selected
# layers become visible.
import napari
from qtpy.QtWidgets import QWidget, QPushButton, QVBoxLayout

if 'viewer' not in globals():
    viewer = napari.Viewer()


class ToggleVisibility(QWidget):
    """
    A widget with a "Toggle" button, that can be attached
    to the napari viewer.
    """
    def __init__(self):
        super().__init__()
        # Build button
        btn_toggle = QPushButton("Toggle")
        btn_toggle.clicked.connect(self._toggle)
        btn_toggle.setMinimumHeight(100)

        # Add button to widget
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(btn_toggle)

    def _toggle(self):
        """
        When the user hits the "Toggle" button, all selected
        layers which were visible before become invisible and
        vise versa.
        """
        for layer in viewer.layers.selection:
            layer.visible = not layer.visible

# Add widget to the napari viewer
viewer.window.add_dock_widget(ToggleVisibility())
