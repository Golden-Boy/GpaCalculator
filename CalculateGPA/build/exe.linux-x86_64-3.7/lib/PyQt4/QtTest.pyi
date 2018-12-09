# The PEP 484 type hints stub file for the QtTest module.
#
# Generated by SIP 4.19.13
#
# Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt4.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt4 import QtGui
from PyQt4 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Support for old-style signals and slots.
QT_SIGNAL = str
QT_SLOT = str


class QTest(sip.simplewrapper):

    class MouseAction(int): ...
    MousePress = ... # type: 'QTest.MouseAction'
    MouseRelease = ... # type: 'QTest.MouseAction'
    MouseClick = ... # type: 'QTest.MouseAction'
    MouseDClick = ... # type: 'QTest.MouseAction'
    MouseMove = ... # type: 'QTest.MouseAction'

    class KeyAction(int): ...
    Press = ... # type: 'QTest.KeyAction'
    Release = ... # type: 'QTest.KeyAction'
    Click = ... # type: 'QTest.KeyAction'

    def qWaitForWindowShown(self, window: QtGui.QWidget) -> bool: ...
    def qWait(self, ms: int) -> None: ...
    def mouseEvent(self, action: 'QTest.MouseAction', widget: QtGui.QWidget, button: QtCore.Qt.MouseButton, stateKey: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier], pos: QtCore.QPoint, delay: int = ...) -> None: ...
    def mouseRelease(self, widget: QtGui.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    def mousePress(self, widget: QtGui.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    def mouseMove(self, widget: QtGui.QWidget, pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    def mouseDClick(self, widget: QtGui.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    def mouseClick(self, widget: QtGui.QWidget, button: QtCore.Qt.MouseButton, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., pos: QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyRelease(self, widget: QtGui.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyRelease(self, widget: QtGui.QWidget, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyPress(self, widget: QtGui.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyPress(self, widget: QtGui.QWidget, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyEvent(self, action: 'QTest.KeyAction', widget: QtGui.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyEvent(self, action: 'QTest.KeyAction', widget: QtGui.QWidget, ascii: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    def keyClicks(self, widget: QtGui.QWidget, sequence: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyClick(self, widget: QtGui.QWidget, key: QtCore.Qt.Key, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @typing.overload
    def keyClick(self, widget: QtGui.QWidget, key: str, modifier: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    def qSleep(self, ms: int) -> None: ...
