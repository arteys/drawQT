# -*- coding: utf-8 -*-
"""
Created on Thu May  8 02:46:29 2014

@author: argentum
"""

from PyQt4 import QtGui, QtCore
from math import sqrt
from PIL import Image
from PIL import ImageQt
from PIL import ImageEnhance

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

import imagePropwidget


class Window(QtGui.QWidget):
    def __init__(self, parent):
        super(Window, self).__init__()
        self.view = View(self)
        self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.btnLoad = QtGui.QPushButton('Load', self)
        self.btnClearView = QtGui.QPushButton('Clear View', self)
        self.btnPlot = QtGui.QPushButton('Plot', self)
        self.btnQuit = QtGui.QPushButton('Quit', self)
        self.lcdBrightness = QtGui.QLCDNumber(self)
        
        
        #Slider Brightness
        self.slrBrightness = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slrBrightness.setTickPosition (QtGui.QSlider.TicksBelow)
        self.slrBrightness.setMinimum(1)
        self.slrBrightness.setMaximum(100)
        self.slrBrightness.setValue(50)
        self.slrBrightness.setTickInterval(1)
        self.slrBrightness.setDisabled(True)
        #Slider Contrast
        self.slrContrast = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slrBrightness.setTickPosition (QtGui.QSlider.TicksBelow)
        self.slrContrast.setMinimum(1)
        self.slrContrast.setMaximum(100)
        self.slrContrast.setValue(50)
        self.slrContrast.setTickInterval(1)
        self.slrContrast.setDisabled(True)
        #CONSTRUCTION
        #layout's
        self.lytVert = QtGui.QVBoxLayout()
        self.lytHorButtons = QtGui.QHBoxLayout()
        self.lytHorView = QtGui.QHBoxLayout()
        #add to layout's
        self.lytHorButtons.addWidget(self.lcdBrightness)
        self.lytHorButtons.addWidget(self.btnLoad)
        self.lytHorButtons.addWidget(self.btnClearView)
        self.lytHorButtons.addWidget(self.btnPlot)
        self.lytHorButtons.addWidget(self.btnQuit)
        self.lytHorView.addWidget(self.view)
        #self.lytHorView.addWidget(self.slrContrast)
        self.lytVert.addLayout(self.lytHorView)
        self.lytVert.addWidget(self.slrBrightness)
        self.lytVert.addWidget(self.slrContrast)
        self.lytVert.addLayout(self.lytHorButtons)
        self.setLayout(self.lytVert)
        #EVENT's
        #short form
        self.btnClearView.clicked.connect(self.handleClearView)
        self.btnLoad.clicked.connect(self.handleLoad)
        self.btnPlot.clicked.connect(self.handlePlot)
        #long form
        self.connect(self.btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
        self.connect(self.slrBrightness, QtCore.SIGNAL('valueChanged(int)'),
                     self.lcdBrightness, QtCore.SLOT('display(int)') )
        self.connect(self.slrBrightness, QtCore.SIGNAL('valueChanged(int)'),
                     self.updateImageProperties)
        self.connect(self.slrContrast, QtCore.SIGNAL('valueChanged(int)'),
                     self.updateImageProperties)
        #CONSTANT's
        #self.lineCoordinates=[]

    #FUNCTION's
    def handleClearView(self):
        self.slrBrightness.setValue(50)
        self.slrContrast.setValue(50)        
        self.view.clearScene()
        self.slrBrightness.setDisabled(True)
        self.slrContrast.setDisabled(True)
        #self.view.setSceneRect(0, 0, 0, 0)
    def handleLoad(self):
        if len(self.view.lines) > 0:
            self.view.clearScene()
        else:
            self.view.scene.clear()
            
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home/argentum/Python_work')
        if self.fname:
            print("Loaded file:")        
            print(self.fname)
            self.imgPath = str(self.fname)
            self.img=Image.open(self.imgPath) #Load image!!!     
            w, h = self.img.size
            self.imgQ = ImageQt.ImageQt(self.img)
            pixMap = QtGui.QPixmap.fromImage(self.imgQ)
            self.pixItem = QtGui.QGraphicsPixmapItem(pixMap)
            self.view.scene.addItem(self.pixItem)
            self.view.fitInView(QtCore.QRectF(0, 0, w, h), QtCore.Qt.KeepAspectRatio)
            self.view.scene.update()
            self.slrBrightness.setDisabled(False)
            self.slrContrast.setDisabled(False)
        else:
            print("Not open")

    def createImagePropWindow(self):# Create image properties widget
        self.improp = imagePropwidget.ImagePropWindow(self)
        self.connect(self.improp.sldbright, QtCore.SIGNAL('valueChanged(int)'), self.updateImageProperties)
        self.connect(self.improp.sldcontr, QtCore.SIGNAL('valueChanged(int)'), self.updateImageProperties)
        self.connect(self.improp.sldcolor, QtCore.SIGNAL('valueChanged(int)'), self.updateImageProperties)


    def updateImageProperties(self, evnt):
        if len(self.view.lines) > 0:
            self.view.lineCoordinates=[]
            for i in range(len(self.view.lines)):
                l=self.view.lines[i]
                lF=l.line()
                curCoord=[lF.x1(), lF.y1(), lF.x2(), lF.y2()]           
                self.view.lineCoordinates.append(curCoord)
            self.view.lines = []

        sliderColorValue = self.improp.sldcolor.value()
        sliderBrightnessValue = self.improp.sldbright.value()
        sliderContrastValue = self.improp.sldcontr.value()

        self.curBr=float(sliderBrightnessValue)/50.0
        self.curCt=float(sliderContrastValue)/50.0
        self.curCl = float(sliderColorValue)/50.0
        self.view.scene.clear()

        curImageState=self.img

        curImageStateBr=curImageState
        enhancerBr = ImageEnhance.Brightness(curImageStateBr)
        curImageStateBr = enhancerBr.enhance(self.curBr)

        curImageStateCt = curImageState
        enhancerCt = ImageEnhance.Contrast(curImageStateCt)
        curImageStateCt = enhancerCt.enhance(self.curCt)

        curImageStateCl = curImageState
        enhancerCl = ImageEnhance.Color(curImageStateCl)
        curImageStateCt = enhancerCt.enhance(self.curCt)

        self.imgQ = ImageQt.ImageQt(curImageStateCt)
        pixMap = QtGui.QPixmap.fromImage(self.imgQ)
        self.pixItem = QtGui.QGraphicsPixmapItem(pixMap)
        self.view.scene.addItem(self.pixItem)
        self.view.scene.update()
        if len(self.view.lineCoordinates) > 0:
            self.view.redrawLines(self.view.lineCoordinates)

    def handlePlot(self):
        print("Handle plot")

        if len(self.view.lines) > 0:
            self.view.lineCoordinates=[]
            self.view.lineLengthes = []
            for i in range(len(self.view.lines)):
                l=self.view.lines[i]
                lF=l.line()
                curCoord=[lF.x1(), lF.y1(), lF.x2(), lF.y2()]           
                self.view.lineCoordinates.append(curCoord)
            #self.view.lines = []
            for i in range(len(self.view.lineCoordinates)):
                x1, y1, x2, y2 = self.view.lineCoordinates[i]
                leng=sqrt((x2-x1)**2+(y2-y1)**2)
                self.view.lineLengthes.append(leng)
                print(leng)
            self.plot = plotWindow()
            self.plot.resize(600, 600)
            self.plot.handlePlot(self.view.lineLengthes)
            self.plot.show()
        #print(self.view.lineCoordinates)
        #


class View(QtGui.QGraphicsView):
    def __init__(self, parent):
        QtGui.QGraphicsView.__init__(self, parent)
        self.scene=QtGui.QGraphicsScene(self)
        self.setScene(self.scene)
        self.lines = [] #list all lines
        self.lineCoordinates = []

    def mousePressEvent(self, event):
        self._start = event.pos()
        self.curLine = 0 #for redraw line interactive in mouseMoveEvent 
        start = QtCore.QPointF(self.mapToScene(self._start))
        curX1=start.x()-2
        curY1=start.y()-2
        curX2=curX1+4
        curY2=curY1+4
        rectCenter=QtCore.QPointF(curX1, curY1)
        rectSize = QtCore.QPointF(curX2, curY2)
        curRect = QtGui.QGraphicsRectItem(QtCore.QRectF(rectCenter, rectSize))
        curRect.setPen(QtCore.Qt.green)
        self.scene.addItem(curRect)
    
    def mouseMoveEvent(self, event):
        if self.curLine:
            self.scene.removeItem(self.curLine)
        self._movePos = event.pos()
        start = QtCore.QPointF(self.mapToScene(self._start))
        midle = QtCore.QPointF(self.mapToScene(self._movePos))
        self.curLine = QtGui.QGraphicsLineItem(QtCore.QLineF(start, midle))
        self.scene.addItem(self.curLine)
        
    def mouseReleaseEvent(self, event):
        start = QtCore.QPointF(self.mapToScene(self._start))
        end = QtCore.QPointF(self.mapToScene(event.pos()))
        curX1=end.x()-2
        curY1=end.y()-2
        curX2=curX1+4
        curY2=curY1+4
        rectCenter=QtCore.QPointF(curX1, curY1)
        rectSize = QtCore.QPointF(curX2, curY2)
        curRect = QtGui.QGraphicsRectItem(QtCore.QRectF(rectCenter, rectSize))
        curRect.setPen(QtCore.Qt.green)
        self.scene.addItem(curRect)
        curLine = QtGui.QGraphicsLineItem(QtCore.QLineF(start, end))
        curLine.setPen(QtCore.Qt.red)
        self.scene.addItem(curLine)
        self.lines.append(curLine) #add line to list!!!
    
    def redrawLines(self, lineCoordinates):
        if len(lineCoordinates) > 0:
            for i in range(len(lineCoordinates)):
                curCoord=lineCoordinates[i]
                x1, y1, x2, y2 = curCoord
                
                #calculate 1'st rectangel
                curXleftStart = x1 - 2
                curYleftStart = y1 - 2
                curXrightStart = curXleftStart+4
                curYrightStart = curYleftStart+4
                rectCenterStart=QtCore.QPointF(curXleftStart, curYleftStart)
                rectSizeStart = QtCore.QPointF(curXrightStart, curYrightStart)
                curRect = QtGui.QGraphicsRectItem(QtCore.QRectF(rectCenterStart, rectSizeStart))
                curRect.setPen(QtCore.Qt.green)
                self.scene.addItem(curRect)
                #calculate 2'nd rectangel
                curXleftEnd = x2 - 2
                curYleftEnd = y2 - 2
                curXrightEnd = curXleftEnd+4
                curYrightEnd = curYleftEnd+4
                rectCenterEnd=QtCore.QPointF(curXleftEnd, curYleftEnd)
                rectSizeEnd = QtCore.QPointF(curXrightEnd, curYrightEnd)
                curRect = QtGui.QGraphicsRectItem(QtCore.QRectF(rectCenterEnd, rectSizeEnd))
                curRect.setPen(QtCore.Qt.green)
                self.scene.addItem(curRect)
                
                curLine=QtGui.QGraphicsLineItem(x1, y1, x2, y2)
                curLine.setPen(QtCore.Qt.red)
                self.scene.addItem(curLine)
                self.lines.append(curLine)
    def clearScene(self):
        self.scene.clear()
        self.lines=[]
        self.lineCoordinates=[]  
        
class plotWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.view = Qt4MplCanvas()
        self.toolbar = NavigationToolbar(self.view, self)
#        self.btnLoad = QtGui.QPushButton('Load', self)
#        self.btnClearView = QtGui.QPushButton('Clear View', self)
#        self.btnPlot = QtGui.QPushButton('Plot', self)
#        self.btnQuit = QtGui.QPushButton('Quit', self)
        #CONSTRUCTION
        self.lytVert = QtGui.QVBoxLayout()
#        self.lytHor = QtGui.QHBoxLayout()
#        self.lytHor.addWidget(self.btnLoad)
#        self.lytHor.addWidget(self.btnClearView)
#        self.lytHor.addWidget(self.btnPlot)
#        self.lytHor.addWidget(self.btnQuit)
#        self.lytVert.addWidget(self.toolbar)
        self.lytVert.addWidget(self.view)
        self.lytVert.addWidget(self.toolbar)
#        self.lytVert.addLayout(self.lytHor)
        self.setLayout(self.lytVert)
        #CONSTANT's
        self.multiplier=1
        #SLOT's
        #self.btnClearView.clicked.connect(self.handleClearView)
        #self.btnLoad.clicked.connect(self.handleLoad)
#        self.btnPlot.clicked.connect(self.handlePlot)
#        self.connect(self.btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
    
    def handlePlot(self, lineLengthes):
        x = np.array(lineLengthes)
        bins = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 300, 400, 500])
        print("Array lenghtes:")
        print(x)
#        hist, bins = np.histogram(x, bins=12, normed=False)
        hist, bins = np.histogram(x, bins = bins, normed=False)
        print("hist:")
        print(hist)
        print("bins")
        print(bins)
        width = 0.9 * (bins[1] - bins[0])
        center = (bins[:-1] + bins[1:]) / 2
        print("center")
        print(center)
        self.view.axes.bar(center, hist, align='center', width=width, facecolor='g', alpha=0.5)
        self.view.axes.set_xlabel(r'$\mathrm{diameter,}\ m \mu$')
        self.view.axes.set_ylabel(r'$\mathrm{distribution,}\ \%$')
#        self.view.axes
#        self.view.axes.hist(lineLenghtes, 5, normed=1, facecolor='green', alpha=0.75)
        self.view.fig.canvas.draw()
#        self.view.axes.clear()
#        self.view.x = np.arange(0.0, 3.0, 0.01)
#        self.view.y = np.cos(self.multiplier*np.pi*self.view.x)
#        self.view.axes.plot(self.view.x, self.view.y)
#        self.view.fig.canvas.draw()
#        self.multiplier += 1


class Qt4MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self):
        # Standard Matplotlib code to generate the plot
        self.fig = Figure(facecolor="white")
        self.axes = self.fig.add_subplot(111, axisbg='w', xlabel='diameter, pxl', 
                                         ylabel='fraction, %', title='Distribution')
        #self.fig.add_axes()
        #self.fig.set_ylabel('log Y')
        #self.fig.add_axes([50, 50, 500, 500])
#        self.fig.text(0.2, 0.5, "Text")
        #self.x = np.arange(0.0, 3.0, 0.01)
        #self.y = np.cos(2*np.pi*self.x)
        #self.axes.plot(self.x, self.y)
        # initialize the canvas where the Figure renders into
        FigureCanvas.__init__(self, self.fig)
        
if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.resize(650, 700)
    window.show()
    sys.exit(app.exec_())