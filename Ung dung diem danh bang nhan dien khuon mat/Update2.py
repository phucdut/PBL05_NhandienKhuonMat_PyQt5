from sqlite3.dbapi2 import connect
from PyQt5 import QtGui, QtWidgets, QtCore, QtSql
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
from PyQt5.sip import delete
import FormUpdate1
from FormUpdate2 import Ui_Form
import sys
import cv2
import numpy as np
import sqlite3
import os


class Update2(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Update2, self).__init__()
        self.setupUi(self)
        # self.openDB()
        self.bt_hienthi.clicked.connect(self.loadData)
        self.bt_xoa.clicked.connect(self.xoa)
        self.bt_back.clicked.connect(self.exit)
        self.bt_timkiem.clicked.connect(self.timkiem)

    def exit(self):
        exit()

    def xoa(self):
        id = self.line_id.text()

        if len(id) == 0:
            self.error.setText("Bạn chưa nhập ID!") 
        else:
            self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName("‪FaceData.db")
            if not self.db.open():
                print("Error")
            self.query = QtSql.QSqlQuery()
            self.query.exec_("SELECT * FROM people WHERE ID = '%s';"%(id))
            self.query.first()
        
            if self.query.value("ID") != None:
                print("thành công")
                self.db.close()
                self.error.setText("") 
                for i in range(1,152):
                    os.remove("dataSet/User."+str(id)+"."+str(i)+".jpg")
                # print("xoa thanh cong")
                
                connection= sqlite3.connect("‪FaceData.db")
                query =" DELETE FROM people WHERE ID="+str(id)+";"
                connection.execute(query)
                connection.commit()
                connection.close()
                QMessageBox.about(self, "THE BOSS(group 98)", "Xóa thành công!")
                
            else:
                self.error.setText("ID này không tồn tại!")
    
    def timkiem(self):
        #tìm kiếm theo id
        id = self.line_id_2.text()

        if len(id) == 0:
            self.error_2.setText("Bạn chưa nhập ID!") 
        else:
            self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName("D:\ok\‪FaceData.db")
            if not self.db.open():
                print("Error")
            self.query = QtSql.QSqlQuery()
            self.query.exec_("SELECT * FROM people WHERE ID = '%s';"%(id))
            self.query.first()
            if self.query.value("ID") != None:
                    print("thành công")
                    self.db.close()
                    self.error_2.setText("")
                    connection = sqlite3.connect("‪FaceData.db")
                    query = "SELECT *FROM people WHERE ID="+str(id)+";"
                    result = connection.execute(query)
                    self.tableWidget.setRowCount(0)
                    for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(
                                row_number, column_number, QtWidgets.QTableWidgetItem(str(data))) 
            else:
                    self.error_2.setText("ID này không tồn tại!")

    def loadData(self):
        connection = sqlite3.connect("‪FaceData.db")
        query = "SELECT *FROM people"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    FormUpdate1 = Update2()
    FormUpdate1.show()
    sys.exit(app.exec_())   
    