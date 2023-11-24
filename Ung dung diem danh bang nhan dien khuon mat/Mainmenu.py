from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import  QApplication,QMessageBox
import sys
from FormMainmenu import Ui_Form_Mainmenu
import os

class Mainmenu(QtWidgets.QWidget,Ui_Form_Mainmenu ):
    def __init__(self):
        super(Mainmenu, self).__init__()
        self.setupUi(self)
        self.bt_thoat.clicked.connect(self.exit)
        self.bt_diemdanh.clicked.connect(self.nhandien)
        self.bt_thongtin.clicked.connect(self.thongtin)
        self.bt_trogiup.clicked.connect(self.trogiup)
        self.bt_admin.clicked.connect(self.admin)


    def exit(self):
        self.bt_thoat.isChecked()
        self.bt_thoat.setEnabled(False)
        buttonReply = QMessageBox.question(self, 'THE BOSS (grorp 98)', "Bạn muốn thoát ứng dụng?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.bt_thoat.setEnabled(True)
            exit()   
        else:
            print('cancel')
            self.bt_thoat.setEnabled(True)

        


    def nhandien(self):
        os.system('python Nhandien.py')

    def trogiup(self):
        os.system('python Trogiup1.py')

    def thongtin(self):
        os.system('python Thongtin.py')

    def admin(self):
        os.system('python Login.py')        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    Mainmenu = Mainmenu()
    Mainmenu.show()
    sys.exit(app.exec_())