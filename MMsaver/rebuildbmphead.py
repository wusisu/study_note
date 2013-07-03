import struct

'''
@note:this class is to change advanced bmp header to normal 40 bytes header
so that PIL can read it.
'''
class Rebuild_BMP_Head():
    @staticmethod
    def convert(oldname,newname):
        t_file = open(oldname,'rb')
        raw = t_file.read()
        t_file.close()
        if not raw[0:2]=='BM': #not a BMP file
            return False

        pic_start_addr = struct.unpack('i',raw[10:14])[0]
        pic_data = raw[pic_start_addr:]
        pic_data_len = len(pic_data)


        t_file = open(newname,'wb')
        t_file.write('BM')
        t_file.write(struct.pack('i',54+pic_data_len))
        t_file.write(struct.pack('i',0))
        t_file.write(struct.pack('i',54))
        t_file.write(struct.pack('i',40))
        t_file.write(raw[18:38])
        t_file.write(struct.pack('4i',0,0,0,0))

        t_file.write(pic_data)

        t_file.close()
        return True

