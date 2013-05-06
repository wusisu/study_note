import os,sys

class MMsaver:

	def __init__(self):
		self.find_root_dir()


	def find_root_dir(self,path=''):
		l_searching_path = os.path.abspath(path)
		if self._is_root_dir(l_searching_path):
			return

		l_find_parent_dir_times = 3
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
	print a.find_root_dir()
	print a.rootdir
	