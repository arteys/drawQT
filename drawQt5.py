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
import imagePropwidget
import tableResultwidget
import histResultwidget


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
        saveDataAction = QtGui.QAction(QtGui.QIcon('./res/save.png'), "Save Data", self, shortcut="Ctrl+S",
                triggered=self.empty)
        exitAction = QtGui.QAction("Exit", self, shortcut="Ctrl+Q",
                triggered=self.close)
        clearAction = QtGui.QAction(QtGui.QIcon('./res/clear.png'), "Clear View", self, shortcut="Ctrl+N",
                triggered=self.clearEvent)
        tableAction = QtGui.QAction(QtGui.QIcon('./res/table.png'), "Create Result Table", self, shortcut="Ctrl+T",
                triggered=self.createTableWindow)
        imagePropAction = QtGui.QAction(QtGui.QIcon('./res/improp.png'), "Image Properties", self, shortcut="Ctrl+I",
                triggered=self.createImagePropWindow)
        histAction = QtGui.QAction(QtGui.QIcon('./res/hist.png'), "Create Result Histogram", self, shortcut="Ctrl+H",
                triggered=self.createHistPropWindow)
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
        fileMenu.addAction(saveDataAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)
        fileMenu = menubar.addMenu('Result')
        fileMenu.addAction(tableAction)
        fileMenu.addAction(histAction)
        fileMenu = menubar.addMenu('Edit')
        fileMenu.addAction(clearAction)
        fileMenu.addAction(imagePropAction)
        fileMenu = menubar.addMenu('View')
        fileMenu.addAction(zoomNormalAction)
        fileMenu.addAction(zoomPlusAction)
        fileMenu.addAction(zoomMinusAction)
        fileMenu = menubar.addMenu('About')

        toolbarfile = self.addToolBar('File')
        toolbarfile.addAction(openAction)
        toolbarfile.addAction(loadDataAction)
        toolbarfile.addAction(saveDataAction)
        toolbarresult = self.addToolBar('Result')
        toolbarresult.addAction(histAction)
        toolbarresult.addAction(tableAction)
        toolbarrview = self.addToolBar('Result')
        toolbarrview.addAction(zoomNormalAction)
        toolbarrview.addAction(zoomPlusAction)
        toolbarrview.addAction(zoomMinusAction)
        toolbaredit = self.addToolBar('Edit')
        toolbaredit.addAction(imagePropAction)
        toolbaredit.addAction(clearAction)

    def createTableWindow(self):           # Create image properties widget
        tabchild = tableResultwidget.TableResultWindow(self)
        tabchild.show()

    def createImagePropWindow(self):           # Create table widget
        imchild = imagePropwidget.ImagePropWindow(self)
        imchild.show()

    def createHistPropWindow(self):           # Create histogram widget
        histchild = histResultwidget.HistResultWindow(self)
        histchild.show()


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


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.resize(1024, 950)
    window.show()
    sys.exit(app.exec_())
