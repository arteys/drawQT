# -*- coding: utf-8 -*-
__author__ = 'arteys'

import sys
from PyQt4 import QtCore, QtGui
#import drawQt6widget


class CalibrationWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle("Calibration line")


#Slider
        self.sldbright = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sldbright.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sldbright.setGeometry(40, 20, 300, 30)
        self.sldbright.setValue(50)
        self.sldbright.setMaximum(100)
        self.sldbright.setMinimum(1)


#Label/Button
        self.labelbright = QtGui.QPushButton(self)
        self.labelbright.setGeometry(10, 20, 22, 22)
        self.labelbright.setIcon(QtGui.QIcon('./res/bright.png'))
        self.labelbright.setIconSize(QtCore.QSize(24,24))

        self.setGeometry(300, 300, 380, 170)
        self.show()

    def empty(self):
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    calibration = CalibrationWindow()
    sys.exit(app.exec_())