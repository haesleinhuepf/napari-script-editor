from napari_script_editor import ScriptEditor
import pytest

def test_something_with_viewer(make_napari_viewer):
    viewer = make_napari_viewer()


    script_editor = ScriptEditor.get_script_editor_from_viewer(viewer, _for_testing=True)

    num_dw = len(viewer.window._dock_widgets)

    script_editor = ScriptEditor(viewer, _for_testing = True)
    viewer.window.add_dock_widget(
        script_editor
    )
    assert len(viewer.window._dock_widgets) == num_dw + 1

    script_editor._on_new_click()
    script_editor._on_save_click("test.py")
    script_editor._on_load_click("test.py")
    script_editor._on_run_click()
    script_editor.set_code("print('hello world')")

    script_editor = ScriptEditor.get_script_editor_from_viewer(viewer, _for_testing=True)

def test_scripts_directory():
    from napari_script_editor._scripts_directory import _init_scripts_directory, _search_scripts
    _init_scripts_directory()
    _search_scripts()
