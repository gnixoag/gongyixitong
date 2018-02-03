from widgets.login import *
from widgets.mainUI import *
import sys
sys.path.append(".")
sys.path.append("..")





if __name__ == '__main__':
    app=QApplication(sys.argv)
    pyqt = os.path.dirname(PyQt5.__file__)
    QApplication.addLibraryPath(os.path.join(pyqt, "plugins"))
    login=UI_login()
    if login.exec_():
        w=mainUI()
        w.show()
        sys.exit(app.exec_())