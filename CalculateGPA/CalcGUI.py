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
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 12, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 12, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 12, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
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
        self.calcBtn = QtGui.QPushButton(self.calcTab)
        self.calcBtn.setGeometry(QtCore.QRect(450, 260, 141, 31))
        self.calcBtn.setObjectName(_fromUtf8("calcBtn"))
        self.exitBtn = QtGui.QPushButton(self.calcTab)
        self.exitBtn.setGeometry(QtCore.QRect(720, 260, 141, 31))
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.tabWidget.addTab(self.calcTab, _fromUtf8(""))
        self.aboutTab = QtGui.QWidget()
        self.aboutTab.setObjectName(_fromUtf8("aboutTab"))
        self.label = QtGui.QLabel(self.aboutTab)
        self.label.setGeometry(QtCore.QRect(10, 150, 231, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.aboutTab)
        self.plainTextEdit.setGeometry(QtCore.QRect(9, 9, 901, 391))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(29, 8, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 8, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.plainTextEdit.setPalette(palette)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.devLbl = QtGui.QLabel(self.aboutTab)
        self.devLbl.setGeometry(QtCore.QRect(10, 110, 161, 18))
        self.devLbl.setOpenExternalLinks(True)
        self.devLbl.setObjectName(_fromUtf8("devLbl"))
        self.devSiteLbl = QtGui.QLabel(self.aboutTab)
        self.devSiteLbl.setGeometry(QtCore.QRect(10, 170, 161, 18))
        self.devSiteLbl.setOpenExternalLinks(True)
        self.devSiteLbl.setObjectName(_fromUtf8("devSiteLbl"))
        self.tabWidget.addTab(self.aboutTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.calcBtn.setText(_translate("MainWindow", "Calculate", None))
        self.exitBtn.setText(_translate("MainWindow", "Exit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calcTab), _translate("MainWindow", "Calculate", None))
        self.label.setText(_translate("MainWindow", "http://www.github.com/golden-boy", None))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "This is a product created and developed by Justice Jacobs from FarBeyondAverage.\n"
"\n"
"If you would like more information and/or would like to contact the developer, the following links will be useful:\n"
"\n"
"Developer Github: \n"
"\n"
"\n"
"Developer Website \n"
"\n"
"\n"
"Online GPA Calculator\n"
"<Place Github Pages URL to online gpa calculator>\n"
"", None))
        self.devLbl.setText(_translate("MainWindow", "<html><head/><a href=\"https://github.com/golden-boy\">Developer GitHub</a><body><p><br/></p></body></html>", None))
        self.devSiteLbl.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"http://FarBeyondAverage.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Developer Website</span></a></p><p><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), _translate("MainWindow", "About", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

