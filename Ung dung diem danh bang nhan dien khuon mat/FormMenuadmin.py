# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormMenuadmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc

class Ui_Form_Menuadmin(object):
    def setupUi(self, Form_Menuadmin):
        Form_Menuadmin.setObjectName("Form_Menuadmin")
        Form_Menuadmin.resize(800, 500)
        Form_Menuadmin.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form_Menuadmin.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form_Menuadmin.setStyleSheet("QPushButton#bt_xemlich{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_xemlich:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_xemlich:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"QPushButton#bt_update1{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_update1:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_update1:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"QPushButton#bt_update2{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_update2:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_update2:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"QPushButton#bt_trogiup{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_trogiup:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_trogiup:hover{\n"
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
"}\n"
"QPushButton#bt_training{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_training:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_training:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}\n"
"QPushButton#bt_updateacc{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#bt_updateacc:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#bt_updateacc:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.label = QtWidgets.QLabel(Form_Menuadmin)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.label.setStyleSheet("border-image:url(:/backgroud/backgroud/dat15904627748632.jpg);\n"
"border-radius:5px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form_Menuadmin)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 531, 71))
        font = QtGui.QFont()
        font.setFamily("UVN Dzung Dakao")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 0)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form_Menuadmin)
        self.label_3.setGeometry(QtCore.QRect(190, 130, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.bt_xemlich = QtWidgets.QPushButton(Form_Menuadmin)
        self.bt_xemlich.setGeometry(QtCore.QRect(350, 200, 120, 45))
        font = QtGui.QFont()
        font.setFamily("UVN Dzung Dakao")
        font.setPointSize(10)
        font.setItalic(True)
        self.bt_xemlich.setFont(font)
        self.bt_xemlich.setObjectName("bt_xemlich")
        self.bt_update1 = QtWidgets.QPushButton(Form_Menuadmin)
        self.bt_update1.setGeometry(QtCore.QRect(350, 260, 120, 45))
        font = QtGui.QFont()
        font.setFamily("UVN Dzung Dakao")
        font.setPointSize(10)
        font.setItalic(True)
        self.bt_update1.setFont(font)
        self.bt_update1.setObjectName("bt_update1")
        self.bt_update2 = QtWidgets.QPushButton(Form_Menuadmin)
        self.bt_update2.setGeometry(QtCore.QRect(350, 320, 120, 45))
        font = QtGui.QFont()
        font.setFamily("UVN Dzung Dakao")
        font.setPointSize(10)
        font.setItalic(True)
        self.bt_update2.setFont(font)
        self.bt_update2.setObjectName("bt_update2")
        self.bt_trogiup = QtWidgets.QPushButton(Form_Menuadmin)
        self.bt_trogiup.setGeometry(QtCore.QRect(350, 390, 120, 40))
        font = QtGui.QFont()
        font.setFamily("UVN Dzung Dakao")
        font.setPointSize(10)
        font.setItalic(True)
        self.bt_trogiup.setFont(font)
        self.bt_trogiup.setObjectName("bt_trogiup")
        self.bt_training = QtWidgets.QPushButton(Form_Menuadmin)
        self.bt_training.setGeometry(QtCore.QRect(620, 320, 120, 40))
        font = QtGui.QFont()
        font.setFamily("UVN Dzung Dakao")
        font.setPointSize(10)
        font.setItalic(True)
        self.bt_training.setFont(font)
        self.bt_training.setObjectName("bt_training")
        self.bt_back = QtWidgets.QPushButton(Form_Menuadmin)
        self.bt_back.setGeometry(QtCore.QRect(10, 10, 93, 28))
        font = QtGui.QFont()
        font.setFamily("UVN Dzung Dakao")
        font.setPointSize(10)
        font.setItalic(True)
        self.bt_back.setFont(font)
        self.bt_back.setObjectName("bt_back")
        self.bt_updateacc = QtWidgets.QPushButton(Form_Menuadmin)
        self.bt_updateacc.setGeometry(QtCore.QRect(620, 260, 120, 40))
        font = QtGui.QFont()
        font.setFamily("UVN Dzung Dakao")
        font.setPointSize(8)
        font.setItalic(True)
        self.bt_updateacc.setFont(font)
        self.bt_updateacc.setObjectName("bt_updateacc")

        self.retranslateUi(Form_Menuadmin)
        QtCore.QMetaObject.connectSlotsByName(Form_Menuadmin)

    def retranslateUi(self, Form_Menuadmin):
        _translate = QtCore.QCoreApplication.translate
        Form_Menuadmin.setWindowTitle(_translate("Form_Menuadmin", "Form"))
        self.label_2.setText(_translate("Form_Menuadmin", "Chào mừng đến với chế độ quản lý"))
        self.label_3.setText(_translate("Form_Menuadmin", "Welcome to management mode"))
        self.bt_xemlich.setText(_translate("Form_Menuadmin", "Xem lịch"))
        self.bt_update1.setText(_translate("Form_Menuadmin", "Cập nhật\n"
"Thông tin"))
        self.bt_update2.setText(_translate("Form_Menuadmin", "Xóa\n"
" Nhân viên"))
        self.bt_trogiup.setText(_translate("Form_Menuadmin", "Trợ giúp"))
        self.bt_training.setText(_translate("Form_Menuadmin", "Training Data"))
        self.bt_back.setText(_translate("Form_Menuadmin", "Back"))
        self.bt_updateacc.setText(_translate("Form_Menuadmin", "Cập nhật\n"
" Tài Khoản"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Menuadmin = QtWidgets.QWidget()
    ui = Ui_Form_Menuadmin()
    ui.setupUi(Form_Menuadmin)
    Form_Menuadmin.show()
    sys.exit(app.exec_())