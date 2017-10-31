# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\gongyixitong\gongyixitong\ui\login.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.setWindowModality(QtCore.Qt.WindowModal)
        login.resize(400, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMinimumSize(QtCore.QSize(400, 200))
        login.setMaximumSize(QtCore.QSize(400, 200))
        login.setBaseSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        login.setFont(font)
        login.setWhatsThis("")
        login.setStyleSheet("")
        login.setSizeGripEnabled(True)
        self.layoutWidget = QtWidgets.QWidget(login)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 321, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "登陆"))
        self.label_3.setText(_translate("login", "密  码："))
        self.lineEdit_4.setText(_translate("login", "admin"))
        self.label_4.setText(_translate("login", "用户名："))
        self.pushButton.setWhatsThis(_translate("login", "<html><head/><body><p>开奖号蓝海看</p></body></html>"))
        self.pushButton.setText(_translate("login", "登陆"))
        self.pushButton_2.setText(_translate("login", "退出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

