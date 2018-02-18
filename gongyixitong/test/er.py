'''
Created on 2018年1月17日

@author: gaoxing
'''
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import app
import sys


def windowd():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle("高星")
    lable1 = QtWidgets.QLabel(w)
    lable1.setText("lkasjdla :lsdajf ")
    lable1.move(100, 100)
    w.setGeometry(100, 100, 300, 300)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    windowd()
