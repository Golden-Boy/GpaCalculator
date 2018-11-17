'''


'''

from PyQt4 import QtGui
import sys # required for argv
import CalcGUI # PyQt UI

class CalculateApp(QtGui.QMainWindow, CalcGUI.Ui_MainWindow):
	def __init__(self):
		super().__init__() # allows passed in variables to handle specific attributes
		self.setupUi(self)
		self.setWindowTitle("GPA Calculator")
		self.calcBtn.clicked.connect(self.calculate)
		self.exitBtn.clicked.connect(self.exit)

	def calculate(self): # calculate gpa
		#print('This is the calculate functionality')
		pass

	def exit(self):  # exit button
		pass
		#print('This is the exit functionality')



def main():
	app = QtGui.QApplication(sys.argv)
	form = CalculateApp()
	form.show()
	app.exec_() # required to run app


if __name__ == '__main__':
	main()