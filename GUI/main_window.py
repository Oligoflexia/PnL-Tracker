#Following along the tutorial here https://coderslegacy.com/python/pyqt6-create-basic-window/

from cProfile import label
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, QAbstractTableModel, Qt

import sys
import pyqtgraph as pg
import numpy as np

from sqlalchemy import null

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data= data
        
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        
    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data[0])


class Window(QWidget):
    def __init__(self):
        super().__init__()
        #self.resize(1200, 900)
        self.setWindowTitle("PnL Tracker")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.UI()
        
        
    def UI(self):  
        #initialize all widgets
        self.addTokenButton = QPushButton("Add Token")
        self.addTokenButton.clicked.connect(self.addtoken)
        self.addTokenButton.setFixedSize(QSize(100, 25))
        
        self.tokenTable = QTableView()
        self.tokenTable.setFixedSize(QSize(525, 250))
        
        data = [
            ["BTC", 1, 69000, 1000, 0], 
            ["ETH", 32, 42069, 10000, 0], 
            ["NANO", 5, 0.69, -100, 0]
        ]
        self.model = TableModel(data)
        self.tokenTable.setModel(self.model)
        
        xval = np.random.normal(size = 100)
        yval = np.random.normal(size = 100)
        self.plotWidget = pg.plot(xval, yval, title="PnL Graph")
        
        
        #self.label = QLabel("The Price of ETH is: To the MOON")      
        self.listlabel = QLabel("I'm a token")
        
        #initialize grid
        grid = QGridLayout()
        grid.addWidget(self.plotWidget, 0, 0)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.addTokenButton)
        #vbox.addWidget(self.listlabel)
        vbox.addWidget(self.tokenTable)
        
        grid.addLayout(vbox, 1, 0)
        
        #
        self.setLayout(grid)
        self.setGeometry(0, 0, 900, 600)
        
    #function which adds a token
    def addtoken(self):
        self.listlabel.setText("You have added a new token")
 
 
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())