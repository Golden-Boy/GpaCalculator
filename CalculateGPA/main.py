'''
Created by Justice Jacobs from FarBeyondAverage
Grade Point Average Calculator

'''

from PyQt4 import QtGui
from PyQt4.QtGui import *

import sys
import CalcGUI # PyQt User Interface

class CalculateApp(QtGui.QMainWindow, CalcGUI.Ui_MainWindow):
	def __init__(self):
		super().__init__() # allows passed in classes to handle inherited attributes
		self.setupUi(self)
		self.setWindowTitle("Grade Calculator")
		self.calcBtn.clicked.connect(self.FinalGradecalculate)

		self.exitBtn.clicked.connect(self.exit)
		self.exitBtn2.clicked.connect(self.exit)
		self.calcBtn2.clicked.connect(self.GpaAverageCalculate)

		self.examWeight.setValidator(QDoubleValidator(.99, 99.99, 2)) # restricts user input(i.e. xx.xx)
		self.targetGrade.setValidator(QDoubleValidator(.99, 99.99, 2))
		self.currentGrade.setValidator(QDoubleValidator(.99, 99.99, 2))

		#self.comboBox
	def FinalGradecalculate(self):

		if self.targetGrade.text() and self.currentGrade.text() and self.examWeight.text(): # if all 3 fields are filled

			targetGrade = self.targetGrade.text()
			currentGrade = self.currentGrade.text() # store user input
			examWeight = self.examWeight.text()

			expectedGrade = ((((float(targetGrade) / 100.0) - ((1 - float(examWeight) / 100.0) * (float(currentGrade) / 100.0))) / (float(examWeight) / 100.0))) * 100.0 # calculate final grade required

			print(self.textEdit.append('You would need a {:.2f}% to get a {}%'.format(float(expectedGrade), self.targetGrade.text())))
		else:
			print(self.textEdit.append("Please fill in all information to get a final grade"))

	def exit(self):
		self.close()

	def GpaAverageCalculate(self):
		comboLst = [self.comboBox, self.comboBox_2, self.comboBox_3, self.comboBox_4, self.comboBox_5, self.comboBox_6, self.comboBox_7,
			   self.comboBox_8, self.comboBox_9]

		spinBoxlst = [self.spinBox, self.spinBox_2, self.spinBox_3, self.spinBox_4, self.spinBox_5, self.spinBox_6, self.spinBox_7,
					  self.spinBox_8]


		#for char in comboLst:
		#	if char.currentText() != '-' and self.spinBox.:
		#		self.textEdit_2.append(str(char.currentText()))

		for num in spinBoxlst:
			if num.value()  != -1:
				self.textEdit_2.append(str(self.spinBox.value()))


def main():
	app = QtGui.QApplication(sys.argv)
	form = CalculateApp()
	form.show()
	app.exec_()


if __name__ == '__main__':
	main()
