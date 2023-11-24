
from PyQt5 import QtGui, QtWidgets, QtSql, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow,QMessageBox, QSplashScreen 
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from FormMenuadmin import Ui_Form_Menuadmin
import cv2
import numpy as np
import os
from PIL import Image

class Menuad(QtWidgets.QWidget,Ui_Form_Menuadmin ):
    def __init__(self):
        super(Menuad, self).__init__()
        self.setupUi(self)
        self.bt_xemlich.clicked.connect(self.xemlich)
        self.bt_update1.clicked.connect(self.openUpdate1)
        self.bt_update2.clicked.connect(self.openUpdate2)
        self.bt_updateacc.clicked.connect(self.updateacc1)
        self.bt_back.clicked.connect(self.exit)
        self.bt_training.clicked.connect(self.training)
        self.bt_trogiup.clicked.connect(self.trogiup)

    def xemlich(self):
        os.system('python Xemlich.py')
    def updateacc1(self):
        os.system('python Updateacc1.py')

    def exit(self):
        exit()

    def openUpdate1(self):
        os.system('python Update1.py')

    def openUpdate2(self):
        os.system('python Update2.py')

    def training(self):
        QMessageBox.about(self, 'THE BOSS (grorp 98)',"Training có thể mất từ 1p - 5p!\n Vui lòng không tắt ứng dụng trong quá trình Training!")
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        path = 'dataSet'


        def getImageWithId(path):
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

            # print(imagePaths)

            faces = []
            IDs = []

            for imagePath in imagePaths:

                faceImg = Image.open(imagePath).convert('L')

                faceNp = np.array(faceImg, 'uint8')

                print(faceNp)

                Id = int(imagePath.split('\\')[1].split('.')[1])

                faces.append(faceNp)
                IDs.append(Id)

                cv2.imshow('Training', faceNp)
                cv2.waitKey(10)

            return faces, IDs


        faces, Ids = getImageWithId(path)

        recognizer.train(faces, np.array(Ids))

        if not os.path.exists('recognizer'):
            os.makedirs('recognizer')

        recognizer.save('trainingData.yml')

        cv2.destroyAllWindows()

    def updateacc(self):
        pass

    def trogiup(self):
        os.system('python Trogiup.py')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    Form_Login = Menuad()
    Form_Login.show()
    sys.exit(app.exec_())