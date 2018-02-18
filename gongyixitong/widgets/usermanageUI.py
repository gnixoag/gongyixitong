#!/usr/bin/env python
# coding=utf-8
'''
#用户登陆界面

@author: gaoxing
'''

import sys

from PyQt5.Qt import QTableWidget, QToolBar
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from gongyixitong.test.dbDingyi import *


class UserManageUI(QDialog):
    '''
    显示用户信息的界面
    '''

    def __init__(self, parent=None):
        super().__init__()
        self._setupUI()
        self.setWindowTitle("用户管理")
        self.setWindowFlags(self.windowFlags() &
                            ~Qt.WindowContextHelpButtonHint)  # 隐藏？按钮
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        self.resize(800, 400)

    def _setupUI(self):
        newuseraction = QAction("新增", self)
        mdaction = QAction("修改", self)
        delaction = QAction("删除", self)
        sxaction = QAction("刷新", self)
        printaction = QAction("打印", self)
        exitaction = QAction("退出", self)

        toolbar = QToolBar("工具栏")
        toolbar.addAction(newuseraction)
        toolbar.addAction(mdaction)
        toolbar.addAction(delaction)
        toolbar.addAction(sxaction)
        toolbar.addAction(printaction)
        toolbar.addAction(exitaction)

        viewtable = QTableView()
        userdata = MyTableModel(datain=d)
        viewtable.setModel(userdata)
        # viewtable.setHorizontalHeaderLabels(['用户名','组名','组说明','ERP用户代码'])
        viewtable.verticalHeader().setVisible(False)  # 不显示
        viewtable.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不能编辑
        viewtable.setSelectionBehavior(QAbstractItemView.SelectRows)  # 只能选择行
        # viewtable.horizontalHeader().setSectionResizeMode(1)
        viewtable.resizeColumnsToContents()  # 列宽自适应内容
        viewtable.setAlternatingRowColors(True)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(viewtable)

        self.setLayout(layout)
        print("dlfaadf")

        exitaction.triggered.connect(self.close)
        mdaction.triggered.connect(self.mduser)

    def mduser(self):
        print("测试成功")
        b = MDuserUI(parent=self)
        b.exec_()


class MyTableModel(QAbstractTableModel):

    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0].nameid())

    def data(self, index, role=Qt.DisplayRole):
        a = self.arraydata[index.row()].nameid()
        if role == Qt.TextAlignmentRole:
            return Qt.AlignVCenter
        elif role != Qt.DisplayRole:
            return QVariant()
        return getattr(self.arraydata[index.row()], str(a[index.column()]))

    def headerData(self, col, orientation, role):
        a = self.arraydata[0].namechiness()

        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(a[col])
        # elif role== Qt.SizeHintRole :
        #   return QVariant(QSize(200,20))
        return QVariant()

    def setData(self, index, value, role):
        print("setData", index.row(), index.column(), value)


class MDuserUI(QDialog):
    '''
    修改用户
    '''

    def __init__(self, parent=None):
        super(QDialog, self).__init__()
        self.setupUI()
        self.setWindowTitle("用户编辑")
        self.resize(400, 200)
        self.setWindowFlags(self.windowFlags() &
                            ~Qt.WindowContextHelpButtonHint)  # 隐藏？按钮

    def setupUI(self):
        saveaction = QAction("保存并关闭", self)
        canaction = QAction("取消并退出", self)

        toolbar = QToolBar("工具栏")
        toolbar.addAction(saveaction)
        toolbar.addAction(canaction)

        lename = QLineEdit()
        lepassword = QLineEdit()
        lepassword.setEchoMode(QLineEdit.Password)
        usergroup = QComboBox()
        usergroup.addItems(["管理员组", "查询组", "设计组", "审核组", 'PDM专员组'])

        formlayou = QFormLayout()
        formlayou.addRow(QLabel('用户名:'), lename)
        formlayou.addRow(QLabel('密  码:'), lepassword)
        formlayou.addRow(QLabel('用户组:'), usergroup)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addLayout(formlayou)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    user = UserManageUI()
    user.show()
    sys.exit(app.exec_())
