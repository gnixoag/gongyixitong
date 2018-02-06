'''
Created on 2018年2月4日

@author: gaoxing
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class About(QDialog):
    '''
    关于
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(QDialog,self).__init__()
        self.setupUI()
        self.setWindowTitle('关于系统')
        self.resize(300,200)
        self.setWindowFlags(self.windowFlags() & 
                            ~Qt.WindowContextHelpButtonHint)
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        
    def setupUI(self):
        

        label = QLabel()
        label.setText(' 开发日期：2018年1月1日 \n \
版本信息：测试版 \n \
最后修改：2018.1.1 \n \
开发单位：高星' )
        qtable=QTabWidget()
        qtable.addTab(label, 'baid')
        layout=QVBoxLayout()
        layout.addWidget(qtable)
        self.setLayout(layout)
        
        
        
if __name__ == '__main__' :
    app=QApplication(sys.argv)
    w=About()
    w.exec_()
    sys.exit(app.exec_())