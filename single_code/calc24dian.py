import sys,copy


class Calc_twentyfour():
    def __init__(self,*args,**kwargs):
        self.reorder=False
        self.data=[]
        self.num=[]
        self.ans=24
        self.filename=''
        if kwargs.has_key('filename'):
            self.filename=kwargs['filename']
        if kwargs.has_key('reorder'):
            self.reorder=kwargs['reorder']

        if kwargs.has_key('num'):
            self.ans=kwargs[num].pop(4)
            self.num.append(num)
        else:
            num=[]
            if len(args)>4:
                self.ans=int(args[4])
            elif len(args)<4:
                print "args wrong!"
                raise RuntimeError
            for i in range(4):
                num.append(int(args[i]))
        fnum=[]
        for n in num:
            fnum.append(1.0*n)

        self.num.append((num,fnum))
        self.fans=self.ans*1.0
            
    def _determineOp(self,o):
        return [o/16, (o%16)/4,o%4]
    def _getSumbyOp(self,o,a,b):
        if o==0:
            return (a+b,'+')
        elif o==1:
            return (a-b,'-')
        elif o==2:
            return (a*b,'*')
        else:
            if b==0:return (9999999,'/')
            return (a/b,'/')
    def _calcASum(self,o,a,b):
            return self._getSumbyOp(o,a,b)
            
    def _calcManger(self,al,nl,fnl):
        if len(fnl)==1:
            self.data.append((fnl[0]==self.fans,nl[0]))
        for i in range(len(nl)-1):
            lnl=copy.copy(nl)
            lfnl=copy.copy(fnl)
            lal=copy.copy(al)
            fa=lfnl.pop(i)
            fb=lfnl.pop(i)
            a=lnl.pop(i)
            b=lnl.pop(i)
            o=lal.pop(i)
            s,c = self._calcASum(o,fa,fb)
            lfnl.insert(i,s)
            lnl.insert(i,'('+str(a)+c+str(b)+')')
            self._calcManger(lal,lnl,lfnl)

    def _writeAns(self):
        count=0
        if self.filename=='':
            #for e in self.data:
            for e in set(self.data):
                if e[0]:
                    count+=1
                    print e[1]
            print "total %d methods"%count
    
    def _calcall(self):
        for nli in self.num:
            for i in range(64):
                self._calcManger(self._determineOp(i),nli[0],nli[1])

    def _reorderList(self):
        for i in range(23):
            nl=copy.copy(self.num[0][0])
            fl=copy.copy(self.num[0][1])
            lnl=[]
            lfl=[]
            for k in range(4):
                lnl.append(nl.pop((i+1)%(4-k)))
                lfl.append(fl.pop((i+1)%(4-k)))
            self.num.append((lnl,lfl))
    def doIt(self):
        if self.reorder:
            self._reorderList()
        self._calcall()
        self._writeAns()













if __name__=='__main__':
    b=24
    while b:
        a1=int(raw_input("input a element:"))
        a2=int(raw_input("input a element:"))
        a3=int(raw_input("input a element:"))
        a4=int(raw_input("input a element:"))
        b=int(raw_input("input the target:(imput 0 to exit)"))
        c = Calc_twentyfour(a1,a2,a3,a4,b,reorder=True)
        c.doIt()    

    num=[]
    if len(sys.argv)>4 and False:
        if len(sys.argv)>5:
            ans=int(sys.argv[5])
        else:
            ans=24
        for i in range(4):
            num.append(sys.argv[i+1])
        num.append(ans)
        c = Calc_twentyfour(num=num)
        c.doIt()
    else:
        print "over"
