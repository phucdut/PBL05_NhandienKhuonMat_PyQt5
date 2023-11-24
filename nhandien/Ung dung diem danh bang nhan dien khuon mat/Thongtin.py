from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from FormThongtin import Ui_FormThongtin
import win32gui,win32con

class Fthongtin(QtWidgets.QWidget, Ui_FormThongtin):
    def __init__(self):
        super(Fthongtin, self).__init__()
        #hiden console
        # hide = win32gui.GetForegroundWindow()
        # win32gui.ShowWindow(hide , win32con.SW_HIDE)
        
        self.setupUi(self)
        self.bt_back.clicked.connect(self.exit)
        
    def exit(self):
        exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    Fthongtin = Fthongtin()
    Fthongtin.show()
    sys.exit(app.exec_())