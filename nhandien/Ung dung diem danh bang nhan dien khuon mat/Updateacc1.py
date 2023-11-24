from PyQt5 import QtGui, QtWidgets, QtSql, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
from FormUpdateacc1 import Ui_Form_Updateacc1
import sys
import os

class FUpdateacc1(QtWidgets.QWidget, Ui_Form_Updateacc1):
    def __init__(self):
        super(FUpdateacc1, self).__init__()
        self.setupUi(self)
        self.openDB()
        self.bt_back.clicked.connect(self.exit)
        self.bt_update.clicked.connect(self.checkUser)
        
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
        password2 = self.line_passwordupdate1.text()
        password3 = self.line_passwordupdate2.text()

        if len(username1) == 0 or len(password1) == 0 or len(password2) == 0 or len(password3) == 0:
            self.error.setText("Hãy nhập đầy đủ thông tin!")
        else:
            self.query.exec_("select * from admin where username = '%s' and password ='%s';"%(username1, password1) )
            self.query.first()
            if self.query.value("username") != None and self.query.value("password") !=None:
                if password2 != password3:
                    self.error.setText("Mật khẩu mới không trùng nhau!")
                else:
                    self.query.exec_("UPDATE admin SET password ='%s' WHERE username ='%s';"%(password2,username1))
                    self.query.first()
                    self.error.setText("")
                    QMessageBox.question(self, "THE BOSS(group 98)", "Cập nhật mật khẩu thành công!",QMessageBox.Ok)
                
            else:
                self.error.setText("Thông tin tài khoản hoặc\nmật khẩu không chính xác!")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    FUpdateacc1 = FUpdateacc1()
    FUpdateacc1.show()
    sys.exit(app.exec_())