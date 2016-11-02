from .util.deb import deb
from .util.nrange import nrange
from .cell import Cell
#F,e,Cursor
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
 cxl=Cell(f[0],0,0)
 cyu=Cell(f[1],0,0)
 cxr=Cell(f[2],0,0)
 cyd=Cell(f[3],0,0,)

 HG=spoint(i-1,j,HG,cxl)
 HG=spoint(i,j-1,HG,cyu)
 HG=spoint(i+1,j,HG,cxr)
 HG=spoint(i,j+1,HG,cyd)
 return HG

def grid_cursor(HG,x,y,f,X,Y):
 return cursor(HG,x,y,f,X,Y)

def _clearcursor(HG):
 cp=gcp()
 r1=r2=r3=r4=Cell('r',0,0)
 deb('clear a cursor in the empty space around point in cell x,y',cp)
 if not cp:return HG
 i,j=cp
 HG=spoint(i-1,j,HG,r1)
 HG=spoint(i,j-1,HG,r2)
 HG=spoint(i+1,j,HG,r3)
 HG=spoint(i,j+1,HG,r4)
 return HG

