#!/usr/bin/env python
'''
#用户登陆界面
    
@author: gaoxing
'''

import base64
import os
import sys
from hashlib import sha512
from hmac import HMAC

from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from gongyixitong.modle.encrypt import *


class UI_login(QDialog, Encrypt):
    '''
    #用户登入界面
    '''

    def __init__(self, parent=None):
        super(QDialog, self).__init__()
        self.initUI()

    def initUI(self):
        '''
        初始化界面
        '''

        self.setWindowTitle("面向MES系统的CAPP-用户登陆")
        self.resize(400, 180)
        self.setFixedSize(self.size())
        self.setWindowFlags(self.windowFlags() &
                            ~Qt.WindowContextHelpButtonHint)
        QApplication.setStyle(QStyleFactory.create("Fusion"))

        self.button()
        self.logingroup()
        self.layout()
        self.connectqb()

    def connectqb(self):
        self.pbCancel.clicked.connect(self.close)
        self.pbLogin.clicked.connect(self.pbloginclicked)

    def pbloginclicked(self):
        username = self.cbName.currentText()
        username = self.encrypt(username)
        password = self.lePassword.text()
        password = self.encrypt(password)

        if self.validate(username, "gaoxing") and self.validate(password, " "):
            # QMessageBox.information(None, "登陆提示", "用户名："+username+"\n密码："+password+"\n登陆成功", QMessageBox.Ok, QMessageBox.Cancel)
            self.accept()
        else:
            QMessageBox.critical(None, "登陆提示", "用户名或密码错误", QMessageBox.Ok)

    def button(self):
        self.pbLogin = QPushButton("登入")
        self.pbCancel = QPushButton("取消")
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addStretch()
        self.buttonLayout.addWidget(self.pbLogin)
        self.buttonLayout.addWidget(self.pbCancel)
        self.buttonLayout.addStretch()

    def logingroup(self):
        '''
        登入登入信息
        '''
        self.lename = QLineEdit()
        self.lename.setPlaceholderText("请输入用户名")
        lenamecompleter = QCompleter(
            ["", "admin", "user", "gaoxing", 'aoming', 'root'])
        self.lename.setCompleter(lenamecompleter)
        self.cbName = QComboBox()
        self.cbName.addItems(
            ["", "admin", "user", "gaoxing", 'aoming', 'root'])
        self.cbName.setFixedWidth(200)
        self.cbName.setLineEdit(self.lename)

        self.lePassword = QLineEdit()
        self.lePassword.setFixedWidth(200)
        self.lePassword.setEchoMode(QLineEdit.Password)
        self.lePassword.setPlaceholderText("密码不能为空")

        self.nameLayout = QFormLayout()
        self.nameLayout.addRow(QLabel("用户名:"), self.cbName)
        self.nameLayout.addRow(QLabel("密  码:"), self.lePassword)
        self.nameLayout.setFormAlignment(Qt.AlignCenter)

    def layout(self):
        '''
        整体布局
        '''
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addLayout(self.nameLayout)
        layout.addStretch()
        layout.addLayout(self.buttonLayout)
        layout.addStretch()
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    from gongyixitong.widgets.mainUI import *
    login = UI_login()
    if login.exec_():
        w = MainUI(parent=None)
        w.show()
        sys.exit(app.exec_())
