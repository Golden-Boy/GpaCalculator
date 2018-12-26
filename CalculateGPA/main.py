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
		self.calcBtn.clicked.connect(self.FinalGradeCalculate)

		self.exitBtn.clicked.connect(self.exit)
		self.exitBtn2.clicked.connect(self.exit)
		self.calcBtn2.clicked.connect(self.GpaAverageCalculate)

		self.examWeight.setValidator(QDoubleValidator(.99, 99.99, 2)) # restricts user input(i.e. xx.xx)
		self.targetGrade.setValidator(QDoubleValidator(.99, 99.99, 2))
		self.currentGrade.setValidator(QDoubleValidator(.99, 99.99, 2))

		self.combolst = [self.comboBox, self.comboBox_2, self.comboBox_3, self.comboBox_4, self.comboBox_5, self.comboBox_6,
					self.comboBox_7,
					self.comboBox_8]

		self.spinBoxlst = [self.spinBox, self.spinBox_2, self.spinBox_3, self.spinBox_4, self.spinBox_5, self.spinBox_6,
					  self.spinBox_7,
					  self.spinBox_8]

		self.gradePoints = []

		self.attemptedCredits = 0

	def FinalGradeCalculate(self):

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

		for char in self.combolst:
			if char.currentText() != '-' and self.spinBox.value() != -1: # if user changes default values
					if char.currentText() == 'A':
						result1 = 4 * self.spinBox.value()
						self.gradePoints.append(result1)
					elif char.currentText() == 'B':
						result2 = 3 * self.spinBox.value()
						self.gradePoints.append(result2)
					elif char.currentText() == 'C':
						result3 = 2 * self.spinBox.value()
						self.gradePoints.append(result3)
					elif char.currentText() == 'D':
						result4 = 1 * self.spinBox.value()
						self.gradePoints.append(result4)
					elif char.currentText() == 'F':
						result5 = 0 * self.spinBox.value()
						self.gradePoints.append(result5)
					else:
						self.gradePoints.append(0)

		self.textEdit_2.append(str(sum(self.gradePoints)))

		for num in self.spinBoxlst:
			if num.value() != -1:
				self.attemptedCredits += num.value() # sum attempted credits
				#self.textEdit_2.append(str(num.value()))
		#self.textEdit_2.append(str(self.attemptedCredits))
		if self.attemptedCredits == 0:
			raise ValueError(self.textEdit_2.append("Can't divide by zero"))
		else:

			self.textEdit_2.append(str(sum((self.gradePoints)) / self.attemptedCredits))


		#self.textEdit_2.append(str((total / self.attemptedCredits)))

		#self.textEdit_2.append(str(total))
def main():
	app = QtGui.QApplication(sys.argv)
	form = CalculateApp()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
