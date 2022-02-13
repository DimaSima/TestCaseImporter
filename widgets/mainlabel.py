import sys
from PyQt5.QtWidgets import QVBoxLayout,QLabel,QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap

class MainLabel(QWidget):
    def __init__(self,text):
        super().__init__()
        self.text = text
        self.initUI()

    def initUI(self):
        _label = QLabel(self)
        _label.setText(self.text)
        _label.setAlignment(Qt.AlignCenter)
        _label.setFont(QFont("Arial", 14, QFont.Bold))

        labelLayout=QHBoxLayout()
        labelLayout.addWidget(_label)

        self.setLayout(labelLayout)
        self.show()
