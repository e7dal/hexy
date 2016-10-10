import arrow
from util import deb,nrange
from cell import F,e,Cursor
from grid import grid, show, spoint

CURSOR_POS=None


def gcp(): #get cursor position
 global CURSOR_POS
 deb('gcp',CURSOR_POS)
 return CURSOR_POS

def scp(x,y): 
 deb('scp',gcp(),x,y)
 cxc=0 #todo, normalize in cursor...
 #if y%2:
 # cxc=1-x%2
 #cx=int(x/2)-cxc
 global CURSOR_POS
 CURSOR_POS=(x,y)
 assert (x,y)==gcp()

#todo cpget and cpset
cpget=gcp
cpset=scp

def cursor(HG,x=3,y=5):
 deb('make an a cursor in the empty space around point in cell x,y',x,y)
 #x,y=x-1,y-1
 HG=_clearcursor(HG)
 i=x
 j=y
 scp(i,j)
 cx=Cursor('-')# todo > <
 cy=Cursor('|')# todo v ^

 HG=spoint(i-1,j,HG,cx)
 HG=spoint(i,j-1,HG,cy)
 HG=spoint(i+1,j,HG,cx)
 HG=spoint(i,j+1,HG,cy)
 return HG


#todo _cursorclear
#todo _cursor_clear
def _clearcursor(HG):
 cp=gcp()
 deb('clear a cursor in the empty space around point in cell x,y',cp)
 if not cp:return HG
 i,j=cp
 HG=spoint(i-1,j,HG,e)
 HG=spoint(i,j-1,HG,e)
 HG=spoint(i+1,j,HG,e)
 HG=spoint(i,j+1,HG,e)
 return HG

if __name__=='__main__':
 HG=grid()
 #show(HG)
 for i in nrange(pow(2,7)):
  print(i,i)
  HG=cursor(HG,i,i)
  HG=spoint(i,i,HG,str(i%10))
  show(HG)
 #HG=_clearcursor(HG)
 #show(HG)
 #HG=_clearcursor(HG)
 #show(HG)
 #ZZHG=cursor(HG)
