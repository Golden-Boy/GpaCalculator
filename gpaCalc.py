import sys
from PyQt5.QtWidgets import QApplication, QWidget

def app():
	my_app = QApplication(sys.argv)
	w = QWidget()
	w.setWindowTitle("GPA Calculator")

	w.show()
	sys.exit(my_app.exec_())

app()
