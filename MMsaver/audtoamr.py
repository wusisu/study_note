#coding=utf-8
import os
f = open('3415.aud','rb')
ff=f.read()
f.close()
#os.remove('3415.aud')
f = open('3415.amr','wb')
f.write("#!AMR\n"+ff)
f.close()
