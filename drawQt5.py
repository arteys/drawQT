# -*- coding: utf-8 -*-
"""
Created on Thu May  8 02:46:29 2014

@author: argentum, arteys
"""

from PyQt4 import QtGui, QtCore
from math import sqrt
from PIL import Image
from PIL import ImageQt
from PIL import ImageEnhance
import drawQt5widget

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        self.setWindowTitle('drawQT')

        self.form_widget = drawQt5widget.Window(self)
        self.setCentralWidget(self.form_widget)

        self.createActions()

    def createActions(self):
        openAction = QtGui.QAction(QtGui.QIcon('./res/open.png'), "Open Image", self, shortcut="Ctrl+O",
                triggered=self.form_widget.handleLoad)
        loadDataAction = QtGui.QAction(QtGui.QIcon('./res/dataload.png'), "Load Data", self, shortcut="Ctrl+D",
                triggered=self.empty)
        exitAction = QtGui.QAction("Exit", self, shortcut="Ctrl+Q",
                triggered=self.close)
        clearAction = QtGui.QAction(QtGui.QIcon('./res/clear.png'), "Clear View", self, shortcut="Ctrl+N",
                triggered=self.form_widget.handleClearView)
        tableAction = QtGui.QAction(QtGui.QIcon('./res/table.png'), "Create Result Table", self, shortcut="Ctrl+T",
                triggered=self.empty)
        histAction = QtGui.QAction(QtGui.QIcon('./res/hist.png'), "Create Result Histogram", self, shortcut="Ctrl+H",
                triggered=self.empty)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(loadDataAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)
        fileMenu = menubar.addMenu('Result')
        fileMenu.addAction(tableAction)
        fileMenu.addAction(histAction)
        fileMenu = menubar.addMenu('Edit')
        fileMenu.addAction(clearAction)
        fileMenu = menubar.addMenu('Settings')
        fileMenu = menubar.addMenu('About')

        toolbarfile = self.addToolBar('File')
        toolbarfile.addAction(openAction)
        toolbarfile.addAction(loadDataAction)
        toolbarresult = self.addToolBar('Result')
        toolbarresult.addAction(histAction)
        toolbarresult.addAction(tableAction)
        toolbaredit = self.addToolBar('Edit')
        toolbaredit.addAction(clearAction)


    def empty(self):
        pass

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.resize(1024, 950)
    window.show()
    sys.exit(app.exec_())
