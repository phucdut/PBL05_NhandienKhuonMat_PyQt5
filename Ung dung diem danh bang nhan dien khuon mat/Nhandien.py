# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.uic import loadUi
# from PyQt5.QtCore import pyqtSlot, QTimer, QDate
# from PyQt5.QtWidgets import QMessageBox, QApplication
# import cv2
# import datetime
# import os
# import sqlite3
# from PyQt5 import  QtWidgets
# from FormNhandien import Ui_FormNhandien
# import sys
# import win32gui,win32con

# class MainWindow(QtWidgets.QWidget, Ui_FormNhandien):
    
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)   
#         self.image = None
#         self.ID= None
#         self.Name =None
#         self.status1 = "Bắt đầu"
#         self.status2 = "Kết thúc"
#         #hiden console
#         hide = win32gui.GetForegroundWindow()
#         win32gui.ShowWindow(hide , win32con.SW_HIDE)

#         self.bt_camera.clicked.connect(self.start_webcam)
#         self.bt_start.clicked.connect(self.writefile1)
#         self.bt_end.clicked.connect(self.writefile2)

#         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#         self.recognizer = cv2.face.LBPHFaceRecognizer_create()
#         self.recognizer.read('trainingData.yml')

#         #update_time_and_Date
#         now = QDate.currentDate()
#         current_date = now.toString('ddd dd MMMM yyyy')
#         current_time = datetime.datetime.now().strftime("%I:%M %p")
#         self.Date_Lable.setText(current_date)
#         self.Time_Lable.setText(current_time)
        
#         self.bt_back.clicked.connect(self.exit)
#         self.bt_xemlich.clicked.connect(self.xemlich)
#         self.bt_trogiup.clicked.connect(self.trogiup)

#     def trogiup(self):
#         os.system('python Trogiup.py')

#     def xemlich(self):
#         os.system('python Xemlich.py')

#     def exit(self):
#         exit()
        
#     def writefile1(self):
#         if self.Name == "None":
#             QMessageBox.about(self, "THE BOSS(group 98)", "Chưa nhận diện được!")
#         else:
#             self.bt_start.isChecked()
#             self.bt_start.setEnabled(False)
#             with open("DATAAttendance.csv", mode='a') as f:
#                 buttonReply = QMessageBox.question(self, 'THE BOSS (grorp 98)',"Bạn muốn bắt đầu ca làm?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#                 if buttonReply == QMessageBox.Yes:
#                     self.bt_start.setEnabled(True)
#                     now = QDate.currentDate()
#                     current_date = now.toString('ddd dd MMMM yyyy')
#                     current_time = datetime.datetime.now().strftime("%I:%M %p")
#                     f.writelines(f'\n{self.Name},{self.ID},{current_time},{current_date},start')
#                     self.Trangthai_Label.setText(self.status1)
#                 else:
#                     print('cancel')
#                     self.bt_start.setEnabled(True)
                   
#     def writefile2(self):
#         if self.Name == "None":
#             QMessageBox.about(self, "THE BOSS(group 98)", "Chưa nhận diện được!")
#         else:
#             self.bt_start.isChecked()
#             self.bt_start.setEnabled(False)
#             with open("DATAAttendance.csv", mode='a') as f:
#                 buttonReply = QMessageBox.question(self, 'THE BOSS (grorp 98)',"Bạn muốn kết thúc ca làm?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#                 if buttonReply == QMessageBox.Yes:
#                     self.bt_start.setEnabled(True)
#                     now = QDate.currentDate()
#                     current_date = now.toString('ddd dd MMMM yyyy')
#                     current_time = datetime.datetime.now().strftime("%I:%M %p")
#                     f.writelines(f'\n{self.Name},{self.ID},{current_time},{current_date},end')
#                     self.Trangthai_Label.setText(self.status2)
#                 else:
#                     print('cancel')
#                     self.bt_start.setEnabled(True)
        
#     def start_webcam(self):
#         QMessageBox.about(self, "THE BOSS(group 98)", "Việc bật camera có thể mất từ 5s - 1p!")
#         self.capture=cv2.VideoCapture(0)
#         self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
#         self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         self.timer=QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(5)

#     def update_frame(self):
#         ret,self.image=self.capture.read()
#         self.image=cv2.flip(self.image,1)
#         detected_image=self.detect_face(self.image)
#         self.displayImage(detected_image,1)

#     def detect_face(self,img):
#         def getProfile(id):
#             conn = sqlite3.connect('‪FaceData.db')
#             query = 'SELECT * FROM people WHERE ID=' + str(id)
#             cursor = conn.execute(query)
#             profile = None
#             for row in cursor:
#                 profile = row
#             conn.close()
#             return profile

#         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#         faces=self.face_cascade.detectMultiScale(gray,1.2,5,minSize=(90,90))
#         fontface = cv2.FONT_HERSHEY_SIMPLEX

#         for(x,y,w,h) in faces:
#             cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#             roi_gray = gray[y: y+h, x: x+w]
#             id, confidence = self.recognizer.predict(roi_gray)
#             if confidence < 60:
#                     profile = getProfile(id)
#                     if(profile != None):
#                         self.ID = str(profile[0])
#                         self.Name = str(profile[1])
#                         cv2.putText(
#                             img, "Name: "+str(profile[1]), (x+10, y+h+30), fontface, 1, (0, 255, 0), 2)
#                         cv2.putText(
#                             img, "Age: "+str(profile[2]), (x+10, y+h+60), fontface, 1, (0, 255, 0), 2)
#                         cv2.putText(
#                             img, "Gender: "+str(profile[3]), (x+10, y+h+90), fontface, 1, (0, 255, 0), 2)      
#             else:
#                         self.ID = " None"
#                         self.Name = "None"
#                         cv2.putText(
#                             img, "Unknow", (x+10, y+h+30),fontface, 1, (0, 0, 255), 2)
#         return img

#     def displayImage(self,img,window=1):
#         qformat=QImage.Format_Indexed8
#         if len(img.shape)==3:
#             if img.shape[2]==4:
#                 qformat=QImage.Format_RGBA8888
#             else:
#                 qformat=QImage.Format_RGB888

#         outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
#         #BGR>>RGB
#         outImage=outImage.rgbSwapped()
#         if window==1:
#             self.Camera_Label.setPixmap(QPixmap.fromImage(outImage))
#             self.Camera_Label.setScaledContents(True)
#             self.Id_Label.setText(self.ID)
#             self.Ten_Label.setText(self.Name)

# app = QApplication(sys.argv)
# widget = MainWindow()
# widget.show()
# sys.exit(app.exec_())


from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer, QDate
from PyQt5.QtWidgets import QMessageBox, QApplication
import cv2
import datetime
import os
import sqlite3
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical
from PyQt5 import QtWidgets
from FormNhandien import Ui_FormNhandien
import sys
import win32gui, win32con

class MainWindow(QtWidgets.QWidget, Ui_FormNhandien):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.image = None
        self.ID = None
        self.Name = None
        self.status1 = "Bắt đầu"
        self.status2 = "Kết thúc"
        # hidden console
        # hide = win32gui.GetForegroundWindow()
        # win32gui.ShowWindow(hide, win32con.SW_HIDE)
        
        self.img_label = QtWidgets.QLabel(self)
        
        self.bt_camera.clicked.connect(self.start_webcam)
        self.bt_start.clicked.connect(self.writefile1)
        self.bt_end.clicked.connect(self.writefile2)

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        self.model = Sequential()
        self.model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(90, 90, 1)))
        self.model.add(MaxPooling2D((2, 2)))
        self.model.add(Flatten())
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(4, activation='softmax'))
        self.model.load_weights('face_model.h5')

        # update_time_and_Date
        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.Date_Lable.setText(current_date)
        self.Time_Lable.setText(current_time)

        self.bt_back.clicked.connect(self.exit)
        self.bt_xemlich.clicked.connect(self.xemlich)
        self.bt_trogiup.clicked.connect(self.trogiup)

    def trogiup(self):
        os.system('python Trogiup.py')

    def xemlich(self):
        os.system('python Xemlich.py')

    def exit(self):
        exit()

    def writefile1(self):
        if self.Name == "None":
            QMessageBox.about(self, "THE BOSS(group 11)", "Chưa nhận diện được!")
        else:
            self.bt_start.isChecked()
            self.bt_start.setEnabled(False)
            #with open("DATAAttendance.csv", mode='a') as f:
            with open("DATAAttendance.csv", mode='a', encoding='utf-8') as f:
                buttonReply = QMessageBox.question(self, 'THE BOSS (grorp 11)',
                                                   "Bạn muốn bắt đầu ca làm?", QMessageBox.Yes | QMessageBox.No,
                                                   QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.bt_start.setEnabled(True)
                    now = QDate.currentDate()
                    current_date = now.toString('ddd dd MMMM yyyy')
                    current_time = datetime.datetime.now().strftime("%I:%M %p")
                    # f.writelines(f'\n{self.Name},{self.ID},{current_time},{current_date},start')
                    f.write(f'{self.Name},{self.ID},{current_time},{current_date},start\n')
                    self.Trangthai_Label.setText(self.status1)
                else:
                    print('cancel')
                    self.bt_start.setEnabled(True)

    def writefile2(self):
        if self.Name == "None":
            QMessageBox.about(self, "THE BOSS(group 98)", "Chưa nhận diện được!")
        else:
            self.bt_start.isChecked()
            self.bt_start.setEnabled(False)
            with open("DATAAttendance.csv", mode='a', encoding='utf-8') as f:
                buttonReply = QMessageBox.question(self, 'THE BOSS (grorp 98)',
                                                   "Bạn muốn kết thúc ca làm?", QMessageBox.Yes | QMessageBox.No,
                                                   QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.bt_start.setEnabled(True)
                    now = QDate.currentDate()
                    current_date = now.toString('ddd dd MMMM yyyy')
                    current_time = datetime.datetime.now().strftime("%I:%M %p")
                    f.write(f'{self.Name},{self.ID},{current_time},{current_date},end\n')
                    self.Trangthai_Label.setText(self.status2)
                else:
                    print('cancel')
                    self.bt_start.setEnabled(True)

    def start_webcam(self):
        QMessageBox.about(self, "THE BOSS(group 98)", "Việc bật camera có thể mất từ 5s - 1p!")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.image = cv2.flip(self.image, 1)
        detected_image = self.detect_face(self.image)
        self.displayImage(detected_image, 1)

    def detect_face(self, img):
        def getProfile(id):
            conn = sqlite3.connect('‪FaceData.db')
            query = 'SELECT * FROM people WHERE ID=' + str(id)
            cursor = conn.execute(query)
            profile = None
            for row in cursor:
                profile = row
            conn.close()
            return profile

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.2, 5, minSize=(90, 90))
        fontface = cv2.FONT_HERSHEY_SIMPLEX

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y: y + h, x: x + w]
            roi_gray = cv2.resize(roi_gray, (90, 90))
            roi_gray = np.expand_dims(roi_gray, axis=-1)
            roi_gray = np.expand_dims(roi_gray, axis=0)
            prediction = self.model.predict(roi_gray)
            if np.argmax(prediction) == 1 and np.max(prediction) > 0.6:
                profile = getProfile(np.argmax(prediction))
                if profile is not None:
                    self.ID = str(profile[0])
                    self.Name = str(profile[1])
                    cv2.putText(
                        img, "Name: " + str(profile[1]), (x + 10, y + h + 30), fontface, 1, (0, 255, 0), 2)
                    cv2.putText(
                        img, "Age: " + str(profile[2]), (x + 10, y + h + 60), fontface, 1, (0, 255, 0), 2)
                    cv2.putText(
                        img, "Gender: " + str(profile[3]), (x + 10, y + h + 90), fontface, 1, (0, 255, 0), 2)
                    cv2.putText(
                        img, "Status: " + str(profile[4]), (x + 10, y + h + 120), fontface, 1, (0, 255, 0), 2)
                    cv2.putText(
                        img, "Address: " + str(profile[5]), (x + 10, y + h + 150), fontface, 1, (0, 255, 0), 2)
            else:
                self.ID = None
                self.Name = "None"

        return img

    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3:
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888

        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        #BGR>>RGB
        outImage=outImage.rgbSwapped()
        if window==1:
            self.Camera_Label.setPixmap(QPixmap.fromImage(outImage))
            self.Camera_Label.setScaledContents(True)
            self.Id_Label.setText(self.ID)
            self.Ten_Label.setText(self.Name)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())