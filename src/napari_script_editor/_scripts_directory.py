import os
from napari_tools_menu import register_action

CODE_TEMPLATE = """import napari
if 'viewer' not in globals():
    viewer = napari.Viewer()
print("Hello world, napari has", len(viewer.layers), "layers")
"""


def _init_scripts_directory():

    home_dir = os.path.expanduser('~')
    sub_dir = "/.napari-scripts/"

    scripts_dir = home_dir + sub_dir

    print("home:", scripts_dir)


    if not os.path.isdir(scripts_dir):
        os.mkdir(scripts_dir)

    if not os.path.isdir(scripts_dir + _new_template_filename()):
        with open(scripts_dir + _new_template_filename(), 'w') as f:
            f.write(CODE_TEMPLATE)

    return scripts_dir

def _new_template_filename():
    return '.new_template.py'

def _search_scripts():
    print("Searching for menus")
    file_list = os.listdir(_init_scripts_directory())
    print("FL", file_list)
    files = [file for file in file_list if file.endswith(".py") and not file.startswith(".")]
    print("FL2", files)

    for i in files:
        print(i)
        _register_menu(_init_scripts_directory() + i)

def _register_menu(filename):

    with open(filename) as f:
        lines = f.readlines()
    code = "\n".join(lines)

    menu = filename.replace("\\", "/").split("/")[-1].replace("_", " ").replace(".py", "")

    def callback(viewer):
        _exec_code(code, viewer)

    print("REG", menu)

    register_action(callback, "Scripts > " + menu)

def _exec_code(code, viewer):
    globs = {"viewer": viewer}
    exec(code, globs)
