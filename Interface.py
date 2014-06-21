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
import Main
import ImagePropWindow
import TableWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        self.setWindowTitle('drawQT')

        self.form_widget = Main.Window(self)
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
                triggered=self.form_widget.createImagePropWindow)
        histAction = QtGui.QAction(QtGui.QIcon('./res/hist.png'), "Create Result Histogram", self, shortcut="Ctrl+H",
                triggered=self.form_widget.handlePlot)
        zoomNormalAction = QtGui.QAction(QtGui.QIcon('./res/zoom.png'), "Zoom 100%", self, shortcut="Ctrl+L",
                triggered=self.empty)
        moveObjAction = QtGui.QAction(QtGui.QIcon('./res/moveobj.png'), "Move Object", self, shortcut="M",
                triggered=self.empty)
        drawCircleAction = QtGui.QAction(QtGui.QIcon('./res/circle.png'), "Draw Circle", self,
                triggered=self.empty)
        drawDoubleCircleAction = QtGui.QAction(QtGui.QIcon('./res/doublecircle.png'), "Draw Circle", self,
                triggered=self.empty)
        drawMeasureActionR = QtGui.QAction(QtGui.QIcon('./res/measurelinered.png'), "Draw Red Measure Line", self,
                triggered=self.empty)
        drawMeasureActionG = QtGui.QAction(QtGui.QIcon('./res/measurelineblue.png'), "Draw Blue Measure Line", self,
                triggered=self.empty)
        drawMeasureActionB = QtGui.QAction(QtGui.QIcon('./res/measurelinegreen.png'), "Draw Green Measure Line", self,
                triggered=self.empty)
        drawMeasureAction = QtGui.QAction(QtGui.QIcon('./res/calibrationmeasureline.png'), "Draw Calibration line", self,
                triggered=self.empty)
        delObjAction = QtGui.QAction(QtGui.QIcon('./res/delete.png'), "Delete Object", self,shortcut="Delete",
                triggered=self.empty)
        zoomCombobox = QtGui.QComboBox()
        zoomCombobox.addItem(QtGui.QIcon('./res/zoom.png'), 'Zoom')
        zoomCombobox.insertItems(1,["10%","20%","25%","33%","50%","67%","75%","100%","150%","200%","300%","400%"])

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
        fileMenu = menubar.addMenu('About')

        toolbarfile = self.addToolBar('File')
        toolbarfile.addAction(openAction)
        toolbarfile.addAction(loadDataAction)
        toolbarfile.addAction(saveDataAction)
        toolbarresult = self.addToolBar('Result')
        toolbarresult.addAction(histAction)
        toolbarresult.addAction(tableAction)
        toolbarrview = self.addToolBar('Result')
        toolbarrview.addWidget(zoomCombobox)
        toolbaredit = self.addToolBar('Edit')
        toolbaredit.addAction(imagePropAction)
        toolbaredit.addAction(clearAction)
        toolbardraw = self.addToolBar('Draw')
        toolbardraw.addAction(drawMeasureActionR)
        toolbardraw.addAction(drawMeasureActionG)
        toolbardraw.addAction(drawMeasureActionB)
        toolbardraw.addAction(drawCircleAction)
        toolbardraw.addAction(drawDoubleCircleAction)
        toolbardraw.addAction(moveObjAction)
        toolbardraw.addAction(delObjAction)
        toolbardraw.addAction(drawMeasureAction)


        zoomCombobox.activated[str].connect(self.empty) #This is zoom's slot


    def createTableWindow(self):           # Create table
        data = {'col1':['1','2','3'], 'col2':['4','5','6'], 'col3':['7','8','9']}
        tabchild = TableWindow.TableResultWindow(self, data, 5, 3)
        tabchild.show()



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
