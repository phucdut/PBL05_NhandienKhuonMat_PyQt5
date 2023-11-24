import os
import sys
from os.path import dirname, realpath, join
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUiType
import pandas as pd
from FormXemlich import Ui_Form_Xemlich

class FXemlich(QWidget,Ui_Form_Xemlich):
    def __init__(self):
        super(FXemlich, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)

        self.bt_back.clicked.connect(self.exit)
        self.bt_hienthi.clicked.connect(self.dataHead)

    def exit(self):
        exit()

    def dataHead(self):
        # filecsv = "DATAAttendance.csv"
        path = "DATAAttendance.csv"
        self.all_data = pd.read_csv(path)
        numColomn = len(self.all_data.index)
        self.tableWidget.setColumnCount(len(self.all_data.columns))
        self.tableWidget.setRowCount(numColomn)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numColomn):
            for j in range(len(self.all_data.columns)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    FXemlich = FXemlich()
    FXemlich.show()
    sys.exit(app.exec_())   