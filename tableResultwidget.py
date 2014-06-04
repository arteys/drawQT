# -*- coding: utf-8 -*-
__author__ = 'arteys'


import sys
from PyQt4 import QtCore, QtGui

data = {'col1':['1','2','3'], 'col2':['4','5','6'], 'col3':['7','8','9']}

class TableResultWindow(QtGui.QTableWidget):
    def __init__(self, data, *args):
        QtGui.QTableWidget.__init__(self, *args)
        self.data = data
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setmydata(self):

        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QtGui.QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)

def main(args):
    app = QtGui.QApplication(args)
    table = TableResultWindow(data, 5, 3)
    table.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main(sys.argv)
