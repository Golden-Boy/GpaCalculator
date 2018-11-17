# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GPAUserInterface.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(929, 512)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(27, 28, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 28, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 139, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.calcTab = QtGui.QWidget()
        self.calcTab.setObjectName(_fromUtf8("calcTab"))
        self.tabWidget.addTab(self.calcTab, _fromUtf8(""))
        self.aboutTab = QtGui.QWidget()
        self.aboutTab.setObjectName(_fromUtf8("aboutTab"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.aboutTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 911, 401))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.horizontalLayoutWidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.tabWidget.addTab(self.aboutTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calcTab), _translate("MainWindow", "Calculate", None))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "This is a product created and developed by Justice Jacobs from FarBeyondAverage.\n"
"\n"
"If you would like more information and/or would like to contact the developer, the following links will be useful:\n"
"\n"
"Developer Github\n"
"http://www.github.com/golden-boy\n"
"\n"
"Developer Website \n"
"http://www.FarBeyondAverage.com\n"
"\n"
"Online GPA Calculator\n"
"<Place Github Pages URL to online gpa calculator>\n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), _translate("MainWindow", "About", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

