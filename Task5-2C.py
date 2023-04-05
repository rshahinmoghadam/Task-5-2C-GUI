import RPi.GPIO as GPIO # import the GPIO library	
from time import sleep # import the time for apply delay
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



GPIO.setmode(GPIO.BOARD) # set the standard mode 
GPIO.setup(40,GPIO.OUT) # set the port 40 as output to LED
GPIO.setup(38,GPIO.OUT) 
GPIO.setup(36,GPIO.OUT) 

def blueLight():

	GPIO.output(40,GPIO.HIGH)
	GPIO.output(38,GPIO.LOW)
	GPIO.output(36,GPIO.LOW)
		
	

def greenLight():

	GPIO.output(40,GPIO.LOW)
	GPIO.output(38,GPIO.HIGH)
	GPIO.output(36,GPIO.LOW)
		

def redLight():

	GPIO.output(40,GPIO.LOW)
	GPIO.output(38,GPIO.LOW)
	GPIO.output(36,GPIO.HIGH)
	
def turnoff():

	GPIO.output(40,GPIO.LOW)
	GPIO.output(38,GPIO.LOW)
	GPIO.output(36,GPIO.LOW)
	

	


def window():
	GPIO.output(40,GPIO.LOW)
	GPIO.output(38,GPIO.LOW)
	GPIO.output(36,GPIO.LOW)
	app = QApplication(sys.argv)
	win = QMainWindow()
	win.setGeometry(600, 600, 400, 300)
	win.setWindowTitle("Task 5.2C")
	
	b1 = QtWidgets.QPushButton(win)
	b1.setText("Blue Light")
	b1.move(50,40)
	b1.clicked.connect(blueLight)
	
	
	b2 = QtWidgets.QPushButton(win)
	b2.setText("Green Light")
	b2.move(50,80)
	b2.clicked.connect(greenLight)
	
	b3 = QtWidgets.QPushButton(win)
	b3.setText("Red Light")
	b3.move(50,120)
	b3.clicked.connect(redLight)
	
	b4 = QtWidgets.QPushButton(win)
	b4.setText("Turn off")
	b4.move(50,160)
	b4.clicked.connect(turnoff)
	
	b5 = QtWidgets.QPushButton(win)
	b5.setText("Exit")
	b5.move(50,200)
	b5.clicked.connect(app.quit)
	
	
	
	
	
	win.show()
	sys.exit(app.exec_())
	
	
try: 
	window()
except:
	GPIO.cleanup()

'''
try:
	while 1:
		window()
except KeyboardInterrupt():
		GPIO.cleanup()
'''

