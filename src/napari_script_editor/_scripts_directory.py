import os
from napari_tools_menu import register_action
from ._utils import write_text_file

CODE_TEMPLATE = """# This is a template script for the napari-script-editor.
# See this folder for more examples:
# https://github.com/haesleinhuepf/napari-script-editor/tree/main/example_scripts
import napari
if 'viewer' not in globals():
    viewer = napari.Viewer()
print("Hello world, napari has", len(viewer.layers), "layers")
"""

def _init_scripts_directory():
    """
    Sets up the <home>/.napari-scripts folder. If it doesn't exist, it puts a template python file there.
    """
    home_dir = os.path.expanduser('~')
    sub_dir = "/.napari-scripts/"
    scripts_dir = home_dir + sub_dir

    if not os.path.isdir(scripts_dir):
        os.mkdir(scripts_dir)

    if not os.path.isdir(scripts_dir + _new_template_filename()):
        write_text_file(scripts_dir + _new_template_filename(), CODE_TEMPLATE)

    return scripts_dir

def _new_template_filename():
    return '.new_template.py'

def _search_scripts():
    """
    Searches scripts in the <home>/.napari-scripts folder and attaches them to the Tools > Scripts menu as actions
    """
    file_list = os.listdir(_init_scripts_directory())
    files = [file for file in file_list if file.endswith(".py") and not file.startswith(".")]

    for i in files:
        _register_menu(_init_scripts_directory() + i)

def _register_menu(filename):
    """
    Adds a specific python file to the Tools > Scripts menu
    """
    with open(filename) as f:
        lines = f.readlines()
    code = "\n".join(lines)

    menu = filename.replace("\\", "/").split("/")[-1].replace("_", " ").replace(".py", "")

    def callback(viewer):
        _exec_code(code, viewer)

    register_action(callback, "Scripts > " + menu)

def _exec_code(code, viewer):
    """
    Executes given code and provides the viewer as global variable to that code.
    """
    globs = {"viewer": viewer}
    exec(code, globs)
