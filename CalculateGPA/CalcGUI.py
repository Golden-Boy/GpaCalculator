# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestUI.ui'
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
        MainWindow.resize(900, 400)
        MainWindow.setMinimumSize(QtCore.QSize(900, 400))
        MainWindow.setMaximumSize(QtCore.QSize(900, 400))
        MainWindow.setBaseSize(QtCore.QSize(900, 400))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 271, 301))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.calcBtn = QtGui.QPushButton(self.tab)
        self.calcBtn.setGeometry(QtCore.QRect(340, 250, 211, 30))
        self.calcBtn.setObjectName(_fromUtf8("calcBtn"))
        self.exitBtn = QtGui.QPushButton(self.tab)
        self.exitBtn.setGeometry(QtCore.QRect(610, 250, 171, 31))
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(620, 40, 211, 30))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(620, 110, 211, 30))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(620, 180, 211, 30))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.formLayoutWidget = QtGui.QWidget(self.tab_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(710, 0, 171, 291))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lineEdit_4 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setInputMask(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.lineEdit_4)
        self.lineEdit_5 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lineEdit_5)
        self.lineEdit_6 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.lineEdit_6)
        self.lineEdit_7 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.lineEdit_7)
        self.lineEdit_9 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.lineEdit_9)
        self.lineEdit_8 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.lineEdit_8)
        self.lineEdit_10 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.lineEdit_10)
        self.formLayoutWidget_2 = QtGui.QWidget(self.tab_3)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(450, 0, 160, 301))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.spinBox = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(6)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.spinBox)
        self.spinBox_2 = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(6)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.spinBox_2)
        self.spinBox_3 = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(6)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.SpanningRole, self.spinBox_3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.tab_4)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 33))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.calcBtn.setText(_translate("MainWindow", "Calculate", None))
        self.exitBtn.setText(_translate("MainWindow", "Exit", None))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Current Grade (e.g 70.00%)", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Target Grade (e.g 75.00%)", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Exam Weight (e.g 20.00%)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Final Grade Calculator", None))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Grade Point Average Calculator", None))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "Final Grade Calculator Usage:\n"
"\n"
"All fields must be filled out for the \'calculate\' button to work\n"
"\n"
"Current Grade = Current grade, as a percentage, in the course\n"
"Final Grade = Final grade, as a percentage, in the course\n"
"Weight = The weight, as a percentage, of the test/quiz\n"
"\n"
"Grade Point Average Calculator\n"
"\n"
"\n"
"\n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Help", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "About", None))

