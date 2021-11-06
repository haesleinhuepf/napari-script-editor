
def _init_scripts_directory():
    import os
    home_dir = os.path.expanduser('~')
    sub_dir = "/.napari-scripts/"

    scripts_dir = home_dir + sub_dir

    print("home:", scripts_dir)


    if not os.path.isdir(scripts_dir):
        os.mkdir(scripts_dir)

    if not os.path.isdir(scripts_dir + _new_template_filename()):
        with open(scripts_dir + _new_template_filename(), 'w') as f:
            f.write('print("Hello world")\n')

    return scripts_dir

def _new_template_filename():
    return '.new_template.py'

