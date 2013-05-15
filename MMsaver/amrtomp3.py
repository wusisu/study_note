#coding=utf-8
import os
'''
This is only a script that to use mplayer and lame
'''


class AmrtoMp3():
    @staticmethod
    def trans(file_addr,del_source=False,bit_rate=160):
        print len(file_addr)
        os.system("mplayer -ao pcm "+file_addr.encode('utf-8'))
        os.system("lame audiodump.wav -o " + file_addr[:-3].encode('utf-8')+'mp3' + " -b %d"%bit_rate)
        os.remove("audiodump.wav")
        if del_source:
            os.remove(file_addr)

if __name__=='__main__':
    AmrtoMp3.trans(u'./output/19f34ba_百度贴吧/audio/8.amr',False)
