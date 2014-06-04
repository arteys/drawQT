# -*- coding: utf-8 -*-
__author__ = 'arteys'

import sys
from PyQt4 import QtCore, QtGui
import drawQt5widget

class TableResultWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Result table')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    tablewindow = TableResultWindow()
    tablewindow.show()
    sys.exit(app.exec_())
