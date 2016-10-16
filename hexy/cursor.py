from .util.deb import deb
from .util.nrange import nrange
from .cell import F,e,Cursor
from .grid import spoint

CURSOR_POS=None

def gcp(): #get cursor position
 global CURSOR_POS
 deb('gcp',CURSOR_POS)
 return CURSOR_POS

def scp(x,y): 
 deb('scp',gcp(),x,y)
 cxc=0 #todo, normalize in cursor...
 global CURSOR_POS
 CURSOR_POS=(x,y)
 assert (x,y)==gcp()

#todo cpget and cpset
cpget=gcp
cpset=scp

def cursor(HG,x,y,f,X,Y):
 deb('make an a cursor in the empty space around point in cell x,y',x,y)
 #x,y=x-1,y-1
 assert len(f)==4
 HG=_clearcursor(HG)
 i=x
 j=y
 scp(i,j)
 cxl=Cursor(f[0])
 cyu=Cursor(f[1])
 cxr=Cursor(f[2])
 cyd=Cursor(f[3])

 HG=spoint(i-1,j,HG,cxl,X,Y)
 HG=spoint(i,j-1,HG,cyu,X,Y)
 HG=spoint(i+1,j,HG,cxr,X,Y)
 HG=spoint(i,j+1,HG,cyd,X,Y)
 return HG

def grid_cursor(HG,x,y,f,X,Y):
 return cursor(HG,x,y,f,X,Y)

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

