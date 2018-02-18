from gongyixitong.widgets.login import *
from gongyixitong.widgets.mainUI import *
from gongyixitong.widgets.usermanageUI import UserManageUI
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    login = UI_login()
    if login.exec_():
        w = MainUI()
        w.show()
        sys.exit(app.exec_())
