# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.uic import loadUi
# from PyQt5.QtCore import pyqtSlot, QTimer, QDate
# from PyQt5.QtWidgets import QMessageBox, QApplication
# import cv2
# import datetime
# import os
# import sqlite3
# import numpy as np
# import tensorflow as tf
# from keras.models import Sequential
# from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# from keras.utils import to_categorical
# from PyQt5 import QtWidgets
# from FormNhandien import Ui_FormNhandien
# import sys
# import win32gui, win32con

# class MainWindow(QtWidgets.QWidget, Ui_FormNhandien):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)
#         self.image = None
#         self.ID = None
#         self.Name = None
#         self.status1 = "Bắt đầu"
#         self.status2 = "Kết thúc"
#         # hidden console
#         # hide = win32gui.GetForegroundWindow()
#         # win32gui.ShowWindow(hide, win32con.SW_HIDE)
        
#         self.img_label = QtWidgets.QLabel(self)
        
#         self.bt_camera.clicked.connect(self.start_webcam)
#         self.bt_start.clicked.connect(self.writefile1)
#         self.bt_end.clicked.connect(self.writefile2)

#         # self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#         # self.model = Sequential()
#         # self.model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(90, 90, 1)))
#         # self.model.add(MaxPooling2D((2, 2)))
#         # self.model.add(Flatten())
#         # self.model.add(Dense(128, activation='relu'))
#         # self.model.add(Dense(4, activation='softmax'))
#         # self.model.load_weights('face_model.h5')

#         # update_time_and_Date
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

    

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.show()
#     sys.exit(app.exec_())