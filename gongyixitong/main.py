#把本模块路径加入目录
import sys,os
sys.path.append(os.path.dirname(sys.path[0]))

#正常代码
from PyQt5.QtWidgets import *

from gongyixitong.widgets.login import *
from gongyixitong.widgets.mainUI import *
from gongyixitong.widgets.usermanageUI import UserManageUI

if __name__ == '__main__':

    app = QApplication(sys.argv)
    login = UI_login()
    if login.exec_():
        w = MainUI()
        w.show()
        sys.exit(app.exec_())
