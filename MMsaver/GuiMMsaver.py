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
        self.mmsaver = MMsaver.MMsaver(True)
        self.usrlist_widget = None
    
    class ignore():
        def write(self,obj):
            return
        
        
    def _init_connect(self):
        self.connect(self.resetbutton, SIGNAL("clicked()"),self.resetbutton_onclicked)
        self.connect(self.select_directory_button,SIGNAL("clicked()"),self.select_directory_button_onclicked)
        self.connect(self.export_button,SIGNAL("clicked()"),self.export_button_onclicked)
        self.connect(self.close_button,SIGNAL("clicked()"),self.close_button_onclicked)
        
    def init_directory(self):
        if not os.path.exists(self.directory_path):
            self.msg_text_browser.setText(self.directory_path+" does not exist!")
            return
    def _add_list_widget(self):
        self.msg_text_browser.hide()
        if self.usrlist_widget:
            self.usrlist_widget.hide()
            self.msg_layout.removeWidget(self.usrlist_widget)

            
        self.usrlist_widget = QListWidget()
        for _usr in self.mmsaver.chat_tables:
            t_icon = QIcon(os.path.join(self.mmsaver.outputddir,'usr',_usr+'.jpg'))
            t_item = QListWidgetItem(t_icon,self.mmsaver.md5_dict[_usr][0])
            t_item._usr = _usr
            self.usrlist_widget.addItem(t_item)
        self.usrlist_widget.setViewMode(QListWidget.IconMode)
        self.usrlist_widget.setSelectionMode(QListWidget.ContiguousSelection)
        self.msg_layout.addWidget(self.usrlist_widget)
        
    def resetbutton_onclicked(self,temp="reset"):
        self.msg_text_browser.show()
        if self.usrlist_widget:
            self.usrlist_widget.hide()
            self.msg_layout.removeWidget(self.usrlist_widget)
        self.bottom_msg_label.setText('')
        self.progress_bar.reset()
        
        
    def select_directory_button_onclicked(self):
        self.directory_path = QFileDialog.getExistingDirectory(self,
                                                               caption = QString(),
                                                               directory = QString(),
                                                               options = QFileDialog.ShowDirsOnly)
        if not self.mmsaver.find_root_dir():
            self.bottom_msg_label.setText('This directory is not I desired')
            return
        
        self.mmsaver.init_dbworker()
        self.mmsaver.basely_analyze_db()
        self.mmsaver.init_output_dir()
        self.mmsaver.copy_usr_headshot()
        self._add_list_widget()
    
    def export_button_onclicked(self):
        if not self.usrlist_widget:
            return
        t_list = self.usrlist_widget.selectedItems()
        if not len(t_list):
            return
        self.progress_bar.setRange(0,len(t_list)+1)
        self.progress_bar.setValue(0)
        for _i in t_list:
            self.bottom_msg_label.setText('dealing with '+_i._usr)
            self.mmsaver.output_chat(_i._usr)
            self.progress_bar.setValue(self.progress_bar.value()+1)
        self.bottom_msg_label.setText('succeed!')
        self.progress_bar.setValue(self.progress_bar.value()+1)
        os.startfile(self.mmsaver.outputddir)
        

    def close_button_onclicked(self):
        self.close()
        
    def _set_windows(self):
        t_dt = QApplication.desktop().screenGeometry()
        t_left = (t_dt.width() - self.my_width) / 2
        t_top = (t_dt.height() - self.my_height) / 2
        self.setGeometry(QRect(t_left,t_top,self.my_width,self.my_height))
    def _set_button_geomatry_range(self,button):
        ts_buttom_min_height = 40
        ts_buttom_max_height = 80
        ts_buttom_min_width = 40
        ts_buttom_max_width = 80
        button.setMaximumSize(ts_buttom_max_width,ts_buttom_max_height)
        button.setMinimumSize(ts_buttom_min_width,ts_buttom_min_height)
    
    def _init_layout(self):

        
        if True:
            if True:
                if True:
                    self.msg_text_browser = QTextBrowser()
                    self.msg_text_browser.setText(QString('Welcome to Sunmile'))
                self.msg_layout = QVBoxLayout()
                self.msg_layout.addWidget(self.msg_text_browser)
                if True:
                    self.resetbutton = QPushButton()
                    self.resetbutton.setText(QString('reset'))
                    self._set_button_geomatry_range(self.resetbutton)
                    self.select_directory_button = QPushButton()
                    self.select_directory_button.setText(QString('select'))
                    self._set_button_geomatry_range(self.select_directory_button)
                    self.export_button = QPushButton()
                    self.export_button.setText('export')
                    self._set_button_geomatry_range(self.export_button)
                    self.close_button = QPushButton()
                    self.close_button.setText('exit')
                    self._set_button_geomatry_range(self.close_button)
                button_Layout = QVBoxLayout()
                button_Layout.addWidget(self.select_directory_button)
                button_Layout.addWidget(self.resetbutton)
                button_Layout.addWidget(self.export_button)
                button_Layout.addWidget(self.close_button)
                
            first_line_Layout = QHBoxLayout()
            first_line_Layout.addLayout(self.msg_layout)
            first_line_Layout.addLayout(button_Layout)
            
            if True:
                self.progress_bar = QProgressBar()
            second_line_Layout = QHBoxLayout()
            second_line_Layout.addWidget(self.progress_bar)
            
            if True:
                self.bottom_msg_label = QLabel()
            bottom_line_Layout = QHBoxLayout()
            bottom_line_Layout.addWidget(self.bottom_msg_label)
            
        mLayout = QVBoxLayout()
        mLayout.addLayout(first_line_Layout)
        mLayout.addLayout(second_line_Layout)
        mLayout.addLayout(bottom_line_Layout)
        self.setLayout(mLayout)

    def _close(self):
        self.close()
    def _init_self(self):
        self.my_width = QApplication.desktop().screenGeometry().width()*2/3
        self.my_height = QApplication.desktop().screenGeometry().height()/2
        self._init_layout()
        self.setWindowTitle('微信导入程序'.decode('utf-8','ignore'))
        self._init_connect()
        self._set_windows()


app = QApplication(sys.argv)
l_ui = GuiMMsaver()
l_ui.show()

sys.exit(app.exec_())
