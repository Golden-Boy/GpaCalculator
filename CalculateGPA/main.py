'''
Created by Justice Jacobs from FarBeyondAverage

'''

from PyQt4 import QtGui
#from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys # required for argv
import CalcGUI # PyQt User Interface

class CalculateApp(QtGui.QMainWindow, CalcGUI.Ui_MainWindow):
	def __init__(self):
		super().__init__() # allows passed in classes to handle specific attributes
		self.setupUi(self)
		self.setWindowTitle("Grade Calculator")
		self.calcBtn.clicked.connect(self.calculate)
		self.exitBtn.clicked.connect(self.exit)
		self.lineEdit.setValidator(QDoubleValidator(.99, 99.99, 3))
		self.lineEdit_2.setValidator(QDoubleValidator(.99, 99.99, 3))
		self.lineEdit_3.setValidator(QDoubleValidator(.99, 99.99, 3))


	def exit(self): 
		self.close()


	def calculate(self):

		if self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit.text():

			desiredGrade = self.lineEdit_2.text()
			currentGrade = self.lineEdit_3.text()
			weightOfGrade = self.lineEdit.text()

			requiredGrade = ((((float(desiredGrade) / 100.0) - ((1 - float(weightOfGrade) / 100.0) * (float(currentGrade) / 100.0))) / (float(weightOfGrade) / 100.0))) * 100.0

			print(self.textEdit.append('You would need a {:.2f}% to get a {}%'.format(float(requiredGrade), self.lineEdit_2.text())))
		else:
			print(self.textEdit.append("Please fill in all information"))
	
def main():
	app = QtGui.QApplication(sys.argv)
	form = CalculateApp()
	form.show()
	app.exec_() # required to run app


if __name__ == '__main__':
	main()
