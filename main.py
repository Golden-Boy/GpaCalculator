from PyQt4 import QtGui
import sys
import CalcGUI

class CalculateApp(QtGui.QMainWindow, CalcGUI.Ui_MainWindow):
	def __init__(self):
		super().__init__()