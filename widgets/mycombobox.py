import sys
from PyQt5.QtWidgets import QVBoxLayout,QLabel,QWidget, QComboBox, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap


class MyComboBox(QWidget):
    def __init__(self):
        super().__init__()

        self.cb = QComboBox()
        self.cb.setFixedSize(300,50)
        self.cb.addItem("eCall")
        self.cb.addItem("Connectivity")
        self.cb.addItem("Predictive Maintenance")
        self.cb.currentIndexChanged.connect(self.printSelectionchange)
        self.cb.setCurrentIndex(0)
        self.cb.setPlaceholderText("Wähle einen Dienst aus:")
        self.cb.setFont(QFont("Arial", 10, QFont.Bold))
        self.cb.setStyleSheet("background:rgb(0,255,0)")

        layout = QHBoxLayout()
        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.show()

    def printSelectionchange(self,i):
        print ("Items in the list are :")
            
        for count in range(self.cb.count()):
            print (self.cb.itemText(count))
        print ("Current index",i,"selection changed ",self.cb.currentText())