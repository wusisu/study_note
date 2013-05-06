#coding=utf-8
import os,sys
import sqlite3
import hashlib


class MMsaver:

	def __init__(self):
		self.find_root_dir()
		self.init_dbworker()
		self.analyze_db()

	def dothejob(self):
		for ec in self.chat_tables:
			self.output_chat(ec)
		
		
	def analyze_db(self):
		self.get_chat_tables()
		self.get_md5s()

			
	def output_chat(self,usrmd5):
		dirname = usrname[0:7]+self.md5_dict[usrmd5].encode('gbk','ignore')
		usrdir = os.path.join(self.outputddir,dirname)
		os.mkdir(usrdir)
		
	
	def get_chat_tables(self):
		cursor = self.dbworker.cursor()
		cursor.execute('select name from sqlite_master where type="table"')
		self.tables = cursor.fetchall()
		self.chat_tables=[]
		for _et in self.tables:
			if _et[0].startswith("Chat_"):
				self.chat_tables.append(_et[0][5:])

	def get_md5s(self):
		cursor = self.dbworker.cursor()
		result = cursor.execute('select UsrName,NickName from Friend')
		md5_maker = hashlib.md5()
		self.md5_dict={}
		for _eun in result:
			md5_maker.update(_eun[0])
			self.md5_dict[md5_maker.hexdigest()]=_eun[1]
	
	def cleanup_for_exit(self):
		pass
	
	def init_output_dir(self):
		self.outputddir = os.path.join(os.path.curdir(),'output')
		if not os.path.exists(self.outputddir):
			os.mkdir(self.outputddir)
		elif not os.path.isdir(self.outputddir):
			os.remove(self.outputddir)
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
	a = MMsaver()
	a.analyze_db()
	#print a.chat_tables
	f = open('md5.txt','w')
	for e in a.md5_dict:
		f.write(e)
		f.write(' ')
		f.write(a.md5_dict[e].encode('gbk','ignore'))
		f.write('\n')
	f.close()
	f = open('chats.txt','w')
	for e in a.chat_tables:
		f.write(e)
		f.write('\n')
	f.close()