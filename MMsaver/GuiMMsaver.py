# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os
#import shutil

isWin=lambda:sys.platform.startswith('win32')

class GuiMMsaver(QDialog):
    def __init__(self):
        super(GuiMMsaver,self).__init__()
        self.curDir=os.path.dirname(os.path.realpath(sys.argv[0]))

        self._init_self()


    
    class ignore():
        def write(self,obj):
            return
        
        
        
    def _init_connect(self):
        self.connect(self.resetbutton, SIGNAL("clicked()"),self.resetbutton_onclicked)
        
    def resetbutton_onclicked(self):
        self.title_label.setText(QString('gafgsd'))
    def select_directory_button_onclicked(self):
        self.schedules_path = QFileDialog.getExistingDirectory(self,
                                                               caption = QString(),
                                                               directory = QString(),
                                                               option = QFileDialog.ShowDirsOnly)

    def _set_windows(self):
        t_dt = QApplication.desktop().screenGeometry()
        t_left = (t_dt.width() - self.my_width) / 2
        t_top = (t_dt.height() - self.my_height) / 2
        self.setGeometry(QRect(t_left,t_top,self.my_width,self.my_height))
    def _set_button_geomatry_range(self,button):
        ts_buttom_min_height = 10
        ts_buttom_max_height = 60
        ts_buttom_min_width = 10
        ts_buttom_max_width = 60
        button.setMaximumSize(ts_buttom_max_width,ts_buttom_max_height)
        button.setMinimumSize(ts_buttom_min_width,ts_buttom_min_height)
    
    def _init_layout(self):

        
        if True:
            if True:
                if True:
                    self.title_label = QLabel()
                    self.title_label.setGeometry(0,0,self.my_width*4/5,self.my_height*4/5)
                    self.title_label.setText(QString('msg label'))
                msg_Layout = QVBoxLayout()
                msg_Layout.addWidget(self.title_label)
                    
                if True:
                    self.resetbutton = QPushButton()
                    self.resetbutton.setText(QString('reset'))
                    self._set_button_geomatry_range(self.resetbutton)
                    self.select_directory_button = QPushButton()
                    self.select_directory_button.setText(QString('select'))
                    self._set_button_geomatry_range(self.select_directory_button)
                button_Layout = QVBoxLayout()
                button_Layout.addWidget(self.select_directory_button)
                button_Layout.addWidget(self.resetbutton)
                
            first_line_Layout = QHBoxLayout()
            first_line_Layout.addLayout(msg_Layout)
            first_line_Layout.addLayout(button_Layout)

        mLayout = QVBoxLayout()
        mLayout.addLayout(first_line_Layout)
        self.setLayout(mLayout)

    def _close(self):
        self.close()
    def _init_self(self):
        self.my_width = QApplication.desktop().screenGeometry().width()/2
        self.my_height = QApplication.desktop().screenGeometry().height()/2
        self._init_layout()
        self.setWindowTitle('微信导入程序'.decode('utf-8','ignore'))
        self._init_connect()
        self._set_windows()


app = QApplication(sys.argv)
l_ui = GuiMMsaver()
l_ui.show()

sys.exit(app.exec_())
