import time
from .util.deb import deb
from .util.nrange import nrange
GRIDCHAR='.'

class Cell(object):
 def __init__(self,s=GRIDCHAR,x=0,y=0):
  self._hist=[]
  self._str=s
  self._pos=(x,y)
  self.set(s)
 def __repr__(self):
  return "<hexy.cell.F '%s' pos:(%d,%d) #hist:%d >"%(self._str,self._pos[0],self._pos[1],len(self._hist))
 def get(self):
  return self._str
 def getpos(self):
  return self._pos
 def set(self,s='.',x=None,y=None):
  deb('F',s)
  self._str=s
  if isinstance(x,int) and isinstance(y,int):
   self._pos=(x,y)
  self.add_history()
 def add_history(self):
  self._hist.append((self._pos,self._str,time.clock()))


#TODO remove old stuff
#F=Cell
#e=Cell('.',-1,-1)
#Cursor=Cell
