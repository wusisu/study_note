import os
import sys
import time

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import hashlib
import sqlite3
import shutil


class steal_thread(QThread):
    def __init__(self):
        super (steal_thread,self).__init__()
        self.DB = 'pic_stat.db'
        
        self.TABLENAME = 'pic'
        self.PICNAME = '360wallpaper.jpg'
        self.SLEEPTIME = 154
        
        qDebug('st_init')
    def run(self):
        while True:
            print "attempt"
            self.take_pic_home()
            time.sleep(self.SLEEPTIME)
            
    def take_pic_home(self):
        qDebug('tphs')
        picfile = open(self.PICNAME,'rb')
        picdata = picfile.read()
        picfile.close()
        picmd5 = hashlib.md5()
        picmd5.update(picdata)
        pichex = picmd5.hexdigest()
        piclen = os.stat(self.PICNAME).st_size
        shutil.copy2(self.PICNAME, os.path.join('pichome',pichex+"_"+str(piclen)+".jpg"))
        
        
class Collect_pic(QWidget):
    
    def __init__(self):
        super(Collect_pic,self).__init__()
        qDebug('collect_pic')
        
        if not os.path.exists('pichome'):
            os.mkdir('pichome')

        qutiAction = QAction(self)
        qutiAction.setText('quit')
        self.connect(qutiAction, SIGNAL('triggered()'),self.close)
        
        trayIconMenu = QMenu(self)     
        trayIconMenu.addAction(qutiAction)
        
        trayicon = QSystemTrayIcon(self)
        trayicon.setIcon(QIcon('ic_launcher.png'))
        trayicon.setToolTip('stealing pictures')
        trayicon.setContextMenu(trayIconMenu)
        trayicon.show()
        self.st = steal_thread()
        self.st.start()
        qDebug('cp_init_finish')
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName(u"stealing pictures")    
    daemonui = Collect_pic()  
    app.exec_()
