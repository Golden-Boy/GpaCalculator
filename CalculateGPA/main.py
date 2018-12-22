'''
Created by Justice Jacobs from FarBeyondAverage
Grade Point Average Calculator

'''

from PyQt4 import QtGui
from PyQt4.QtGui import *

import sys # required for argv
import CalcGUI # PyQt User Interface

class CalculateApp(QtGui.QMainWindow, CalcGUI.Ui_MainWindow):
	def __init__(self):
		super().__init__() # allows passed in classes to handle inherited attributes
		self.setupUi(self)
		self.setWindowTitle("Grade Calculator")
		self.calcBtn.clicked.connect(self.calculate)

		self.pushButton.clicked.connect(self.click_count)
		self.pushButton_2.clicked.connect(self.output)
		self.exitBtn.clicked.connect(self.exit)

		self.lineEdit.setValidator(QDoubleValidator(.99, 99.99, 3)) # restricts user input(i.e. xx.xxx)
		self.lineEdit_2.setValidator(QDoubleValidator(.99, 99.99, 3))
		self.lineEdit_3.setValidator(QDoubleValidator(.99, 99.99, 3))


		#self.comboBox = QtGui.QComboBox(self.formLayoutWidget_3)
		#self.formLayout_3.setWidget(1, QtGui.QFormLayout.SpanningRole, self.comboBox)
		#self.comboBox.setCurrentIndex(1)

		self.count = 0


	def exit(self): 
		self.close()


	def calculate(self):

		if self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit.text():

			desiredGrade = self.lineEdit_2.text()
			currentGrade = self.lineEdit_3.text()
			weightOfGrade = self.lineEdit.text()

			requiredGrade = ((((float(desiredGrade) / 100.0) - ((1 - float(weightOfGrade) / 100.0) * (float(currentGrade) / 100.0))) / (float(weightOfGrade) / 100.0))) * 100.0 # calculate final grade required

			print(self.textEdit.append('You would need a {:.2f}% to get a {}%'.format(float(requiredGrade), self.lineEdit_2.text())))
		else:
			print(self.textEdit.append("Please fill in all information to get a final grade"))



	def click_count(self):
		self.count += 1


	def output(self):
		pass


	
def main():
	app = QtGui.QApplication(sys.argv)
	form = CalculateApp()
	form.show()
	app.exec_() # required to run app


if __name__ == '__main__':
	main()
