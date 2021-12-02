# This is a template script for the napari-script-editor.
# See this folder for more examples:
# https://github.com/haesleinhuepf/napari-script-editor/tree/main/example_scripts
import napari
if 'viewer' not in globals():
    viewer = napari.Viewer()
print("Hello world, napari has", len(viewer.layers), "layers")

import pyzo
from pyzo.util import qt
from pyzo.util.qt import QtCore, QtGui, QtWidgets
from queue import Queue, Empty

from pyzo.core import editor
from pyzo.codeeditor import CodeEditor

#ce = CodeEditor()
#ce.setAutocompleteMinChars(0)
#ce.setIndentUsishellsngSpaces(True)

class DeadEnd(QtCore.QObject):
    breakPointsChanged = QtCore.Signal(object)

    def setMainTitle(self):
        pass

    def updateBreakPoints(self):
        pass

    def getCurrentEditor(self):
        return ce

pyzo.main = DeadEnd()

from pyzo.core.main import loadIcons
loadIcons()


from pyzo.tools import ToolManager

# Instantiate tool manager
pyzo.toolManager = ToolManager()

from pyzo.core import codeparser
if pyzo.parser is None:
    pyzo.parser = codeparser.Parser()
    pyzo.parser.start()


from pyzo.core.editorTabs import EditorTabs
pyzo.editors = DeadEnd() #EditorTabs(viewer.window._qt_window)


from pyzo.core import menu

pyzo.keyMapper = menu.KeyMapper()

from pyzo.core.shell import PythonShell
a_shell = PythonShell(viewer.window._qt_window, None)



class _CallbackEventHandler(QtCore.QObject):
    """Helper class to provide the callLater function."""

    def __init__(self):
        QtCore.QObject.__init__(self)
        self.queue = Queue()

    def customEvent(self, event):
        while True:
            try:
                callback, args = self.queue.get_nowait()
            except Empty:
                break
            try:
                callback(*args)
            except Exception as why:
                print("callback failed: {}:\n{}".format(callback, why))

    def postEventWithCallback(self, callback, *args):
        self.queue.put((callback, args))
        QtWidgets.qApp.postEvent(self, QtCore.QEvent(QtCore.QEvent.User))


def callLater(callback, *args):
    """callLater(callback, *args)
    Post a callback to be called in the main thread.
    """
    print("Calling later")
    _callbackEventHandler.postEventWithCallback(callback, *args)

_callbackEventHandler = _CallbackEventHandler()
pyzo.callLater = callLater


from pyzo.core.shellStack import ShellStackWidget
pyzo.shells = ShellStackWidget(viewer.window._qt_window)
callLater(pyzo.shells.addShell)

from pyzo.codeeditor.manager import Manager

from pyzo.core.baseTextCtrl import BaseTextCtrl
class MyEditor(BaseTextCtrl):
    def processAutoComp(self, aco):
        """Processes an autocomp request using an AutoCompObject instance."""

        # Try using buffer first
        if aco.tryUsingBuffer():
            return

        # Init name to poll by remote process (can be changed!)
        nameForShell = aco.name

        # Get normal fictive namespace
        fictiveNS = pyzo.parser.getFictiveNameSpace(self)
        fictiveNS = set(fictiveNS)

        # Add names
        if not aco.name:
            # "root" names
            aco.addNames(fictiveNS)
            # imports
            importNames, importLines = pyzo.parser.getFictiveImports(self)
            aco.addNames(importNames)
        else:
            # Prepare list of class names to check out
            classNames = [aco.name]
            handleSelf = True
            # Unroll supers
            while classNames:
                className = classNames.pop(0)
                if not className:
                    continue
                if handleSelf or (className in fictiveNS):
                    # Only the self list (only first iter)
                    fictiveClass = pyzo.parser.getFictiveClass(
                        className, self, handleSelf
                    )
                    handleSelf = False
                    if fictiveClass:
                        aco.addNames(fictiveClass.members)
                        classNames.extend(fictiveClass.supers)
                else:
                    nameForShell = className
                    break

        # If there's a shell, let it finish the autocompletion
        shell = a_shell
        if shell:
            aco.name = nameForShell  # might be the same or a base class
            shell.processAutoComp(aco)
        else:
            # Otherwise we finish it ourselves
            aco.finish()






ce = MyEditor()
ce.setParser("python3")

ce.setPlainText("import napari\nviewer = napari.Viewer()\nif napari:\n    whatever()")

# for k, v in ce.__dict__.items():
#     print(k, ":  ", v)
viewer.window.add_dock_widget(ce)
ce.setParser(pyzo.config.settings.defaultStyle)
