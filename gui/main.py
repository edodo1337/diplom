from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import pandas as pd

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Tutorial")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("TestButton")
        
        self.lineEdit1 = QtWidgets.QLineEdit(self)
        self.lineEdit1.move(100,100)
        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.move(100,200)

        self.error_label1 = QtWidgets.QLabel(self)
        self.error_label2 = QtWidgets.QLabel(self)
        self.error_label1.move(200, 100)
        self.error_label2.move(200, 200)
        

        self.onlyFloat = QtGui.QDoubleValidator()

        self.lineEdit1.setValidator(self.onlyFloat)
        self.lineEdit2.setValidator(self.onlyFloat)

        self.b1.clicked.connect(self.clicked)
    
    # def validate(self, state):
    #     if state == QtGui.QValidator.Invalid:
    #         colour = 'red'
    #     elif state == QtGui.QValidator.Intermediate:
    #         colour = 'gold'
    #     elif state == QtGui.QValidator.Acceptable:
    #         colour = 'lime'
    #     self.lineEdit2.setStyleSheet('border: 3px solid %s' % colour)
    #     QtCore.QTimer.singleShot(1000, lambda: self.lineEdit2.setStyleSheet(''))

    def clicked(self):
        x1 = self.lineEdit1.text()
        x2 = self.lineEdit2.text()

        if x2 == '5':
            print('hello')
            self.lineEdit2.setStyleSheet('border: 3px solid %s' % 'red')
            self.error_label2.setText("Error")
            QtCore.QTimer.singleShot(1000, lambda: self.lineEdit2.setStyleSheet(''))
            QtCore.QTimer.singleShot(1000, lambda: self.error_label2.setText(''))

            return


        self.label.setText(x1+x2)

        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
