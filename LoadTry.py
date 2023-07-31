import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.uic import loadUi
import sys

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("try.ui", self)

        self.actionNew_File.triggered.connect(self.new_file)
        self.actionOpen_File.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_as.triggered.connect(self.saveAs)
    
    def new_file(self):
        print("Clicked on new file")
    
    def open_file(self):
        print("Clicked on open file")
    
    def save_file(self):
        print("Clicked on save")

    def saveAs(self):
        print("Clicked on save as")

if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()