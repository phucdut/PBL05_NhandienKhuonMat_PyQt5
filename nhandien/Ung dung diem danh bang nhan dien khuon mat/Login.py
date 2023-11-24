from PyQt5 import QtGui, QtWidgets, QtSql, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from FormLogin import Ui_Form_Login
import win32gui,win32con
import sys
import os

class myApp(QtWidgets.QWidget, Ui_Form_Login):
    def __init__(self):
        #hiden console
        # hide = win32gui.GetForegroundWindow()
        # win32gui.ShowWindow(hide , win32con.SW_HIDE)
        super(myApp, self).__init__()
        self.setupUi(self)
        self.openDB()
        self.bt_login.clicked.connect(self.checkUser)
        self.bt_back.clicked.connect(self.exit)
        
    def exit(self):
        exit()
        
    def openDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.sqlite")
        if not self.db.open():
            print("Error")
        self.query = QtSql.QSqlQuery()

    
        

    def checkUser(self):
        username1 = self.line_username.text()
        password1 = self.line_password.text()

        if len(username1) == 0 or len(password1) == 0:
            self.error.setText("Hãy nhập đầy đủ thông tin!")
        else:
            
            self.query.exec_("select * from admin where username = '%s' and password ='%s';"%(username1, password1) )
            self.query.first()
            if self.query.value("username") != None and self.query.value("password") !=None:
                print("Đăng nhập thành công!")
                self.error.setText("")
                self.query.clear()
                os.system('python Menuadmin.py')
            else:
                self.error.setText("Thông tin tài khoản hoặc\nmật khẩu không chính xác!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    Form_Login = myApp()
    Form_Login.show()
    sys.exit(app.exec_())