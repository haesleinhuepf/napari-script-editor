from napari_plugin_engine import napari_hook_implementation
from qtpy.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog

from pyqode.python.backend import server
from pyqode.python.widgets import PyCodeEdit

from ._scripts_directory import _init_scripts_directory, _new_template_filename, _exec_code
import os
from napari_tools_menu import register_dock_widget

@register_dock_widget(menu="Scripts > Script Editor")
class ScriptEditor(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        wgt = QWidget()
        wgt.setLayout(QHBoxLayout())

        btn = QPushButton("New")
        btn.clicked.connect(self._on_new_click)
        wgt.layout().addWidget(btn)

        btn = QPushButton("Load")
        btn.clicked.connect(self._on_load_click)
        wgt.layout().addWidget(btn)

        btn = QPushButton("Save")
        btn.clicked.connect(self._on_save_click)
        wgt.layout().addWidget(btn)

        btn = QPushButton("Run")
        btn.clicked.connect(self._on_run_click)
        wgt.layout().addWidget(btn)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(wgt)

        self.code_edit = PyCodeEdit(server_script=server.__file__)
        self.layout().addWidget(self.code_edit)

        self.code_edit.setStyleSheet("background-color: rgb(196, 196, 196);")
        self._on_new_click()

    def _on_new_click(self):
        new_template = _init_scripts_directory() + _new_template_filename()
        self.code_edit.file.open(new_template)

    def _on_load_click(self):
        filename,_ = QFileDialog.getOpenFileName(parent=self, filter="*.py", directory=_init_scripts_directory())
        if os.path.isfile(filename):
            self.code_edit.file.open(filename)

    def _on_save_click(self):
        filename, _ = QFileDialog.getSaveFileName(parent=self, filter="*.py", directory=_init_scripts_directory())

        if isinstance(filename, str) and len(filename) > 0:
            self.code_edit.file.save(filename)

    def _on_run_click(self):
        _exec_code(self.code_edit.toPlainText(), self.viewer)

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return [ScriptEditor]
