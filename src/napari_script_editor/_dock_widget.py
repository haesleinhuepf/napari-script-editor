from napari_plugin_engine import napari_hook_implementation
from qtpy.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog

from pyzo.codeeditor import CodeEditor

from ._scripts_directory import _init_scripts_directory, _new_template_filename, _exec_code
import os
from napari_tools_menu import register_dock_widget
from ._utils import read_text_file, write_text_file

@register_dock_widget(menu="Scripts > Script Editor")
class ScriptEditor(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self._viewer = napari_viewer
        ScriptEditor._add_script_editor(self)

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

        self._code_edit = CodeEditor()
        self.layout().addWidget(self._code_edit)

        #self._code_edit.setStyleSheet("background-color: rgb(196, 196, 196);")
        self._on_new_click()

    def _on_new_click(self):
        new_template = _init_scripts_directory() + _new_template_filename()
        self._code_edit.setPlainText(read_text_file(new_template))

    def _on_load_click(self):
        filename,_ = QFileDialog.getOpenFileName(parent=self, filter="*.py", directory=_init_scripts_directory())
        if os.path.isfile(filename):
            self._code_edit.setPlainText(read_text_file(filename))

    def _on_save_click(self):
        filename, _ = QFileDialog.getSaveFileName(parent=self, filter="*.py", directory=_init_scripts_directory())

        if isinstance(filename, str) and len(filename) > 0:
            write_text_file(filename, self._code_edit.toPlainText())

    def _on_run_click(self):
        _exec_code(self._code_edit.toPlainText(), self._viewer)

    def set_code(self, code):
        self._code_edit.setPlainText(code)

    @classmethod
    def _add_script_editor(cls, instance):
        if not hasattr(cls, "editors"):
            cls.editors = []
        cls.editors.append(instance)

    @classmethod
    def get_script_editor_from_viewer(cls, viewer, create_editor=True):
        result = None
        if hasattr(cls, "editors"):
            # search for the last editor which was added
            for editor in cls.editors:
                if editor._viewer is viewer:
                    result = editor
        if result is None:
            if create_editor:
                result = ScriptEditor(viewer)
                w = viewer.window.add_dock_widget(result, area='right', name="Script editor")
                w.setFloating(True)
                w.resize(600, 400)

        return result


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return [ScriptEditor]
