# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormUpdateacc1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Updateacc1(object):
    def setupUi(self, Form_Updateacc1):
        Form_Updateacc1.setObjectName("Form_Updateacc1")
        Form_Updateacc1.resize(800, 500)
        Form_Updateacc1.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form_Updateacc1.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form_Updateacc1.setStyleSheet("QPushButton#bt_update{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_update:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_update:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"QPushButton#bt_back{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_back:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_back:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label = QtWidgets.QLabel(Form_Updateacc1)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.label.setStyleSheet("border-image: url(:/backgroud/backgroud/b7.jpg);\n"
"border-radius:5px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form_Updateacc1)
        self.label_2.setGeometry(QtCore.QRect(260, 60, 311, 71))
        font = QtGui.QFont()
        font.setFamily("UVN Dzung Dakao")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 0)")
        self.label_2.setObjectName("label_2")
        self.line_username = QtWidgets.QLineEdit(Form_Updateacc1)
        self.line_username.setGeometry(QtCore.QRect(270, 150, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_username.setFont(font)
        self.line_username.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 255, 0);\n"
"color:rgb(255, 255, 0);\n"
"padding-bottom:7px;\n"
"")
        self.line_username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_username.setObjectName("line_username")
        self.line_password = QtWidgets.QLineEdit(Form_Updateacc1)
        self.line_password.setGeometry(QtCore.QRect(270, 210, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_password.setFont(font)
        self.line_password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 255, 0);\n"
"color:rgb(255, 255, 0);\n"
"padding-bottom:7px;\n"
"")
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setObjectName("line_password")
        self.line_passwordupdate1 = QtWidgets.QLineEdit(Form_Updateacc1)
        self.line_passwordupdate1.setGeometry(QtCore.QRect(270, 280, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_passwordupdate1.setFont(font)
        self.line_passwordupdate1.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 255, 0);\n"
"color:rgb(255, 255, 0);\n"
"padding-bottom:7px;\n"
"")
        self.line_passwordupdate1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_passwordupdate1.setObjectName("line_passwordupdate1")
        self.line_passwordupdate2 = QtWidgets.QLineEdit(Form_Updateacc1)
        self.line_passwordupdate2.setGeometry(QtCore.QRect(270, 350, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_passwordupdate2.setFont(font)
        self.line_passwordupdate2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgb(255, 255, 0);\n"
"color:rgb(255, 255, 0);\n"
"padding-bottom:7px;\n"
"")
        self.line_passwordupdate2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_passwordupdate2.setObjectName("line_passwordupdate2")
        self.bt_update = QtWidgets.QPushButton(Form_Updateacc1)
        self.bt_update.setGeometry(QtCore.QRect(310, 450, 150, 30))
        font = QtGui.QFont()
        font.setFamily("UVN Dzung Dakao")
        font.setPointSize(10)
        font.setItalic(True)
        self.bt_update.setFont(font)
        self.bt_update.setObjectName("bt_update")
        self.bt_back = QtWidgets.QPushButton(Form_Updateacc1)
        self.bt_back.setGeometry(QtCore.QRect(20, 20, 93, 28))
        font = QtGui.QFont()
        font.setFamily("UVN Dzung Dakao")
        font.setPointSize(10)
        font.setItalic(True)
        self.bt_back.setFont(font)
        self.bt_back.setObjectName("bt_back")
        self.error = QtWidgets.QLabel(Form_Updateacc1)
        self.error.setGeometry(QtCore.QRect(270, 400, 251, 41))
        font = QtGui.QFont()
        font.setItalic(True)
        self.error.setFont(font)
        self.error.setStyleSheet("color: rgb(255, 0, 0);")
        self.error.setText("")
        self.error.setObjectName("error")

        self.retranslateUi(Form_Updateacc1)
        QtCore.QMetaObject.connectSlotsByName(Form_Updateacc1)

    def retranslateUi(self, Form_Updateacc1):
        _translate = QtCore.QCoreApplication.translate
        Form_Updateacc1.setWindowTitle(_translate("Form_Updateacc1", "Form"))
        self.label_2.setText(_translate("Form_Updateacc1", "Cập nhật tài khoản"))
        self.line_username.setPlaceholderText(_translate("Form_Updateacc1", "Username"))
        self.line_password.setPlaceholderText(_translate("Form_Updateacc1", "Current password"))
        self.line_passwordupdate1.setPlaceholderText(_translate("Form_Updateacc1", "New password"))
        self.line_passwordupdate2.setPlaceholderText(_translate("Form_Updateacc1", "New password confirmation"))
        self.bt_update.setText(_translate("Form_Updateacc1", "Cập nhật"))
        self.bt_back.setText(_translate("Form_Updateacc1", "Back"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Updateacc1 = QtWidgets.QWidget()
    ui = Ui_Form_Updateacc1()
    ui.setupUi(Form_Updateacc1)
    Form_Updateacc1.show()
    sys.exit(app.exec_())
