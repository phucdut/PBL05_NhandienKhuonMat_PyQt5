from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from FormTrogiup import Ui_FormTrogiup

class Ftrogiup(QtWidgets.QWidget, Ui_FormTrogiup):
    def __init__(self):
        super(Ftrogiup, self).__init__()
        self.setupUi(self)
        self.bt_back.clicked.connect(self.exit)

        
    def exit(self):
        exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    Ftrogiup = Ftrogiup()
    Ftrogiup.show()
    sys.exit(app.exec_())