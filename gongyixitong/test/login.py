#!/usr/bin/env python
'''
#用户登陆界面

@author: gaoxing
'''

import sys
import os
from PyQt5.QtWidgets import (QDialog, QApplication, QBoxLayout,
                             QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QComboBox,
                             QStyleFactory, QCompleter,
                             QFormLayout, QMessageBox)
from PyQt5.QtCore import Qt
import PyQt5
import os
import base64
from hashlib import sha512
from hmac import HMAC
from mainUI import mainUI


class UI_login(QDialog):
    '''
    #用户登入界面
    '''

    def __init__(self):
        super(UI_login, self).__init__()
        self.initUI()

    def initUI(self):
        '''
        #初始化界面
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

        if self.validate(username, "高星") and self.validate(password, "12345"):
            #QMessageBox.information(None, "登陆提示", "用户名："+username+"\n密码："+password+"\n登陆成功", QMessageBox.Ok, QMessageBox.Cancel)
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

    def encrypt(self, password, salt=None):
        """Hash password on the fly."""
        if salt is None:
            salt = os.urandom(8)

        # 如果指定 salt， 进行 salt 检查
        assert 8 == len(salt)
        assert isinstance(salt, bytes)
        assert isinstance(password, str)

        if isinstance(password, str):
            password = password.encode('UTF-8')

        assert isinstance(password, bytes)

        result = password

        # 使用 sha512 进行20次随机加密
        for i in range(20):
            result = HMAC(result, salt, sha512).digest()

        # 返回utf-8加密字符（把salt加入用于验证加密）
        return str(base64.b64encode(salt + result), encoding="utf-8")

    def validate(self, hashed, input_password):
        salt = base64.b64decode(bytes(hashed, encoding="utf8"))
        return hashed == self.encrypt(input_password, salt[:8])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pyqt = os.path.dirname(PyQt5.__file__)
    QApplication.addLibraryPath(os.path.join(pyqt, "plugins"))
    login = UI_login()
    if login.exec_():
        w = mainUI()
        w.show()
        sys.exit(app.exec_())
