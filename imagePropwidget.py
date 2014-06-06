# -*- coding: utf-8 -*-
__author__ = 'arteys'

import sys
from PyQt4 import QtCore, QtGui
#import drawQt6widget


class ImagePropWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle("Image properties window")



        self.sldbright = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sldbright.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sldbright.setGeometry(40, 20, 300, 30)
        self.sldbright.setValue(50)
        self.sldbright.setMaximum(100)
        self.sldbright.setMinimum(1)
        #self.sldbright.setDisabled(True)
        #self.sldbright.valueChanged()
#        self.sldbright.valueChanged[int].connect(self.brightchanged)

        self.sldcontr = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sldcontr.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sldcontr.setGeometry(40, 60, 300, 30)
        self.sldcontr.setValue(50)
        self.sldcontr.setMaximum(100)
        self.sldcontr.setMinimum(1)
        #self.sldcontr.setDisabled(True)
        #self.sldcontr.valueChanged[int].connect(self.changeValueContr)

        self.labelbright = QtGui.QPushButton(self)
        self.labelbright.setGeometry(10, 20, 22, 22)
        self.labelbright.setIcon(QtGui.QIcon('./res/bright.png'))
        self.labelbright.setIconSize(QtCore.QSize(24,24))
        self.labelbright.clicked.connect(self.setValueBright)

        self.labelcontr = QtGui.QPushButton(self)
        self.labelcontr.setGeometry(10, 60, 22, 22)
        self.labelcontr.setIcon(QtGui.QIcon('./res/contr.png'))
        self.labelcontr.setIconSize(QtCore.QSize(24,24))
        self.labelcontr.clicked.connect(self.setValueContr)


        self.setGeometry(300, 300, 380, 170)
        self.show()

    #Slots
#        self.connect(self.sldbright, QtCore.SIGNAL('valueChanged(int)'),
#                     self.drawQt6widget.Window.updateBrightnessContrast)
#        self.connect(self.sldcontr, QtCore.SIGNAL('valueChanged(int)'),
#                     self.drawQt6widget.Window.updateBrightnessContrast)

#    def brightchanged(self, value):


    def setValueBright(self):
        self.sldbright.setValue(50)
    def setValueContr(self):
        self.sldcontr.setValue(50)

    def empty(self):
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    propwindow = ImagePropWindow()
    sys.exit(app.exec_())