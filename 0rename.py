import os
import md5
import datetime
'''
delete same files and rename;
'''
oldlist = os.listdir('')

def converitos(indw):
    s=str(indw)
    while (len(s)<4):
        s = '0'+s
    return s

def calc_md5(string):
    return md5.new(string).hexdigest()

i=0
md5_dict = {}
ts = calc_md5(str(datetime.datetime.now()))[:6] + '_'

for fn in oldlist:
    if fn.lower().endswith('.jpg'):
        t_md5 = calc_md5(open(fn,'rb').read())
        if not md5_dict.has_key(t_md5):
            md5_dict[t_md5] = []
        md5_dict[t_md5].append(fn)


for md in md5_dict:
    i = 0
    for fn in md5_dict[md]:

        os.rename(fn,ts + md +str(i)+'.jpg')
        i+=1
