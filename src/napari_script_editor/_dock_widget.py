"""
This module is an example of a barebones QWidget plugin for napari

It implements the ``napari_experimental_provide_dock_widget`` hook specification.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs.
"""
from napari_plugin_engine import napari_hook_implementation
from qtpy.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
from magicgui import magic_factory

from pyqode.python.backend import server
from pyqode.python.widgets import PyCodeEdit
from pyqode.python.widgets import code_edit

from ._scripts_directory import _init_scripts_directory, _new_template_filename
import os

class ExampleQWidget(QWidget):
    # your QWidget.__init__ can optionally request the napari viewer instance
    # in one of two ways:
    # 1. use a parameter called `napari_viewer`, as done here
    # 2. use a type annotation of 'napari.viewer.Viewer' for any parameter
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        #self._backend()

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
            print("Load", filename)
            self.code_edit.file.open(filename)

    def _on_save_click(self):
        filename, _ = QFileDialog.getSaveFileName(parent=self, filter="*.py", directory=_init_scripts_directory())
        print("Save?", filename)

        if isinstance(filename, str) and len(filename) > 0:
            print("Save", filename)
            self.code_edit.file.save(filename)

    def _on_run_click(self):
        code = self.code_edit.toPlainText()
        globs = {"viewer": self.viewer}

        exec(code, globs)
    def _backend(self):
        if not hasattr(ExampleQWidget, "backend"):
            from pyqode.core import backend
            backend.CodeCompletionWorker.providers.append(
                backend.DocumentWordsProvider())
            backend.serve_forever()
            ExampleQWidget.backend = backend

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    # you can return either a single widget, or a sequence of widgets
    return [ExampleQWidget]
