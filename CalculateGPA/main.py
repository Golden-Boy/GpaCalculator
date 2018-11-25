'''
Created by Justice Jacobs from FarBeyondAverage

'''

from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys # required for argv
import CalcGUI # PyQt UI

class CalculateApp(QtGui.QMainWindow, CalcGUI.Ui_MainWindow):
	def __init__(self):
		super().__init__() # allows passed in classes to handle specific attributes
		self.setupUi(self)
		self.setWindowTitle("GPA Calculator")
		self.calcBtn.clicked.connect(self.calculate)
		self.exitBtn.clicked.connect(self.exit)
		self.lineEdit.setValidator(QDoubleValidator(.99, 99.99, 3))
		self.lineEdit_2.setValidator(QDoubleValidator(.99, 99.99, 3))
		self.lineEdit_3.setValidator(QDoubleValidator(.99, 99.99, 3))


	def exit(self): # exit button
		self.close()


	def calculate(self): # calculate gpa

		d = self.lineEdit_2.text()
		c = self.lineEdit_3.text()
		w = self.lineEdit.text()

		#print(self.textEdit.append(str(float(c) - (float(c) * ((1 - (float(w) / 100)) * float(1))) / (float(w) / 100))))

		print(str(((float(d) - ((1 - float(w)) * float(c))) / float(w))))


		#print(self.textEdit.append(str(((float(self.lineEdit_2.text()) - float(self.lineEdit_3.text() * (.1 - float(self.lineEdit.text())))) / float(self.lineEdit.text())))))

		#print(self.textEdit.append(str(float(self.lineEdit_2.text()) - float(self.lineEdit_3.text())) * (.1 - float(self.lineEdit.text())) / float(self.lineEdit_3.text())))


	def user_output(self): # output all relevant info to textEdit

		if self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text():
			print(self.textEdit.append('At your current grade {} you need a minimum grade of {} to get a {}'.format(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text())))
		#for char in self.lst:
			#print(self.textEdit.append(char))

def main():
	app = QtGui.QApplication(sys.argv)
	form = CalculateApp()
	form.show()
	app.exec_() # required to run app


if __name__ == '__main__':
	main()