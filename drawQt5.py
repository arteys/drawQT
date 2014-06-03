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

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()   
        
        self.setWindowTitle('drawQT')
       
        self.form_widget = Window(self) 
        self.setCentralWidget(self.form_widget)
        
        self.createActions()

    def createActions(self):
        openAction = QtGui.QAction(QtGui.QIcon('exit24.png'), "Open Image", self, shortcut="Ctrl+O",
                triggered=self.close)
        loadDataAction = QtGui.QAction("Load Data", self, shortcut="Ctrl+D",
                triggered=self.close)
        exitAction = QtGui.QAction("Exit", self, shortcut="Ctrl+Q",
                triggered=self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(loadDataAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)
        fileMenu = menubar.addMenu('Edit')
        fileMenu = menubar.addMenu('Settings')
        fileMenu = menubar.addMenu('About')



class Window(QtGui.QWidget):
    def __init__(self, parent):
        super(Window, self).__init__()

        self.view = View(self)


        self.btnLoad = QtGui.QPushButton('Load', self)
        self.btnLoad.setIcon(QtGui.QIcon('./res/open.ico')) #Загрузка картинки
        self.btnLoad.setIconSize(QtCore.QSize(24,24))

        self.btnClearView = QtGui.QPushButton('Clear View', self)
        self.btnPlot = QtGui.QPushButton('Plot', self)


        self.slrBrigthness = QtGui.QSlider(QtCore.Qt.Horizontal, self)
#       self.lcdBrigthness = QtGui.QLCDNumber(self)
        self.slrBrigthness.setTickPosition (QtGui.QSlider.TicksBelow)
        self.slrBrigthness.setMinimum(1)
        self.slrBrigthness.setMaximum(100)
        self.slrBrigthness.setValue(50)
        self.slrBrigthness.setTickInterval(1)
        self.slrBrigthness.setDisabled(True)
        self.slrContrast = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        #CONSTRUCTION
        #layout's
        self.lytVert = QtGui.QVBoxLayout()
        self.lytHorButtons = QtGui.QHBoxLayout()
        self.lytHorView = QtGui.QHBoxLayout()


        #add to layout's
#       self.lytHorButtons.addWidget(self.lcdBrigthness)
        self.lytHorButtons.addWidget(self.btnLoad)
        self.lytHorButtons.addWidget(self.btnClearView)
        self.lytHorButtons.addWidget(self.btnPlot)


        self.lytHorView.addWidget(self.view)
        

        self.lytVert.addLayout(self.lytHorView)
        self.lytVert.addWidget(self.slrBrigthness)
        self.lytVert.addWidget(self.slrContrast)

        self.lytVert.addLayout(self.lytHorButtons)
        self.setLayout(self.lytVert)

        #SLOT's
        self.btnClearView.clicked.connect(self.handleClearView)
        self.btnLoad.clicked.connect(self.handleLoad)

#       self.connect(self.slrBrigthness, QtCore.SIGNAL('valueChanged(int)'),
#                     self.lcdBrigthness, QtCore.SLOT('display(int)') )
        self.connect(self.slrBrigthness, QtCore.SIGNAL('valueChanged(int)'),
                     self.updateBrigthness)
        #CONSTANT's
        self.coordinates=[]

    #FUNCTION's




    def handleClearView(self):
        self.view.scene.clear()
        self.view.lines=[]
        self.slrBrigthness.setDisabled(True)
        #self.view.setSceneRect(0, 0, 0, 0)
    def handleLoad(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home/argentum/Python_work')
        print("Loaded file:")
        print(self.fname)
        #print(type(fname))
        #print(type(str(fname)))
        self.imgPath = str(self.fname)
        img=Image.open(self.imgPath)
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)
        pixMap = QtGui.QPixmap.fromImage(self.imgQ)
        self.pixItem = QtGui.QGraphicsPixmapItem(pixMap)
        self.view.scene.addItem(self.pixItem)
        self.view.fitInView(QtCore.QRectF(0, 0, w, h), QtCore.Qt.KeepAspectRatio)
        self.view.scene.update()
        self.slrBrigthness.setDisabled(False)

    def updateBrigthness(self, evnt):
        if len(self.view.lines) > 0:
            self.coordinates=[]
            for i in range(len(self.view.lines)):
                l=self.view.lines[i]
                lF=l.line()
                curCoord=[lF.x1(), lF.y1(), lF.x2(), lF.y2()]           
                self.coordinates.append(curCoord)
        #self.view.scene.clear()
        self.view.lines = []
        #print(self.coordinates)
        
        sliderBrigthnessValue = self.slrBrigthness.value()
        curBr=float(sliderBrigthnessValue)/25.0
        print(curBr)
        #self.view.scene.removeItem(self.pixItem)
        self.view.scene.clear()
        #imgPath = str(self.fname)
        img=Image.open(self.imgPath)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(curBr)
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)
        pixMap = QtGui.QPixmap.fromImage(self.imgQ)
        self.pixItem = QtGui.QGraphicsPixmapItem(pixMap)
        self.view.scene.addItem(self.pixItem)
        self.view.fitInView(QtCore.QRectF(0, 0, w, h), QtCore.Qt.KeepAspectRatio)
        self.view.scene.update()
        if len(self.coordinates) > 0:
            self.view.redrawLines(self.coordinates)
        
        
    
    def updateContrast(self):
        pass


class View(QtGui.QGraphicsView):
    def __init__(self, parent):
        QtGui.QGraphicsView.__init__(self, parent)
        self.scene=QtGui.QGraphicsScene(self)
        self.setScene(self.scene)
        self.lines = []

    def mousePressEvent(self, event):
        self._start = event.pos()

    def mouseReleaseEvent(self, event):
        start = QtCore.QPointF(self.mapToScene(self._start))
        end = QtCore.QPointF(self.mapToScene(event.pos()))
        curLine = QtGui.QGraphicsLineItem(QtCore.QLineF(start, end))
        self.scene.addItem(curLine)
        xx=[]
        yy=[]
        for point in (start, end):
#            text = self.scene.addSimpleText('(%d, %d)' % (point.x(), point.y()))
#            text.setBrush(QtCore.Qt.red)
#            text.setPos(point)
            xx.append(point.x())
            yy.append(point.y())
        leng=sqrt((xx[1]-xx[0])**2+(yy[1]-yy[0])**2)
#        print("Current coordinates (x1, x2) and (y1, y2):")
#        print(xx, yy)
#        print("Messured length in pixels:")
#        print(leng)
        self.lines.append(curLine)
        print("Number of lines: "),
        print(len(self.lines))

        for i in range(len(self.lines)):
            l=self.lines[i]
            print(l)
            lF=l.line()
            #print("Extracted coordinates:")
            #print(lF.x1(), lF.y1(), lF.x2(), lF.y2())
    def redrawLines(self, coordinates):
        if len(coordinates) > 0:
            for i in range(len(coordinates)):
                curCoord=coordinates[i]
                x1, y1, x2, y2 = curCoord
                curLine=QtGui.QGraphicsLineItem(x1, y1, x2, y2)
                self.scene.addItem(curLine)
                self.lines.append(curLine)
#            for i in range(len(self.lines)):
#                l=self.lines[i]
#                print(l)
#                lF=l.line()

        
if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.resize(1024, 950)
    window.show()
    sys.exit(app.exec_())
