# -*- coding: utf-8 -*-
__author__ = 'arteys'

import sys
from PyQt4 import QtCore, QtGui
import drawQt5widget

class ImagePropWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle("Image properties window")

        self.draw_widget = drawQt5widget.Window(self)


        self.sldbright = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sldbright.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sldbright.setGeometry(30, 20, 300, 30)
        self.sldbright.setValue(50)
        self.sldbright.setMaximum(100)
        self.sldbright.setMinimum(1)
        #self.sldbright.setDisabled(True)
        #self.sldbright.valueChanged[int].connect(self.empty)

        self.sldcontr = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sldcontr.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sldcontr.setGeometry(30, 60, 300, 30)
        self.sldcontr.setValue(50)
        self.sldcontr.setMaximum(100)
        self.sldcontr.setMinimum(1)
        #self.sldcontr.setDisabled(True)
        #self.sldcontr.valueChanged[int].connect(self.changeValueContr)

        self.labelbright = QtGui.QLabel(self)
        self.labelbright.setPixmap(QtGui.QPixmap('./res/bright.png'))
        self.labelbright.setGeometry(10, 20, 15, 30)

        self.labelcontr = QtGui.QLabel(self)
        self.labelcontr.setPixmap(QtGui.QPixmap('./res/contr.png'))
        self.labelcontr.setGeometry(10, 60, 15, 30)

        self.setGeometry(300, 300, 350, 170)
        self.show()

    #Slots
        self.connect(self.sldbright, QtCore.SIGNAL('valueChanged(int)'),
                     self.draw_widget.updateBrightnessContrast)
        self.connect(self.sldcontr, QtCore.SIGNAL('valueChanged(int)'),
                     self.draw_widget.updateBrightnessContrast)



    def empty(self):
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    propwindow = ImagePropWindow()
    propwindow.show()
    sys.exit(app.exec_())