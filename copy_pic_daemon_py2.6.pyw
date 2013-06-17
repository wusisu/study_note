import os
import sys
import time

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import hashlib
import sqlite3
import shutil


            
        
        
class Collect_pic(QWidget):
    
    def __init__(self):
        super(Collect_pic,self).__init__()

        qutiAction = QAction(self)
        qutiAction.setText('quit')
        self.connect(qutiAction, SIGNAL('triggered()'),self.close)
        steal_action=QAction(self)
        steal_action.setText('steal')
        self.connect(steal_action,SIGNAL('triggered()'),self.take_pic_timer)
        rob_action = QAction(self)
        rob_action.setText('rob')
        self.connect(rob_action,SIGNAL('triggered()'),self.on_rename_files)
        set_path_action = QAction(self)
        set_path_action.setText('path')
        self.connect(set_path_action,SIGNAL('triggered()'),self.on_set_path_clicked)
        
        trayIconMenu = QMenu(self)
        trayIconMenu.addAction(steal_action)
        trayIconMenu.addSeparator()
        trayIconMenu.addAction(rob_action)
        trayIconMenu.addAction(set_path_action)
        trayIconMenu.addAction(qutiAction)
        
        
        trayicon = QSystemTrayIcon(self)
        trayicon.setIcon(QIcon('ic_launcher.png'))
        trayicon.setToolTip('stealing pictures')
        trayicon.setContextMenu(trayIconMenu)
        trayicon.activated.connect(self.on_system_trayicon_clicked)
        trayicon.show()
        self.trayicon = trayicon

        self.init_settings()

        
    def init_settings(self):

        self.PICNAME = '360wallpaper.jpg'
        self.stealhome = 'stealpic'
        self.robhome = 'robpic'
        self.SLEEPTIME = 154
        
        if not os.path.exists(self.stealhome):
            os.mkdir(self.stealhome)
            
        self.timer = QTimer()
        self.connect(self.timer,SIGNAL('timeout()'),self.take_pic_timer)
        self.timer.start(self.SLEEPTIME*1000)
        
       

    def take_pic_timer(self):
        if not self.timer is None:
            self.timer.stop()
        self.timer = QTimer()
        self.take_pic_home()
        self.connect(self.timer,SIGNAL('timeout()'),self.take_pic_timer)
        self.timer.start(self.SLEEPTIME*1000)
        
        
    def take_pic_home(self, pichome='',picname=''):
        if picname=='':
            picname = self.PICNAME
        if pichome=='':
            pichome = self.stealhome
        if not os.path.exists(picname):
            return
        picfile = open(picname,'rb')
        picdata = picfile.read()
        picfile.close()
        picmd5 = hashlib.md5()
        picmd5.update(picdata)
        pichex = picmd5.hexdigest()
        piclen = os.stat(picname).st_size

        existed = "not exist"
        if os.path.exists(os.path.join(pichome,pichex+"_"+str(piclen)+".jpg")):
            existed = "exist"
        else:
            shutil.copy2(picname, os.path.join(pichome,pichex+"_"+str(piclen)+".jpg"))
        self.trayicon.showMessage('get pics','%d %s %s %s'%(piclen,pichex,picname,existed),QSystemTrayIcon.Information,1500)
        
    def on_system_trayicon_clicked(self,click_reason):
        if click_reason==QSystemTrayIcon.Trigger:
            self.take_pic_timer()
            return
        if click_reason==QSystemTrayIcon.DoubleClick:
            self.close()
            return
        
    def on_rename_files(self):
        t_rename_files = QFileDialog.getOpenFileNames(self,
                                                      'rob pics',
                                                      '',
                                                      'Images (*.jpg *.bmp *.png)')
        if not os.path.exists(self.robhome):
            os.mkdir(self.robhome)
        for _ef in t_rename_files:
            self.take_pic_home(self.robhome,_ef)
    
    def on_set_path_clicked(self):
        t_save_path = QFileDialog.getExistingDirectory(self,
                                                       'Set save path',
                                                       self.stealhome)
        self.robhome = unicode(t_save_path)
        self.stealhome = unicode(t_save_path)
        self.trayicon.showMessage('set path','set path to %s'%t_save_path,QSystemTrayIcon.Information,3000)
                                                       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName(u"stealing pictures")    
    daemonui = Collect_pic()  
    app.exec_()
