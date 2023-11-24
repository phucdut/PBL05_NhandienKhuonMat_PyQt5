
from sqlite3.dbapi2 import connect
from PyQt5 import QtGui, QtWidgets, QtSql, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
from PyQt5.sip import delete
import FormUpdate1
from FormUpdate1 import Ui_FormUpdate1
import sys
import cv2
import numpy as np
import sqlite3
import os



class Update1(QtWidgets.QWidget, Ui_FormUpdate1):
    def __init__(self):
        super(Update1, self).__init__()
        self.setupUi(self)
        self.bt_hienthi.clicked.connect(self.loadData)
        self.bt_capnhat.clicked.connect(self.updateData)
        self.bt_thoat.clicked.connect(self.exit)
        self.bt_timkiem.clicked.connect(self.timkiem)
    
    def exit(self):
        exit()

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

    def updateData(self):
        id = self.line_id.text()
        name = self.line_name.text()
        age = self.line_age.text()
        gender = self.line_gender.text()
        phone = self.line_phone.text()
        address = self.line_address.text()

        flags = 0
        while(flags == 0):
            if len(str(id)) == 0 or len(name) == 0 or len(str(age)) == 0 or len(gender) == 0 or len(str(phone)) == 0 or len(address) == 0:

                flags =0
                self.error.setText("Bạn phải nhập đầy đủ thông tin!")
                break
            
            try:
                id = int(id)
                age = int(age)
                phone = int(phone)
                flags = 1
                self.error.setText("")
                def insertOrUpdate(id, name, age, gender, phone, address):
                    conn = sqlite3.connect('‪FaceData.db')

                    query1 = "SELECT * FROM people WHERE ID="+str(id)
                    try:
                        cursor = conn.execute(query1)

                    except sqlite3.OperationalError:
                        query = " CREATE TABLE people ( ID CHAR (10, 20)    NOT NULL  PRIMARY KEY,Name    VARCHAR (30, 40) NOT NULL,Age     INTEGER (10, 20),Gender  CHAR (20, 30),Phone   NUMERIC (0, 11),Address VARCHAR (150) );"

                        conn.execute(query)
                        cursor = conn.execute(query1)
                        conn.commit()

                    global isRecordExist
                    isRecordExist = 0
                    for row in cursor:
                        isRecordExist = 1

                    if(isRecordExist == 0):
                        query = "INSERT INTO people (ID, Name, Age, Gender, Phone, Address) VALUES("+str(
                            id)+",'"+str(name)+"','"+str(age)+"','"+str(gender)+"',"+str(phone)+",'"+str(address)+"')"
                        print("Thêm thông tin thành công")
                    else:
                        query = "UPDATE people SET Name = '"+str(name)+"',Age = '"+str(age)+"',Gender = '"+str(
                            gender)+"',Phone = "+str(phone)+",Address = '"+str(address)+"' WHERE ID="+str(id)
                        print("Cập nhật thông tin thành công")
                    conn.execute(query)
                    conn.commit()
                    conn.close()
                QMessageBox.about(self, "THE BOSS(group 98)", "Cập nhật thành công!")
                insertOrUpdate(id, name, age, gender, phone, address)

                if(isRecordExist == 1):
                    print("UPDATE Thành Công")

                if(isRecordExist == 0):

                    #load thu vien
                    QMessageBox.about(self, "THE BOSS(group 98)", "Bạn vừa thêm nhân viên mới!\n Camera sắp bật trong 10s hãy quay các góc mặt\nđể thuận tiện cho việc cập nhật thông tin!")
                    face_cascade = cv2.CascadeClassifier(
                        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                    cap = cv2.VideoCapture(0)

                    sampleNum = 0

                    while(True):
                        ret, frame = cap.read()
                        cv2.imshow('FaceDetecting', frame)
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                        for (x, y, w, h) in faces:
                            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                            if not os.path.exists("dataSet"):
                                os.makedirs("dataSet")

                            sampleNum += 1

                            cv2.imwrite(
                                "dataSet/User."+str(id)+"."+str(sampleNum)+".jpg", gray[y:y+h, x:x+w])

                    #  cv2.imshow('FaceDetecting', frame)
                        cv2.waitKey(1)

                        if sampleNum > 150:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    QMessageBox.about(self, "THE BOSS(group 98)", "Thêm thành công")
                        
            except ValueError:

                flags =0
                self.error.setText("Bạn nhập sai định dạng!")
                break
        
        
        


        # def insertOrUpdate(id, name, age, gender, phone, address):
        #     conn = sqlite3.connect('‪FaceData.db')

        #     query1 = "SELECT * FROM people WHERE ID="+str(id)
        #     try:
        #         cursor = conn.execute(query1)

        #     except sqlite3.OperationalError:
        #         query = " CREATE TABLE people ( ID CHAR (10, 20)    NOT NULL  PRIMARY KEY,Name    VARCHAR (30, 40) NOT NULL,Age     INTEGER (10, 20),Gender  CHAR (20, 30),Phone   NUMERIC (0, 11),Address VARCHAR (150) );"

        #         conn.execute(query)
        #         cursor = conn.execute(query1)
        #         conn.commit()

        #     global isRecordExist
        #     isRecordExist = 0
        #     for row in cursor:
        #         isRecordExist = 1

        #     if(isRecordExist == 0):
        #         query = "INSERT INTO people (ID, Name, Age, Gender, Phone, Address) VALUES("+str(
        #             id)+",'"+str(name)+"','"+str(age)+"','"+str(gender)+"',"+str(phone)+",'"+str(address)+"')"
        #         print("Thêm thông tin thành công")
        #     else:
        #         query = "UPDATE people SET Name = '"+str(name)+"',Age = '"+str(age)+"',Gender = '"+str(
        #             gender)+"',Phone = "+str(phone)+",Address = '"+str(address)+"' WHERE ID="+str(id)
        #         print("Cập nhật thông tin thành công")
        #     conn.execute(query)
        #     conn.commit()
        #     conn.close()

        # insertOrUpdate(id, name, age, gender, phone, address)

        # if(isRecordExist == 1):
        #     print("UPDATE Thành Công")

        # if(isRecordExist == 0):

        #     #load thu vien

        #     face_cascade = cv2.CascadeClassifier(
        #         cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        #     cap = cv2.VideoCapture(0)

        #     sampleNum = 0

        #     while(True):
        #         ret, frame = cap.read()
        #         cv2.imshow('FaceDetecting', frame)
        #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #         faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #         for (x, y, w, h) in faces:
        #             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        #             if not os.path.exists("dataSet"):
        #                 os.makedirs("dataSet")

        #             sampleNum += 1

        #             cv2.imwrite(
        #                 "dataSet/User."+str(id)+"."+str(sampleNum)+".jpg", gray[y:y+h, x:x+w])

        #     #  cv2.imshow('FaceDetecting', frame)
        #         cv2.waitKey(1)

        #         if sampleNum > 150:
        #             break

        #     cap.release()
        #     cv2.destroyAllWindows()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    FormUpdate1 = Update1()
    FormUpdate1.show()
    sys.exit(app.exec_())
