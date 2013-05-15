# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os
import shutil

isWin=lambda:sys.platform.startswith('win32')

class GuiMMsaver(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        self.curDir=os.path.dirname(os.path.realpath(sys.argv[0]))

        self._init_layout()
        #self.addTitleBar()
        #self.setTitle(QString('MMsaver'))
        self._init_connect()

    
    class ignore():
        def write(self,obj):
            return
        
        
        
    def _init_connect(self):
        self.connect(self.resetbutton, SIGNAL("clicked()"),self.resetbutton_onclicked)
        
    def resetbutton_onclicked(self):
        #self.title_label.setText('reset')
        pass

    
    def _init_layout(self):
        
        self.title_label = QLabel()
        self.title_label.setMaximumHeight(80)
        self.title_label.setText(QString('f'))
        self.resetbutton = QPushButton
        self.resetbutton.setText(QString('a'))
        mLayout = QVBoxLayout()
        mLayout.addWidget(self.title_label)
        mLayout.addWidget(self.resetbutton)
        self.setLayout(mLayout)

    def _close(self):
        self.close()
    def _init_self(self):
        pass


app = QApplication(sys.argv)
l_ui = GuiMMsaver()
l_ui.show()
sys.exit(app.exec_())
