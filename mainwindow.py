import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QStackedWidget,QWidget, QHBoxLayout
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

from widgets.mainlabel import MainLabel

__version__ = '0.1'
__author__ = 'Dmitrij Simagin'

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.x=100
        self.y=100
        self.width=1300
        self.height=910
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setMinimumSize(self.width, self.height)
        self.setStyleSheet("background:rgb(255,255,255)")
        self.setWindowTitle('Test Case Import Tool')
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

        self.stackedWidget=QStackedWidget()
        self.startWindow=StartWindow()

        self.stackedWidget.addWidget(self.startWindow)

        self.setCentralWidget(self.stackedWidget)
        self.show()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        copyright = QAction("Copyright",self)
        self.menu.addAction(copyright)
        copyright.triggered.connect(self._open_copyright)

        about = QAction("About", self)
        self.menu.addAction(about)
        about.triggered.connect(self._open_about)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

    def _open_copyright(self):
        Copyright=QDialog(None, Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        OkBtn=QDialogButtonBox(Copyright)
        #Copyright.accepted.connect(self.close())
        Copyright.setFixedSize(600,500)
        Copyright.setWindowTitle("Copyright")

        # Copyright notice
        CopyrightLbl=QLabel("Lizenzhinweis")
        CopyrightLbl.setFont(QFont("Arial", 14, QFont.Bold))
        CopyrightLbl1=QLabel("Copyright (c) 2022 Dmitrij Simagin")
        CopyrightLbl2=QLabel('Permission is hereby granted, free of charge, to any person obtaining a copy of this software and\nassociated documentation files (the "Software"), to deal in the Software without restriction,\nincluding without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,\nand/or sell copies of the Software, and to permit persons to whom the Software is furnished to do\nso, subject to the following conditions:')
        CopyrightLbl3=QLabel("The above copyright notice and this permission notice shall be included in all copies or\nsubstantial portions of the Software.")
        CopyrightLbl4=QLabel('THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,\nINCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A\nPARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\nCOPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN\nAN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION\nWITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.')

        CopyrightLayout=QVBoxLayout()
        CopyrightLayout.addWidget(CopyrightLbl)
        CopyrightLayout.addSpacing(40)
        CopyrightLayout.addWidget(CopyrightLbl1)
        CopyrightLayout.addSpacing(40)
        CopyrightLayout.addWidget(CopyrightLbl2)
        CopyrightLayout.addSpacing(40)
        CopyrightLayout.addWidget(CopyrightLbl3)
        CopyrightLayout.addSpacing(40)
        CopyrightLayout.addWidget(CopyrightLbl4)

        # Set layout of Dialog-Window
        Copyright.setLayout(CopyrightLayout)

        # Execute Dialog-Window
        Copyright.exec()

    def _open_about(self):
        About=QDialog(None, Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        OkBtn=QDialogButtonBox(About)
        About.setFixedSize(400,150)
        About.setWindowTitle("Copyright")

        AboutLbl=QLabel("Test Case Importer Tool")
        AboutLbl.setFont(QFont("Arial", 8, QFont.Bold))
        AboutLbl1=QLabel('Version:  {}'.format(__version__))
        AboutLbl2=QLabel('Author:  {}'.format(__author__))

        AboutLayout=QVBoxLayout()
        AboutLayout.addStretch(1)
        AboutLayout.addWidget(AboutLbl)
        AboutLayout.addSpacing(10)
        AboutLayout.addWidget(AboutLbl1)
        AboutLayout.addWidget(AboutLbl2)
        AboutLayout.addStretch(1)

        About.setLayout(AboutLayout)
        About.exec()


class StartWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setStyleSheet("background:rgb(255,255,255)")
            #self.eximiaText = MainLabel("Eximia Engineering")
            #self.toolText = MainLabel("Test Case Import Tool")
            self.eximiaText = QLabel("Eximia Engineering",self)
            self.toolText = QLabel("Test Case Import Tool",self)

            windowLayout = QHBoxLayout()
            windowLayout.addWidget(self.eximiaText)
            windowLayout.addWidget(self.toolText)

            self.setLayout(windowLayout)
            self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())