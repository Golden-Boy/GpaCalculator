# The PEP 484 type hints stub file for the QtOpenGL module.
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


class QGL(sip.simplewrapper):

    class FormatOption(int): ...
    DoubleBuffer = ... # type: 'QGL.FormatOption'
    DepthBuffer = ... # type: 'QGL.FormatOption'
    Rgba = ... # type: 'QGL.FormatOption'
    AlphaChannel = ... # type: 'QGL.FormatOption'
    AccumBuffer = ... # type: 'QGL.FormatOption'
    StencilBuffer = ... # type: 'QGL.FormatOption'
    StereoBuffers = ... # type: 'QGL.FormatOption'
    DirectRendering = ... # type: 'QGL.FormatOption'
    HasOverlay = ... # type: 'QGL.FormatOption'
    SampleBuffers = ... # type: 'QGL.FormatOption'
    SingleBuffer = ... # type: 'QGL.FormatOption'
    NoDepthBuffer = ... # type: 'QGL.FormatOption'
    ColorIndex = ... # type: 'QGL.FormatOption'
    NoAlphaChannel = ... # type: 'QGL.FormatOption'
    NoAccumBuffer = ... # type: 'QGL.FormatOption'
    NoStencilBuffer = ... # type: 'QGL.FormatOption'
    NoStereoBuffers = ... # type: 'QGL.FormatOption'
    IndirectRendering = ... # type: 'QGL.FormatOption'
    NoOverlay = ... # type: 'QGL.FormatOption'
    NoSampleBuffers = ... # type: 'QGL.FormatOption'
    DeprecatedFunctions = ... # type: 'QGL.FormatOption'
    NoDeprecatedFunctions = ... # type: 'QGL.FormatOption'

    class FormatOptions(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QGL.FormatOptions', 'QGL.FormatOption']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QGL.FormatOptions') -> None: ...

        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QGL.FormatOptions': ...
        def __int__(self) -> int: ...

    def setPreferredPaintEngine(self, engineType: QtGui.QPaintEngine.Type) -> None: ...


class QGLFormat(sip.simplewrapper):

    class OpenGLContextProfile(int): ...
    NoProfile = ... # type: 'QGLFormat.OpenGLContextProfile'
    CoreProfile = ... # type: 'QGLFormat.OpenGLContextProfile'
    CompatibilityProfile = ... # type: 'QGLFormat.OpenGLContextProfile'

    class OpenGLVersionFlag(int): ...
    OpenGL_Version_None = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_1_1 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_1_2 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_1_3 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_1_4 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_1_5 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_2_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_2_1 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_3_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_3_1 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_3_2 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_3_3 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_Version_4_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_ES_Common_Version_1_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_ES_CommonLite_Version_1_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_ES_Common_Version_1_1 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_ES_CommonLite_Version_1_1 = ... # type: 'QGLFormat.OpenGLVersionFlag'
    OpenGL_ES_Version_2_0 = ... # type: 'QGLFormat.OpenGLVersionFlag'

    class OpenGLVersionFlags(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QGLFormat.OpenGLVersionFlags', 'QGLFormat.OpenGLVersionFlag']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QGLFormat.OpenGLVersionFlags') -> None: ...

        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QGLFormat.OpenGLVersionFlags': ...
        def __int__(self) -> int: ...

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, options: typing.Union[QGL.FormatOptions, QGL.FormatOption], plane: int = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGLFormat') -> None: ...

    def profile(self) -> 'QGLFormat.OpenGLContextProfile': ...
    def setProfile(self, profile: 'QGLFormat.OpenGLContextProfile') -> None: ...
    def minorVersion(self) -> int: ...
    def majorVersion(self) -> int: ...
    def setVersion(self, major: int, minor: int) -> None: ...
    @staticmethod
    def openGLVersionFlags() -> 'QGLFormat.OpenGLVersionFlags': ...
    def swapInterval(self) -> int: ...
    def setSwapInterval(self, interval: int) -> None: ...
    def blueBufferSize(self) -> int: ...
    def setBlueBufferSize(self, size: int) -> None: ...
    def greenBufferSize(self) -> int: ...
    def setGreenBufferSize(self, size: int) -> None: ...
    def redBufferSize(self) -> int: ...
    def setRedBufferSize(self, size: int) -> None: ...
    def sampleBuffers(self) -> bool: ...
    def hasOverlay(self) -> bool: ...
    def directRendering(self) -> bool: ...
    def stereo(self) -> bool: ...
    def stencil(self) -> bool: ...
    def accum(self) -> bool: ...
    def alpha(self) -> bool: ...
    def rgba(self) -> bool: ...
    def depth(self) -> bool: ...
    def doubleBuffer(self) -> bool: ...
    @staticmethod
    def hasOpenGLOverlays() -> bool: ...
    @staticmethod
    def hasOpenGL() -> bool: ...
    @staticmethod
    def setDefaultOverlayFormat(f: 'QGLFormat') -> None: ...
    @staticmethod
    def defaultOverlayFormat() -> 'QGLFormat': ...
    @staticmethod
    def setDefaultFormat(f: 'QGLFormat') -> None: ...
    @staticmethod
    def defaultFormat() -> 'QGLFormat': ...
    def testOption(self, opt: typing.Union[QGL.FormatOptions, QGL.FormatOption]) -> bool: ...
    def setOption(self, opt: typing.Union[QGL.FormatOptions, QGL.FormatOption]) -> None: ...
    def setPlane(self, plane: int) -> None: ...
    def plane(self) -> int: ...
    def setOverlay(self, enable: bool) -> None: ...
    def setDirectRendering(self, enable: bool) -> None: ...
    def setStereo(self, enable: bool) -> None: ...
    def setStencil(self, enable: bool) -> None: ...
    def setAccum(self, enable: bool) -> None: ...
    def setAlpha(self, enable: bool) -> None: ...
    def setRgba(self, enable: bool) -> None: ...
    def setDepth(self, enable: bool) -> None: ...
    def setDoubleBuffer(self, enable: bool) -> None: ...
    def samples(self) -> int: ...
    def setSamples(self, numSamples: int) -> None: ...
    def setSampleBuffers(self, enable: bool) -> None: ...
    def stencilBufferSize(self) -> int: ...
    def setStencilBufferSize(self, size: int) -> None: ...
    def alphaBufferSize(self) -> int: ...
    def setAlphaBufferSize(self, size: int) -> None: ...
    def accumBufferSize(self) -> int: ...
    def setAccumBufferSize(self, size: int) -> None: ...
    def depthBufferSize(self) -> int: ...
    def setDepthBufferSize(self, size: int) -> None: ...


class QGLContext(sip.wrapper):

    class BindOption(int): ...
    NoBindOption = ... # type: 'QGLContext.BindOption'
    InvertedYBindOption = ... # type: 'QGLContext.BindOption'
    MipmapBindOption = ... # type: 'QGLContext.BindOption'
    PremultipliedAlphaBindOption = ... # type: 'QGLContext.BindOption'
    LinearFilteringBindOption = ... # type: 'QGLContext.BindOption'
    DefaultBindOption = ... # type: 'QGLContext.BindOption'

    class BindOptions(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QGLContext.BindOptions', 'QGLContext.BindOption']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QGLContext.BindOptions') -> None: ...

        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QGLContext.BindOptions': ...
        def __int__(self) -> int: ...

    def __init__(self, format: QGLFormat, device: QtGui.QPaintDevice) -> None: ...

    @staticmethod
    def areSharing(context1: 'QGLContext', context2: 'QGLContext') -> bool: ...
    def generateFontDisplayLists(self, fnt: QtGui.QFont, listBase: int) -> None: ...
    def setInitialized(self, on: bool) -> None: ...
    def initialized(self) -> bool: ...
    def setWindowCreated(self, on: bool) -> None: ...
    def windowCreated(self) -> bool: ...
    def deviceIsPixmap(self) -> bool: ...
    def chooseContext(self, shareContext: typing.Optional['QGLContext'] = ...) -> bool: ...
    @staticmethod
    def currentContext() -> 'QGLContext': ...
    def overlayTransparentColor(self) -> QtGui.QColor: ...
    def device(self) -> QtGui.QPaintDevice: ...
    def getProcAddress(self, proc: str) -> sip.voidptr: ...
    @staticmethod
    def textureCacheLimit() -> int: ...
    @staticmethod
    def setTextureCacheLimit(size: int) -> None: ...
    def deleteTexture(self, tx_id: int) -> None: ...
    def chooseVisual(self) -> sip.voidptr: ...
    @typing.overload
    def drawTexture(self, target: QtCore.QRectF, textureId: int, textureTarget: int = ...) -> None: ...
    @typing.overload
    def drawTexture(self, point: typing.Union[QtCore.QPointF, QtCore.QPoint], textureId: int, textureTarget: int = ...) -> None: ...
    @typing.overload
    def bindTexture(self, image: QtGui.QImage, target: int = ..., format: int = ...) -> int: ...
    @typing.overload
    def bindTexture(self, pixmap: QtGui.QPixmap, target: int = ..., format: int = ...) -> int: ...
    @typing.overload
    def bindTexture(self, fileName: str) -> int: ...
    @typing.overload
    def bindTexture(self, image: QtGui.QImage, target: int, format: int, options: 'QGLContext.BindOptions') -> int: ...
    @typing.overload
    def bindTexture(self, pixmap: QtGui.QPixmap, target: int, format: int, options: 'QGLContext.BindOptions') -> int: ...
    def swapBuffers(self) -> None: ...
    def doneCurrent(self) -> None: ...
    def makeCurrent(self) -> None: ...
    def setFormat(self, format: QGLFormat) -> None: ...
    def requestedFormat(self) -> QGLFormat: ...
    def format(self) -> QGLFormat: ...
    def reset(self) -> None: ...
    def isSharing(self) -> bool: ...
    def isValid(self) -> bool: ...
    def create(self, shareContext: typing.Optional['QGLContext'] = ...) -> bool: ...


class QGLWidget(QtGui.QWidget):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtGui.QWidget] = ..., shareWidget: typing.Optional['QGLWidget'] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...
    @typing.overload
    def __init__(self, context: QGLContext, parent: typing.Optional[QtGui.QWidget] = ..., shareWidget: typing.Optional['QGLWidget'] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...
    @typing.overload
    def __init__(self, format: QGLFormat, parent: typing.Optional[QtGui.QWidget] = ..., shareWidget: typing.Optional['QGLWidget'] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None: ...

    def fontDisplayListBase(self, font: QtGui.QFont, listBase: int = ...) -> int: ...
    def glDraw(self) -> None: ...
    def glInit(self) -> None: ...
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None: ...
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None: ...
    def autoBufferSwap(self) -> bool: ...
    def setAutoBufferSwap(self, on: bool) -> None: ...
    def paintOverlayGL(self) -> None: ...
    def resizeOverlayGL(self, w: int, h: int) -> None: ...
    def initializeOverlayGL(self) -> None: ...
    def paintGL(self) -> None: ...
    def resizeGL(self, w: int, h: int) -> None: ...
    def initializeGL(self) -> None: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def updateOverlayGL(self) -> None: ...
    def updateGL(self) -> None: ...
    def deleteTexture(self, tx_id: int) -> None: ...
    @typing.overload
    def drawTexture(self, target: QtCore.QRectF, textureId: int, textureTarget: int = ...) -> None: ...
    @typing.overload
    def drawTexture(self, point: typing.Union[QtCore.QPointF, QtCore.QPoint], textureId: int, textureTarget: int = ...) -> None: ...
    @typing.overload
    def bindTexture(self, image: QtGui.QImage, target: int = ..., format: int = ...) -> int: ...
    @typing.overload
    def bindTexture(self, pixmap: QtGui.QPixmap, target: int = ..., format: int = ...) -> int: ...
    @typing.overload
    def bindTexture(self, fileName: str) -> int: ...
    @typing.overload
    def bindTexture(self, image: QtGui.QImage, target: int, format: int, options: QGLContext.BindOptions) -> int: ...
    @typing.overload
    def bindTexture(self, pixmap: QtGui.QPixmap, target: int, format: int, options: QGLContext.BindOptions) -> int: ...
    def paintEngine(self) -> QtGui.QPaintEngine: ...
    @typing.overload
    def renderText(self, x: int, y: int, str: str, font: QtGui.QFont = ..., listBase: int = ...) -> None: ...
    @typing.overload
    def renderText(self, x: float, y: float, z: float, str: str, font: QtGui.QFont = ..., listBase: int = ...) -> None: ...
    def setColormap(self, map: 'QGLColormap') -> None: ...
    def colormap(self) -> 'QGLColormap': ...
    def setMouseTracking(self, enable: bool) -> None: ...
    @staticmethod
    def convertToGLFormat(img: QtGui.QImage) -> QtGui.QImage: ...
    def overlayContext(self) -> QGLContext: ...
    def makeOverlayCurrent(self) -> None: ...
    def grabFrameBuffer(self, withAlpha: bool = ...) -> QtGui.QImage: ...
    def renderPixmap(self, width: int = ..., height: int = ..., useContext: bool = ...) -> QtGui.QPixmap: ...
    def setContext(self, context: QGLContext, shareContext: typing.Optional[QGLContext] = ..., deleteOldContext: bool = ...) -> None: ...
    def context(self) -> QGLContext: ...
    def setFormat(self, format: QGLFormat) -> None: ...
    def format(self) -> QGLFormat: ...
    def swapBuffers(self) -> None: ...
    def doubleBuffer(self) -> bool: ...
    def doneCurrent(self) -> None: ...
    def makeCurrent(self) -> None: ...
    def isSharing(self) -> bool: ...
    def isValid(self) -> bool: ...
    def qglClearColor(self, c: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def qglColor(self, c: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...


class QGLBuffer(sip.simplewrapper):

    class UsagePattern(int): ...
    StreamDraw = ... # type: 'QGLBuffer.UsagePattern'
    StreamRead = ... # type: 'QGLBuffer.UsagePattern'
    StreamCopy = ... # type: 'QGLBuffer.UsagePattern'
    StaticDraw = ... # type: 'QGLBuffer.UsagePattern'
    StaticRead = ... # type: 'QGLBuffer.UsagePattern'
    StaticCopy = ... # type: 'QGLBuffer.UsagePattern'
    DynamicDraw = ... # type: 'QGLBuffer.UsagePattern'
    DynamicRead = ... # type: 'QGLBuffer.UsagePattern'
    DynamicCopy = ... # type: 'QGLBuffer.UsagePattern'

    class Type(int): ...
    VertexBuffer = ... # type: 'QGLBuffer.Type'
    IndexBuffer = ... # type: 'QGLBuffer.Type'
    PixelPackBuffer = ... # type: 'QGLBuffer.Type'
    PixelUnpackBuffer = ... # type: 'QGLBuffer.Type'

    class Access(int): ...
    ReadOnly = ... # type: 'QGLBuffer.Access'
    WriteOnly = ... # type: 'QGLBuffer.Access'
    ReadWrite = ... # type: 'QGLBuffer.Access'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, type: 'QGLBuffer.Type') -> None: ...
    @typing.overload
    def __init__(self, other: 'QGLBuffer') -> None: ...

    def unmap(self) -> bool: ...
    def map(self, access: 'QGLBuffer.Access') -> sip.voidptr: ...
    @typing.overload
    def allocate(self, data: sip.voidptr, count: int) -> None: ...
    @typing.overload
    def allocate(self, count: int) -> None: ...
    def write(self, offset: int, data: sip.voidptr, count: int) -> None: ...
    def read(self, offset: int, data: sip.voidptr, count: int) -> bool: ...
    def size(self) -> int: ...
    def bufferId(self) -> int: ...
    @typing.overload
    def release(self) -> None: ...
    @typing.overload
    @staticmethod
    def release(type: 'QGLBuffer.Type') -> None: ...
    def bind(self) -> bool: ...
    def destroy(self) -> None: ...
    def isCreated(self) -> bool: ...
    def create(self) -> bool: ...
    def setUsagePattern(self, value: 'QGLBuffer.UsagePattern') -> None: ...
    def usagePattern(self) -> 'QGLBuffer.UsagePattern': ...
    def type(self) -> 'QGLBuffer.Type': ...


class QGLColormap(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QGLColormap') -> None: ...

    def setHandle(self, ahandle: int) -> None: ...
    def handle(self) -> int: ...
    def findNearest(self, color: int) -> int: ...
    def find(self, color: int) -> int: ...
    def entryColor(self, idx: int) -> QtGui.QColor: ...
    def entryRgb(self, idx: int) -> int: ...
    @typing.overload
    def setEntry(self, idx: int, color: int) -> None: ...
    @typing.overload
    def setEntry(self, idx: int, color: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def setEntries(self, colors: typing.List[int], base: int = ...) -> None: ...
    def size(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def detach(self) -> None: ...


class QGLFramebufferObject(QtGui.QPaintDevice):

    class Attachment(int): ...
    NoAttachment = ... # type: 'QGLFramebufferObject.Attachment'
    CombinedDepthStencil = ... # type: 'QGLFramebufferObject.Attachment'
    Depth = ... # type: 'QGLFramebufferObject.Attachment'

    @typing.overload
    def __init__(self, size: QtCore.QSize, target: int = ...) -> None: ...
    @typing.overload
    def __init__(self, width: int, height: int, target: int = ...) -> None: ...
    @typing.overload
    def __init__(self, size: QtCore.QSize, attachment: 'QGLFramebufferObject.Attachment', target: int = ..., internalFormat: int = ...) -> None: ...
    @typing.overload
    def __init__(self, width: int, height: int, attachment: 'QGLFramebufferObject.Attachment', target: int = ..., internalFormat: int = ...) -> None: ...
    @typing.overload
    def __init__(self, size: QtCore.QSize, format: 'QGLFramebufferObjectFormat') -> None: ...
    @typing.overload
    def __init__(self, width: int, height: int, format: 'QGLFramebufferObjectFormat') -> None: ...

    @staticmethod
    def blitFramebuffer(target: 'QGLFramebufferObject', targetRect: QtCore.QRect, source: 'QGLFramebufferObject', sourceRect: QtCore.QRect, buffers: int = ..., filter: int = ...) -> None: ...
    @staticmethod
    def hasOpenGLFramebufferBlit() -> bool: ...
    def format(self) -> 'QGLFramebufferObjectFormat': ...
    def metric(self, metric: QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    @staticmethod
    def hasOpenGLFramebufferObjects() -> bool: ...
    def handle(self) -> int: ...
    def paintEngine(self) -> QtGui.QPaintEngine: ...
    def toImage(self) -> QtGui.QImage: ...
    def size(self) -> QtCore.QSize: ...
    @typing.overload
    def drawTexture(self, target: QtCore.QRectF, textureId: int, textureTarget: int = ...) -> None: ...
    @typing.overload
    def drawTexture(self, point: typing.Union[QtCore.QPointF, QtCore.QPoint], textureId: int, textureTarget: int = ...) -> None: ...
    def texture(self) -> int: ...
    def release(self) -> bool: ...
    def isBound(self) -> bool: ...
    def bind(self) -> bool: ...
    def isValid(self) -> bool: ...
    def attachment(self) -> 'QGLFramebufferObject.Attachment': ...


class QGLFramebufferObjectFormat(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGLFramebufferObjectFormat') -> None: ...

    def mipmap(self) -> bool: ...
    def setMipmap(self, enabled: bool) -> None: ...
    def internalTextureFormat(self) -> int: ...
    def setInternalTextureFormat(self, internalTextureFormat: int) -> None: ...
    def textureTarget(self) -> int: ...
    def setTextureTarget(self, target: int) -> None: ...
    def attachment(self) -> QGLFramebufferObject.Attachment: ...
    def setAttachment(self, attachment: QGLFramebufferObject.Attachment) -> None: ...
    def samples(self) -> int: ...
    def setSamples(self, samples: int) -> None: ...


class QGLPixelBuffer(QtGui.QPaintDevice):

    @typing.overload
    def __init__(self, size: QtCore.QSize, format: QGLFormat = ..., shareWidget: typing.Optional[QGLWidget] = ...) -> None: ...
    @typing.overload
    def __init__(self, width: int, height: int, format: QGLFormat = ..., shareWidget: typing.Optional[QGLWidget] = ...) -> None: ...

    def devType(self) -> int: ...
    def metric(self, metric: QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    @staticmethod
    def hasOpenGLPbuffers() -> bool: ...
    def format(self) -> QGLFormat: ...
    def paintEngine(self) -> QtGui.QPaintEngine: ...
    def toImage(self) -> QtGui.QImage: ...
    def handle(self) -> int: ...
    def size(self) -> QtCore.QSize: ...
    def deleteTexture(self, texture_id: int) -> None: ...
    @typing.overload
    def drawTexture(self, target: QtCore.QRectF, textureId: int, textureTarget: int = ...) -> None: ...
    @typing.overload
    def drawTexture(self, point: typing.Union[QtCore.QPointF, QtCore.QPoint], textureId: int, textureTarget: int = ...) -> None: ...
    @typing.overload
    def bindTexture(self, image: QtGui.QImage, target: int = ...) -> int: ...
    @typing.overload
    def bindTexture(self, pixmap: QtGui.QPixmap, target: int = ...) -> int: ...
    @typing.overload
    def bindTexture(self, fileName: str) -> int: ...
    def updateDynamicTexture(self, texture_id: int) -> None: ...
    def releaseFromDynamicTexture(self) -> None: ...
    def bindToDynamicTexture(self, texture: int) -> bool: ...
    def generateDynamicTexture(self) -> int: ...
    def doneCurrent(self) -> bool: ...
    def makeCurrent(self) -> bool: ...
    def isValid(self) -> bool: ...


class QGLShader(QtCore.QObject):

    class ShaderTypeBit(int): ...
    Vertex = ... # type: 'QGLShader.ShaderTypeBit'
    Fragment = ... # type: 'QGLShader.ShaderTypeBit'
    Geometry = ... # type: 'QGLShader.ShaderTypeBit'

    class ShaderType(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QGLShader.ShaderType', 'QGLShader.ShaderTypeBit']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QGLShader.ShaderType') -> None: ...

        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QGLShader.ShaderType': ...
        def __int__(self) -> int: ...

    @typing.overload
    def __init__(self, type: 'QGLShader.ShaderType', parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, type: 'QGLShader.ShaderType', context: QGLContext, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    @staticmethod
    def hasOpenGLShaders(type: 'QGLShader.ShaderType', context: typing.Optional[QGLContext] = ...) -> bool: ...
    def shaderId(self) -> int: ...
    def log(self) -> str: ...
    def isCompiled(self) -> bool: ...
    def sourceCode(self) -> QtCore.QByteArray: ...
    def compileSourceFile(self, fileName: str) -> bool: ...
    @typing.overload
    def compileSourceCode(self, source: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> bool: ...
    @typing.overload
    def compileSourceCode(self, source: str) -> bool: ...
    def shaderType(self) -> 'QGLShader.ShaderType': ...


class QGLShaderProgram(QtCore.QObject):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, context: QGLContext, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    @typing.overload
    def setAttributeBuffer(self, location: int, type: int, offset: int, tupleSize: int, stride: int = ...) -> None: ...
    @typing.overload
    def setAttributeBuffer(self, name: str, type: int, offset: int, tupleSize: int, stride: int = ...) -> None: ...
    def geometryOutputType(self) -> int: ...
    def setGeometryOutputType(self, outputType: int) -> None: ...
    def geometryInputType(self) -> int: ...
    def setGeometryInputType(self, inputType: int) -> None: ...
    def geometryOutputVertexCount(self) -> int: ...
    def setGeometryOutputVertexCount(self, count: int) -> None: ...
    @staticmethod
    def hasOpenGLShaderPrograms(context: typing.Optional[QGLContext] = ...) -> bool: ...
    @typing.overload
    def setUniformValue(self, location: int, value: int) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: float) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, x: float, y: float) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, x: float, y: float, z: float) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, x: float, y: float, z: float, w: float) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QVector2D) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QVector3D) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QVector4D) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, color: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, point: QtCore.QPoint) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, point: typing.Union[QtCore.QPointF, QtCore.QPoint]) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, size: QtCore.QSize) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, size: QtCore.QSizeF) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QMatrix2x2) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QMatrix2x3) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QMatrix2x4) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QMatrix3x2) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QMatrix3x3) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QMatrix3x4) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QMatrix4x2) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QMatrix4x3) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QMatrix4x4) -> None: ...
    @typing.overload
    def setUniformValue(self, location: int, value: QtGui.QTransform) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: int) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: float) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, x: float, y: float) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, x: float, y: float, z: float) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, x: float, y: float, z: float, w: float) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QVector2D) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QVector3D) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QVector4D) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, color: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, point: QtCore.QPoint) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, point: typing.Union[QtCore.QPointF, QtCore.QPoint]) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, size: QtCore.QSize) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, size: QtCore.QSizeF) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QMatrix2x2) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QMatrix2x3) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QMatrix2x4) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QMatrix3x2) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QMatrix3x3) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QMatrix3x4) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QMatrix4x2) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QMatrix4x3) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QMatrix4x4) -> None: ...
    @typing.overload
    def setUniformValue(self, name: str, value: QtGui.QTransform) -> None: ...
    @typing.overload
    def setUniformValueArray(self, location: int, values: PYQT_SHADER_UNIFORM_VALUE_ARRAY) -> None: ...
    @typing.overload
    def setUniformValueArray(self, name: str, values: PYQT_SHADER_UNIFORM_VALUE_ARRAY) -> None: ...
    @typing.overload
    def uniformLocation(self, name: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> int: ...
    @typing.overload
    def uniformLocation(self, name: str) -> int: ...
    @typing.overload
    def disableAttributeArray(self, location: int) -> None: ...
    @typing.overload
    def disableAttributeArray(self, name: str) -> None: ...
    @typing.overload
    def enableAttributeArray(self, location: int) -> None: ...
    @typing.overload
    def enableAttributeArray(self, name: str) -> None: ...
    @typing.overload
    def setAttributeValue(self, location: int, value: float) -> None: ...
    @typing.overload
    def setAttributeValue(self, location: int, x: float, y: float) -> None: ...
    @typing.overload
    def setAttributeValue(self, location: int, x: float, y: float, z: float) -> None: ...
    @typing.overload
    def setAttributeValue(self, location: int, x: float, y: float, z: float, w: float) -> None: ...
    @typing.overload
    def setAttributeValue(self, location: int, value: QtGui.QVector2D) -> None: ...
    @typing.overload
    def setAttributeValue(self, location: int, value: QtGui.QVector3D) -> None: ...
    @typing.overload
    def setAttributeValue(self, location: int, value: QtGui.QVector4D) -> None: ...
    @typing.overload
    def setAttributeValue(self, location: int, value: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    @typing.overload
    def setAttributeValue(self, name: str, value: float) -> None: ...
    @typing.overload
    def setAttributeValue(self, name: str, x: float, y: float) -> None: ...
    @typing.overload
    def setAttributeValue(self, name: str, x: float, y: float, z: float) -> None: ...
    @typing.overload
    def setAttributeValue(self, name: str, x: float, y: float, z: float, w: float) -> None: ...
    @typing.overload
    def setAttributeValue(self, name: str, value: QtGui.QVector2D) -> None: ...
    @typing.overload
    def setAttributeValue(self, name: str, value: QtGui.QVector3D) -> None: ...
    @typing.overload
    def setAttributeValue(self, name: str, value: QtGui.QVector4D) -> None: ...
    @typing.overload
    def setAttributeValue(self, name: str, value: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    @typing.overload
    def setAttributeArray(self, location: int, values: PYQT_SHADER_ATTRIBUTE_ARRAY) -> None: ...
    @typing.overload
    def setAttributeArray(self, name: str, values: PYQT_SHADER_ATTRIBUTE_ARRAY) -> None: ...
    @typing.overload
    def attributeLocation(self, name: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> int: ...
    @typing.overload
    def attributeLocation(self, name: str) -> int: ...
    @typing.overload
    def bindAttributeLocation(self, name: typing.Union[QtCore.QByteArray, bytes, bytearray], location: int) -> None: ...
    @typing.overload
    def bindAttributeLocation(self, name: str, location: int) -> None: ...
    def programId(self) -> int: ...
    def release(self) -> None: ...
    def bind(self) -> bool: ...
    def log(self) -> str: ...
    def isLinked(self) -> bool: ...
    def link(self) -> bool: ...
    def removeAllShaders(self) -> None: ...
    def addShaderFromSourceFile(self, type: QGLShader.ShaderType, fileName: str) -> bool: ...
    @typing.overload
    def addShaderFromSourceCode(self, type: QGLShader.ShaderType, source: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> bool: ...
    @typing.overload
    def addShaderFromSourceCode(self, type: QGLShader.ShaderType, source: str) -> bool: ...
    def shaders(self) -> typing.List[QGLShader]: ...
    def removeShader(self, shader: QGLShader) -> None: ...
    def addShader(self, shader: QGLShader) -> bool: ...
