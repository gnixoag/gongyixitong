'''
Created on 2018年1月25日

@author: gaoxing
'''
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QAction,
                             QTableWidget, QHBoxLayout, QPushButton,
                             QToolBar, QStyleFactory, QDialog)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from gongyixitong.widgets.usermanageUI import *
from gongyixitong.widgets.about import *


class MainUI(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        self.resize(800, 600)
        self.setWindowTitle('工艺系统')

        menuber = self.menuBar()

        gongyiBOMmenu = menuber.addMenu("工艺BOM(&G)")
        newBOMaction = QAction("新建BOM(&X)", self)
        newBOMaction.setShortcut("Ctrl+n")
        # newBOMaction.triggered.connect(self.close(self))
        reviewBOMaction = QAction("审核BOM(&S)", self)
        putBOMaction = QAction("输出BOM(&P)", self)
        gongyishejiaction = QAction("工艺设计(&D)", self)
        queryBOMaction = QAction("查下BOM(&C)", self)

        gongyiBOMmenu.addAction(newBOMaction)
        gongyiBOMmenu.addAction(reviewBOMaction)
        gongyiBOMmenu.addAction(putBOMaction)
        gongyiBOMmenu.addAction(gongyishejiaction)
        gongyiBOMmenu.addAction(queryBOMaction)

        sysCFGmenu = menuber.addMenu("系统配置(&X)")
        modcfgaction = QAction("模块配置(&M)", self)
        usermanageaction = QAction("用户管理(&Y)", self)
        usergroupmanageaction = QAction("用户组管理(&Z)", self)

        sysCFGmenu.addAction(modcfgaction)
        sysCFGmenu.addAction(usermanageaction)
        sysCFGmenu.addAction(usergroupmanageaction)

        helpmenu = menuber.addMenu("帮助(&B)")
        aboutation = QAction("关于(A)", self)
        helpmenu.addAction(aboutation)
        aboutation.triggered.connect(self.aboutok)

        toolbar = self.addToolBar("工具栏")
        toolbar.addAction(usermanageaction)
        toolbar.addAction(usergroupmanageaction)
        toolbar.addAction(newBOMaction)

        usermanageaction.triggered.connect(self.usermanage)

        self.statusBar().showMessage('工艺系统')

        table = QTableWidget(20, 10)

    def aboutok(self):
        a = About()
        a.exec_()

    def usermanage(self):
        print('测试信息')
        d = UserManageUI(parent=self)
        d.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainUI()
    w.show()
    sys.exit(app.exec_())
