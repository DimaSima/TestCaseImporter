import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt

class MainLabel(QWidget):
    def __init__(self,text):
        super().__init__()
        self.initUI()

    def initUI(self):
        label_ = QLabel(self)
        label_.setText(self.text)
        label_.setAlignment(Qt.AlignCenter)
        