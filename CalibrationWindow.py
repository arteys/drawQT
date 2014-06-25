# -*- coding: utf-8 -*-
__author__ = 'arteys'

import sys
from PyQt4 import QtCore, QtGui


class CalibrationWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle("Calibration line")

        unitCombobox = QtGui.QComboBox()
        unitCombobox.insertItems(1,["mm","mkm","nm","Å"])


        toolbar = self.addToolBar('Box')
        toolbar.addWidget(unitCombobox)

        self.setGeometry(300, 300, 380, 170)
        self.show()

    def empty(self):
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    calibration = CalibrationWindow()
    sys.exit(app.exec_())