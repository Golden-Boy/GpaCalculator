import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def app():

	# PyQt Application Object
	my_app = QApplication(sys.argv)

	# User interface object
	w = QWidget()

	# window size
	w.resize(500, 200)

	# window title
	w.setWindowTitle("Grade Point Average Calculator")

	# create textboxes
	textbox_output = QLineEdit(w)
	textbox_output.move(150,0)
	#textbox_output.resize(125,175)

	textbox_input = QLineEdit(w)
	textbox_input.textChanged.connect(gettext())

	# add button
	btn = QPushButton('Calculate', w)

	#btn.setToolTip('Click to quit!')
	btn.clicked.connect(when_clicked)

	#btn.resize(btn.sizeHint())
	btn.move(200,80)

	# show window
	w.show()

	# stops instant exit
	sys.exit(my_app.exec_())

	app()

# button actions
def when_clicked():
	pass

def gettext(text):
	pass
	#print(text)




'''
When button is clicked, it needs to take the users input and compute the needed grade to achieve the needed grade.
It should be able to determine the points needed and the overall grade in terms of a letter grade.

Code should utilize a 'class' structure.

'''
