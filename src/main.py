from widgets.login import *
from widgets.mainUI import *
from widgets.usermanageUI import UserManageUI
from PyQt5.QtWidgets import *





if __name__ == '__main__':
    app=QApplication(sys.argv)
    login=UI_login()
    if login.exec_():
        w=MainUI()
        w.show()
        sys.exit(app.exec_())