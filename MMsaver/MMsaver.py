#coding=utf-8
import os,sys
import sqlite3
import hashlib
import shutil
import BeautifulSoup
import time
import re

class MMsaver:


    def __init__(self):
        if sys.platform.startswith('win32'):
            self.platform='w'
            self.coding='gbk'
            self.separater='\\'
        elif sys.platform.startswith('linux'):
            self.platform='l'
            self.coding='utf-8'
            self.separater='/'
        else:
            self.platform='unknown'
            self.coding='utf-8a'
            self.separater='/'
        if not self.find_root_dir():print "cannot find the dir"
        self.init_dbworker()
        self.basely_analyze_db()
        self.init_output_dir()

    def dothejob(self):
        os.mkdir(os.path.join(self.outputddir,'usr'))
        self.copy_usr_headshot(self.outputddir)
        
        for ec in self.chat_tables:
            self.output_chat(ec)


    def basely_analyze_db(self):
        self.get_chat_tables()
        self.get_md5s()

    def validateTitle(self,title):
        rstr = r"[ \/\\\:\*\?\"\<\>\|]"  # '/\:*?"<>|'
        new_title = re.sub(rstr, "", title)
        return new_title
    
    def output_chat(self,usrmd5):
        dirname = usrmd5[0:7]+'_'+self.validateTitle(self.md5_dict[usrmd5][0])
        usrdir = os.path.join(self.outputddir,dirname)#.encode(self.coding,'ignore'))
        os.mkdir(usrdir)
        os.mkdir(os.path.join(usrdir,'audio'))
        os.mkdir(os.path.join(usrdir,'img'))
        
        
        self.copy_all_files(usrmd5,usrdir)
        

        t_cs = self.dbworker.cursor()
        t_cs.execute('select * from Chat_%s'%usrmd5)
        t_msg_list = t_cs.fetchall()
        u_xhtml_file = open(os.path.join(usrdir,'Message.html'),'w')
        u_xhtml_file.write("<html><head></head><body>")
        yourname = ''
        for _msg in t_msg_list:
            try:
                item_string = self.get_item_string(_msg,self.md5_dict[usrmd5][0],self.md5_dict[usrmd5][1].endswith('@chatroom'))
                u_xhtml_file.write(item_string.encode('gbk','ignore'))
            except e:
                print item_string
        u_xhtml_file.write("</body></html>")

    def copy_usr_headshot(self,usrdir):
        for _epic in os.listdir(os.path.join(self.rootdir,'Usr')):
            shutil.copy(os.path.join(self.rootdir,'Usr',_epic),os.path.join(usrdir,'usr',_epic[:-7]+'jpg'))
    
    def copy_all_files(self,usrmd5,usrdir):
        u_aud_list,u_pic_list = self.get_data_list(usrmd5)
        for _epic in u_pic_list:
            shutil.copy(os.path.join(self.rootdir,'Img',usrmd5,_epic),os.path.join(usrdir,'img',_epic[:-3]+'jpg'))
        for _eaud in u_aud_list:
            t_source_file = open(os.path.join(self.rootdir,'Audio',usrmd5,_eaud),'rb')
            t_raw = t_source_file.read()
            t_source_file.close()
            t_target_file = open(os.path.join(usrdir,'audio',_eaud[:-3]+'amr'),'wb')
            t_target_file.write("#!AMR\n"+t_raw)
            t_target_file.close()

    def get_item_string(self,msg,your_name='',is_in_group=False):
            result = u''
            result += '<ul class="item" id=%d>'%msg[1]
            t_time = time.localtime(int(msg[3]))
            result += '<li class="time">%s</li>'%time.asctime(t_time)
            if msg[7]==10000:#10000号是腾讯的消息号啊！
                try:
                    result += '<li class="body" id="system_msg">%s</li>'%msg[4]#.encode(self.coding,'ignore')
                except:
                    print msg[4]
            else:
                msg_body=msg[4]
                if msg[8]==0:#自己发的
                    result += '<li class="who" id="self">wo:</li>'
                else:
                    #写名字
                    if is_in_group:#群里
                        t_name_index = msg_body.find(':\n')
                        if t_name_index:
                            result += '<li class="who" id="others"><img src="..%susr%s%s.jpg:/>'%(self.separater,
                                    self.separater,self.nametomd5[msg_body[:t_name_index]])
                            result += '%s:</li>'%msg_body[:t_name_index]
                            msg_body = msg_body[t_name_index:]
                    else:
                        result += '<li class="who" id="you">%s:</li>'%your_name

                if msg[7]==49:#49是app
                    result += '<li class="body" id="app">%s</li>'%"app"
                elif msg[7]==47:#47是表情。emoji的那个。
                    result += '<li class="body" id="emoji">%s</li>'%"emoji"
                elif msg[7]==34:#voice
                    result += '<li class="body" id="voice"><a href="audio%s%d.amr" target=_blank>voice</a></li>'%(self.separater,msg[1])
                elif msg[7]==3:
                    result += '<li class="body" id="pic"><img src="img\\%d.jpg"/></li>'%msg[1]
                elif msg[7]==1:
                    result += '<li class="body" id="text">%s</li>'%msg_body
                else:
                    result += '<li class="error">error:%d can not parse</li>'%msg[7]
            result += '</ul>'
            return result

    def get_data_list(self,usrmd5):
        res_aud_list = []
        res_pic_list = []
        if os.path.exists(os.path.join(self.rootdir,'Audio',usrmd5)):
            for _ef in os.listdir(os.path.join(self.rootdir,'Audio',usrmd5)):
                if _ef.endswith('.aud'):
                    res_aud_list.append(_ef)
            res_aud_list.sort(self.filename_compare)

        if os.path.exists(os.path.join(self.rootdir,'Img',usrmd5)):
            for _ef in os.listdir(os.path.join(self.rootdir,'Img',usrmd5)):
                if _ef.endswith('.pic'):
                    res_pic_list.append(_ef)
            res_pic_list.sort(self.filename_compare)
        
        
        
        result = (res_aud_list,res_pic_list)
        return result

    def filename_compare(self,fna,fnb):
        return int(os.path.splitext(fna)[0]) - int(os.path.splitext(fnb)[0])

    def get_chat_tables(self):
        cursor = self.dbworker.cursor()
        cursor.execute('select name from sqlite_master where type="table"')
        self.tables = cursor.fetchall()
        self.chat_tables=[]
        for _et in self.tables:
            if _et[0].startswith("Chat_"):
                self.chat_tables.append(_et[0][5:])

    def get_md5s(self):
        self.md5_dict={}
        self.nametomd5={}
        cursor = self.dbworker.cursor()
        result = cursor.execute('select UsrName,NickName from Friend')
        self.save_data_to_md5(result)
        cursor = self.dbworker.cursor()
        result = cursor.execute('select UsrName,NickName from QQContact')
        self.save_data_to_md5(result)
        
    def save_data_to_md5(self,result):
        for _eun in result:
            md5_maker = hashlib.md5()
            md5_maker.update(_eun[0])
            t_md5 = md5_maker.hexdigest()
            self.md5_dict[t_md5]=(_eun[1],_eun[0])
            self.nametomd5[_eun[0]]=t_md5

    def cleanup_for_exit(self):
        self.dbworker.commit()
        self.dbworker.close()

    def init_output_dir(self):
        self.outputddir = os.path.join(os.path.curdir,'output')
        if os.path.exists(self.outputddir):
            shutil.rmtree(self.outputddir)
        os.mkdir(self.outputddir)


    def init_dbworker(self):
        self.dbworker = sqlite3.connect(os.path.join(self.rootdir,'DB','MM.sqlite'))


    def find_root_dir(self,path=''):
        l_searching_path = os.path.abspath(path)
        if self._is_root_dir(l_searching_path):
            return

        l_find_parent_dir_times = 5
        while l_find_parent_dir_times>0:
            t_files_dirs = os.listdir(l_searching_path)
            if "Documents" in t_files_dirs:
                l_searching_path = os.path.join(l_searching_path,\
                    "Documents")
                break
            if "com.tencent.xin" in t_files_dirs:
                l_searching_path = os.path.join(l_searching_path,\
                    "com.tencent.xin","Documents")
                break
            if "Application" in t_files_dirs:
                l_searching_path = os.path.join(l_searching_path,\
                    "Application","com.tencent.xin","Documents")
                break
            l_find_parent_dir_times -=1
            l_searching_path = os.path.split(l_searching_path)[0]

        for _edf in os.listdir(l_searching_path):
            if os.path.isdir(os.path.join(l_searching_path,_edf)):
                if self._is_root_dir(os.path.join(l_searching_path,_edf)):
                    return True
        return False

    def _is_root_dir(self,path):
        if path == None: return False
        t_files_dirs = os.listdir(path)
        if 'DB' in t_files_dirs and \
            'Audio' in t_files_dirs and \
            'Img' in t_files_dirs:
            self.rootdir = path
            return True
        return False


if __name__=='__main__':

    def compare_md5(a,b):
        cp = int(a[0],16) - int(b[0],16)
        if cp>0:
            return 1
        elif cp==0:
            return 0
        else:
            return -1

    a = MMsaver()
    f = open('md5.txt','w')

    md5l = []
    for e in a.md5_dict:
        md5l.append((e,a.md5_dict[e][0].encode('utf-8','ignore')))
    md5l.sort(compare_md5)
    for e in md5l:
        f.write(e[0]+' '+e[1])
        f.write('\n')
    f.close()

    index=0
    f = open('chats.txt','w')
    for e in a.chat_tables:
        #if e.startswith('f1'):print index
        index+=1
        f.write(e)
        f.write('\n')
    f.close()
    a.dothejob()
