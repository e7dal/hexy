import arrow
from .util.deb import deb
from .util.nrange import nrange
GRIDCHAR='.'

class C(object):
 def __str__(self): return ''
 def set(self,s='.',x=0,y=0):deb('C',s)

class E(C):
 def __str__(self): return ' '
 def set(self,s='.',x=0,y=0):deb('E',s)

class Cursor(E):
 def __init__(self,s=' '):self._str=s
 def __str__(self): return self._str
 def set(self,s=' ',x=0,y=0):deb('E',s)

class F(C):
 def __init__(self,s=GRIDCHAR,x=0,y=0):
  self._hist=[]
  self._str=s
  self._pos=(x,y)
  self.set(s)
 def __str__(self): return self._str
 def set(self,s='.',x=None,y=None):
  deb('F',s)
  self._str=s
  if isinstance(x,int) and isinstance(y,int):
   self._pos=(x,y)
  self.add_history()
 def add_history(self):
  self._hist.append((self._pos,self._str,arrow.now()))

e=E()
c=Cursor()
