from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QThread
from PySide6.QtGui import QAction
import sys
import os



class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.mainWindow = loader.load('mainWindow.ui')
        self.initialize()
        self.mainWindow.show()


    def initialize(self):
        openAction = QAction('Exit')
        self.mainWindow.openDicomFilesMenu.triggered.connect(self.openDicomFiles())

        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)
        self.filemenu = self.menubar.addMenu('&File')
        self.filemenu.addAction(QAction(openAction, self))


    def openDicomFiles(self):
        print('Menu clicked')


app = QApplication(sys.argv)
main = mainWindow()
# main.start()
sys.exit(app.exec())




