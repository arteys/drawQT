# -*- coding: utf-8 -*-
__author__ = 'arteys'

import sys
from PyQt4 import QtCore, QtGui
import drawQt5widget

class HistResultWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Result histogramm')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    histwindow = HistResultWindow()
    histwindow.show()
    sys.exit(app.exec_())
