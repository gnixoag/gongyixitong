# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\gongyixitong\gongyixitong\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 720)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 0, 421, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 931, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 80, 931, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        self.menu_BOM = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.menu_BOM.setFont(font)
        self.menu_BOM.setObjectName("menu_BOM")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewBOM = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.actionNewBOM.setFont(font)
        self.actionNewBOM.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionNewBOM.setObjectName("actionNewBOM")
        self.actionSHBOM = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.actionSHBOM.setFont(font)
        self.actionSHBOM.setObjectName("actionSHBOM")
        self.actionSCBOM = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.actionSCBOM.setFont(font)
        self.actionSCBOM.setObjectName("actionSCBOM")
        self.actionGYSJ = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.actionGYSJ.setFont(font)
        self.actionGYSJ.setObjectName("actionGYSJ")
        self.actionabout = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.actionabout.setFont(font)
        self.actionabout.setObjectName("actionabout")
        self.actionMKPZ = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.actionMKPZ.setFont(font)
        self.actionMKPZ.setObjectName("actionMKPZ")
        self.actionYHGL = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.actionYHGL.setFont(font)
        self.actionYHGL.setObjectName("actionYHGL")
        self.actionYHZGL = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.actionYHZGL.setFont(font)
        self.actionYHZGL.setObjectName("actionYHZGL")
        self.menu_BOM.addAction(self.actionNewBOM)
        self.menu_BOM.addAction(self.actionSHBOM)
        self.menu_BOM.addAction(self.actionSCBOM)
        self.menu_BOM.addAction(self.actionGYSJ)
        self.menu.addAction(self.actionMKPZ)
        self.menu.addAction(self.actionYHGL)
        self.menu.addAction(self.actionYHZGL)
        self.menu_2.addAction(self.actionabout)
        self.menubar.addAction(self.menu_BOM.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "面向MES系统的CAPP开发"))
        self.label.setText(_translate("MainWindow", "设计BOM表结构表单管理--"))
        self.label_2.setText(_translate("MainWindow", "新建"))
        self.pushButton.setText(_translate("MainWindow", "新增"))
        self.pushButton_2.setText(_translate("MainWindow", "修改"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))
        self.pushButton_4.setText(_translate("MainWindow", "刷新"))
        self.menu_BOM.setTitle(_translate("MainWindow", "工艺BOM"))
        self.menu.setTitle(_translate("MainWindow", "系统配置"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.actionNewBOM.setText(_translate("MainWindow", "新建BOM"))
        self.actionSHBOM.setText(_translate("MainWindow", "审核BOM"))
        self.actionSCBOM.setText(_translate("MainWindow", "输出BOM"))
        self.actionGYSJ.setText(_translate("MainWindow", "工艺设计"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.actionMKPZ.setText(_translate("MainWindow", "模块配置"))
        self.actionYHGL.setText(_translate("MainWindow", "用户管理"))
        self.actionYHZGL.setText(_translate("MainWindow", "用户组管理"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
