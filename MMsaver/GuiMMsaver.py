# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os
import MMsaver
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
        self.connect(self.select_directory_button,SIGNAL("clicked()"),self.select_directory_button_onclicked)
        
    def init_directory(self):
        if not os.path.exists(self.directory_path):
            self.msg_text_browser.setText(self.directory_path+" does not exist!")
            return
        
    def resetbutton_onclicked(self,temp="reset"):
        if self.msg_object_layout:
            self.msg_layout.removeItem(self.msg_object_layout)
            for i in self.msg_object_layout.findChildren(QPushButton):
                i.hide()
                i.deleteLater()
            self.msg_object_layout.deleteLater()
            self.msg_object_layout = None
        self.msg_text_browser.hide()
        self.msg_object_layout = QGridLayout()
        for i in temp:
            t_label = QPushButton()
            t_label.setText(i)
            self.msg_object_layout.addWidget(t_label)
        self.msg_layout.addLayout(self.msg_object_layout)
            
            
    def select_directory_button_onclicked(self):
        self.directory_path = QFileDialog.getExistingDirectory(self,
                                                               caption = QString(),
                                                               directory = QString(),
                                                               options = QFileDialog.ShowDirsOnly)
        #self.resetbutton.hide()
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
                    self.msg_text_browser = QTextBrowser()
                    self.msg_text_browser.setText(QString('msg label'))
                    self.msg_text_browser_layout = QVBoxLayout()
                    self.msg_text_browser_layout.addWidget(self.msg_text_browser)
                self.msg_layout = QVBoxLayout()
                self.msg_layout.addLayout(self.msg_text_browser_layout)
                self.msg_object_layout = None
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
            first_line_Layout.addLayout(self.msg_layout)
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
