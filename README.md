# napari-script-editor

[![License](https://img.shields.io/pypi/l/napari-script-editor.svg?color=green)](https://github.com/haesleinhuepf/napari-script-editor/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-script-editor.svg?color=green)](https://pypi.org/project/napari-script-editor)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-script-editor.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/napari-script-editor/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/napari-script-editor/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/napari-script-editor/branch/main/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/napari-script-editor)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-script-editor)](https://napari-hub.org/plugins/napari-script-editor)

A python script editor for napari based on [haesleinhuepf's fork of PyQode](https://github.com/haesleinhuepf/pyqode.core).

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

![](https://github.com/haesleinhuepf/napari-script-editor/raw/main/docs/screenshot2.png)

## Usage

Start the script editor from the menu `Tools > Scripts > Script Editor`. Use the auto-completion while typing, 
check out the [napari tutorials](https://napari.org/tutorials/) and the
[example scripts](https://github.com/haesleinhuepf/napari-script-editor/tree/main/example_scripts). 
Use the `Run` button to execute a script.

![](https://github.com/haesleinhuepf/napari-script-editor/raw/main/docs/type_and_run_screencast.gif)

If you save the script to the folder ".napari-scripts" in your home directory, you will find the script in the 
`Tools > Scripts` menu in napari. You can then also start it from there.

![](https://github.com/haesleinhuepf/napari-script-editor/raw/main/docs/run_from_menu_screencast.gif)

Note: If you have scripts, that might be useful to others, please send them as 
[pull-request](https://github.com/haesleinhuepf/napari-script-editor/pulls) to the examples in 
repository or share them in any other way that suits you.

## Installation
* Get a python environment, e.g. via [mini-conda](https://docs.conda.io/en/latest/miniconda.html). 
  If you never used python/conda environments before, please follow the instructions 
  [here](https://mpicbg-scicomp.github.io/ipf_howtoguides/guides/Python_Conda_Environments) first.
* Install [napari](https://github.com/napari/napari) using conda. 

```
conda install -c conda-forge napari
```

Afterwards, install `napari-script-editor` using pip:

```
pip install napari-script-editor
```

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-script-editor" is free and open source software

## Known issues

* Sometimes, the script editor thinks, the file has been changed on disk and asks to reload it.

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/haesleinhuepf/napari-script-editor/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
