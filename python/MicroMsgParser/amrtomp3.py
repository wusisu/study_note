#coding=utf-8
import os
import sys
'''
This is only a script that to use mplayer and lame
'''


class AmrtoMp3():
    @staticmethod
    def trans(file_addr,del_source=False,transor="ffmpeg",bit_rate=160):
        if sys.platform.startswith("win32"):
            file_addr_coded = file_addr.encode('gbk')
        else:
            file_addr_coded = file_addr.encode('utf-8')
            
        AmrtoMp3.trans_ffmpeg(file_addr_coded)
        if del_source:
            os.remove(file_addr_coded)

    @staticmethod
    def trans_ffmpeg(file_addr):
        os.system("ffmpeg -i %s %s"%(file_addr,file_addr[:-3]+'mp3'))
        
    
    @staticmethod
    def trans_linux_meplayer_lame(file_addr,del_source=False,bit_rate=160):
        os.system("mplayer -ao pcm "+file_addr.encode('utf-8'))
        os.system("lame audiodump.wav -o " + file_addr[:-3].encode('utf-8')+'mp3' + " -b %d"%bit_rate)
        os.remove("audiodump.wav")

