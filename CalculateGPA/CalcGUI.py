# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalcGUI.ui'
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
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
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
        self.calcBtn.setGeometry(QtCore.QRect(340, 250, 171, 31))
        self.calcBtn.setObjectName(_fromUtf8("calcBtn"))
        self.exitBtn = QtGui.QPushButton(self.tab)
        self.exitBtn.setGeometry(QtCore.QRect(610, 250, 171, 31))
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.currentGrade = QtGui.QLineEdit(self.tab)
        self.currentGrade.setGeometry(QtCore.QRect(620, 40, 211, 30))
        self.currentGrade.setText(_fromUtf8(""))
        self.currentGrade.setObjectName(_fromUtf8("currentGrade"))
        self.targetGrade = QtGui.QLineEdit(self.tab)
        self.targetGrade.setGeometry(QtCore.QRect(620, 110, 211, 30))
        self.targetGrade.setText(_fromUtf8(""))
        self.targetGrade.setObjectName(_fromUtf8("targetGrade"))
        self.examWeight = QtGui.QLineEdit(self.tab)
        self.examWeight.setGeometry(QtCore.QRect(620, 180, 211, 30))
        self.examWeight.setText(_fromUtf8(""))
        self.examWeight.setObjectName(_fromUtf8("examWeight"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.formLayoutWidget = QtGui.QWidget(self.tab_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 261))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.course_4 = QtGui.QLineEdit(self.formLayoutWidget)
        self.course_4.setInputMask(_fromUtf8(""))
        self.course_4.setObjectName(_fromUtf8("course_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.course_4)
        self.course_5 = QtGui.QLineEdit(self.formLayoutWidget)
        self.course_5.setInputMask(_fromUtf8(""))
        self.course_5.setObjectName(_fromUtf8("course_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.course_5)
        self.course_6 = QtGui.QLineEdit(self.formLayoutWidget)
        self.course_6.setInputMask(_fromUtf8(""))
        self.course_6.setObjectName(_fromUtf8("course_6"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.course_6)
        self.course_7 = QtGui.QLineEdit(self.formLayoutWidget)
        self.course_7.setInputMask(_fromUtf8(""))
        self.course_7.setObjectName(_fromUtf8("course_7"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.course_7)
        self.course_8 = QtGui.QLineEdit(self.formLayoutWidget)
        self.course_8.setInputMask(_fromUtf8(""))
        self.course_8.setObjectName(_fromUtf8("course_8"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.course_8)
        self.course_9 = QtGui.QLineEdit(self.formLayoutWidget)
        self.course_9.setInputMask(_fromUtf8(""))
        self.course_9.setObjectName(_fromUtf8("course_9"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.course_9)
        self.course_10 = QtGui.QLineEdit(self.formLayoutWidget)
        self.course_10.setInputMask(_fromUtf8(""))
        self.course_10.setObjectName(_fromUtf8("course_10"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.course_10)
        self.course_11 = QtGui.QLineEdit(self.formLayoutWidget)
        self.course_11.setInputMask(_fromUtf8(""))
        self.course_11.setObjectName(_fromUtf8("course_11"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.SpanningRole, self.course_11)
        self.formLayoutWidget_2 = QtGui.QWidget(self.tab_3)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(560, 0, 91, 261))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.spinBox = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.spinBox.setMinimum(-1)
        self.spinBox.setMaximum(6)
        self.spinBox.setProperty("value", -1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.spinBox)
        self.spinBox_3 = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinBox_3.setMinimum(-1)
        self.spinBox_3.setMaximum(6)
        self.spinBox_3.setProperty("value", -1)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.SpanningRole, self.spinBox_3)
        self.spinBox_4 = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinBox_4.setMinimum(-1)
        self.spinBox_4.setMaximum(6)
        self.spinBox_4.setProperty("value", -1)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.SpanningRole, self.spinBox_4)
        self.spinBox_5 = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinBox_5.setMinimum(-1)
        self.spinBox_5.setMaximum(6)
        self.spinBox_5.setProperty("value", -1)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.SpanningRole, self.spinBox_5)
        self.spinBox_6 = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinBox_6.setMinimum(-1)
        self.spinBox_6.setMaximum(6)
        self.spinBox_6.setProperty("value", -1)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.SpanningRole, self.spinBox_6)
        self.spinBox_7 = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinBox_7.setMinimum(-1)
        self.spinBox_7.setMaximum(6)
        self.spinBox_7.setProperty("value", -1)
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.SpanningRole, self.spinBox_7)
        self.spinBox_8 = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinBox_8.setMinimum(-1)
        self.spinBox_8.setMaximum(6)
        self.spinBox_8.setProperty("value", -1)
        self.spinBox_8.setObjectName(_fromUtf8("spinBox_8"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.SpanningRole, self.spinBox_8)
        self.spinBox_2 = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.spinBox_2.setMinimum(-1)
        self.spinBox_2.setMaximum(6)
        self.spinBox_2.setProperty("value", -1)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.spinBox_2)
        self.exitBtn2 = QtGui.QPushButton(self.tab_3)
        self.exitBtn2.setGeometry(QtCore.QRect(490, 270, 161, 30))
        self.exitBtn2.setObjectName(_fromUtf8("exitBtn2"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.tab_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(760, 0, 121, 261))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.comboBox = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox.setEnabled(True)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.SpanningRole, self.comboBox)
        self.comboBox_2 = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.SpanningRole, self.comboBox_2)
        self.comboBox_3 = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox_3.setEnabled(True)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.SpanningRole, self.comboBox_3)
        self.comboBox_4 = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox_4.setEnabled(True)
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.SpanningRole, self.comboBox_4)
        self.comboBox_5 = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox_5.setEnabled(True)
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.SpanningRole, self.comboBox_5)
        self.comboBox_6 = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox_6.setEnabled(True)
        self.comboBox_6.setEditable(False)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.SpanningRole, self.comboBox_6)
        self.comboBox_7 = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox_7.setEnabled(True)
        self.comboBox_7.setEditable(False)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.SpanningRole, self.comboBox_7)
        self.comboBox_8 = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox_8.setEnabled(True)
        self.comboBox_8.setEditable(False)
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.SpanningRole, self.comboBox_8)
        self.comboBox_9 = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox_9.setEnabled(True)
        self.comboBox_9.setEditable(False)
        self.comboBox_9.setObjectName(_fromUtf8("comboBox_9"))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.SpanningRole, self.comboBox_9)
        self.calcBtn2 = QtGui.QPushButton(self.tab_3)
        self.calcBtn2.setGeometry(QtCore.QRect(300, 270, 161, 30))
        self.calcBtn2.setObjectName(_fromUtf8("calcBtn2"))
        self.textEdit_2 = QtGui.QTextEdit(self.tab_3)
        self.textEdit_2.setGeometry(QtCore.QRect(680, 270, 161, 30))
        self.textEdit_2.setMouseTracking(True)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setAcceptRichText(False)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit_21 = QtGui.QTextEdit(self.tab_4)
        self.textEdit_21.setObjectName(_fromUtf8("textEdit_21"))
        self.verticalLayout.addWidget(self.textEdit_21)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(0)
        self.comboBox_9.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.calcBtn.setText(_translate("MainWindow", "Calculate", None))
        self.exitBtn.setText(_translate("MainWindow", "Exit", None))
        self.currentGrade.setPlaceholderText(_translate("MainWindow", "Current Grade (e.g 70.00%)", None))
        self.targetGrade.setPlaceholderText(_translate("MainWindow", "Target Grade (e.g 75.00%)", None))
        self.examWeight.setPlaceholderText(_translate("MainWindow", "Exam Weight (e.g 20.00%)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Final Grade Calculator", None))
        self.course_4.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.course_5.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.course_6.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.course_7.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.course_8.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.course_9.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.course_10.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.course_11.setPlaceholderText(_translate("MainWindow", "e.g. course", None))
        self.exitBtn2.setText(_translate("MainWindow", "Exit", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "-", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "A", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "C", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "D", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "F", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "-", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "A", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "C", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "D", None))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "F", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "-", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "A", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "C", None))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "D", None))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "F", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "-", None))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "A", None))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "C", None))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "D", None))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "F", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "-", None))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "A", None))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "C", None))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "D", None))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "F", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "-", None))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "A", None))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "C", None))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "D", None))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "F", None))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "-", None))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "A", None))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "C", None))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "D", None))
        self.comboBox_7.setItemText(5, _translate("MainWindow", "F", None))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "-", None))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "A", None))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "C", None))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "D", None))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "F", None))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "-", None))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "A", None))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "B", None))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "C", None))
        self.comboBox_9.setItemText(4, _translate("MainWindow", "D", None))
        self.comboBox_9.setItemText(5, _translate("MainWindow", "F", None))
        self.calcBtn2.setText(_translate("MainWindow", "Calculate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Grade Point Average Calculator", None))
        self.textEdit_21.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Zekton\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Final Grade Calculator Usage</span>:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All fields must be filled out for the \'calculate\' button to work</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Current Grade = Current grade, as a percentage, in the course</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Final Grade = Final grade, as a percentage, in the course</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Weight = The weight, as a percentage, on the test/quiz</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Grade Point Average Calculator Usage:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Course Name(optional) = Name of Course</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Credit Hours = Credit Hours of Course</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grade Received = Final grade in Course</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NOTE: Credit Hour(s) and Grade Received both must be filled out for a calculation.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Help", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Zekton\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This is a product created and developed by Justice Jacobs by FarBeyondAverage.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">If you would like more information and/or would like to contact the developer, the following links will be useful:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/golden-boy\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Developer Github</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.farbeyondaverage.com/\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Developer Website</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; text-decoration: underline; color:#0000ff;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "About", None))

