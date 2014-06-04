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
                triggered=self.clearEvent)
        tableAction = QtGui.QAction(QtGui.QIcon('./res/table.png'), "Create Result Table", self, shortcut="Ctrl+T",
                triggered=self.createTableWindow)
        histAction = QtGui.QAction(QtGui.QIcon('./res/hist.png'), "Create Result Histogram", self, shortcut="Ctrl+H",
                triggered=self.empty)
        zoomPlusAction = QtGui.QAction(QtGui.QIcon('./res/zoomplus.png'), "Zoom +20%", self, shortcut="Ctrl++",
                triggered=self.empty)
        zoomMinusAction = QtGui.QAction(QtGui.QIcon('./res/zoomminus.png'), "Zoom -20%", self, shortcut="Ctrl+-",
                triggered=self.empty)
        zoomNormalAction = QtGui.QAction(QtGui.QIcon('./res/zoomoptimal.png'), "Zoom 100%", self, shortcut="Ctrl+L",
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
        fileMenu = menubar.addMenu('View')
        fileMenu.addAction(zoomNormalAction)
        fileMenu.addAction(zoomPlusAction)
        fileMenu.addAction(zoomMinusAction)
        fileMenu = menubar.addMenu('About')

        toolbarfile = self.addToolBar('File')
        toolbarfile.addAction(openAction)
        toolbarfile.addAction(loadDataAction)
        toolbarresult = self.addToolBar('Result')
        toolbarresult.addAction(histAction)
        toolbarresult.addAction(tableAction)
        toolbarrview = self.addToolBar('Result')
        toolbarrview.addAction(zoomNormalAction)
        toolbarrview.addAction(zoomPlusAction)
        toolbarrview.addAction(zoomMinusAction)
        toolbaredit = self.addToolBar('Edit')
        toolbaredit.addAction(clearAction)

    def createTableWindow(self):
        # here put the code that creates the new window and shows it.
        child = MyWindow(self)
        child.show()

    def empty(self):
        pass

    def clearEvent(self):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to clear all?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.form_widget.handleClearView()
        else:
            pass

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class MyWindow(QtGui.QDialog):    # any super class is okay
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.button = QtGui.QPushButton('Press')
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.create_child)
    def create_child(self):
        pass

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.resize(1024, 950)
    window.show()
    sys.exit(app.exec_())
