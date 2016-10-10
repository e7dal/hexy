import arrow
from pprint import pprint as pp
from operator import xor
from util import deb,nrange
from cell import F,e
from grid import grid, show, fill


def spoint(x,y,HG,c):
 spl=[(x,y)]
 HG=fill(HG,spl,c)
 show(HG)
 return HG

#L='ABCDEFGHIJKLMNOPRSTUVWXYZ'

def makex(HG,x=3,y=3,l=5):
 print('make an X line')
 j=y
 for i in nrange(x,x+l):
  deb(i,j)
  ii=j%2  #todo this bothers me, make something for this
  ii+=i*2
  HG=spoint(ii,j,HG,'X')
 return HG

def makey(HG,x=3,y=3,l=5):
 print('make an Y line')
 S=None
 for i in nrange(x,x+l):
  deb(i)
  if not S:
   ii=i%2
   ii+=i*2
   S=ii;
  else:
   S+=1
  j=i-1
  HG=spoint(S+1,j,HG,'Y')
 return HG

def makez(HG,x=3,y=3,l=5):
 print('make an Y line')
 S=None
 for i in nrange(x,x+l):
  deb(i)
  if not S:
   ii=i%2
   ii+=i*2
   S=ii;
  else:
   S-=1
  j=i-1
  HG=spoint(S+1,j,HG,'Z')
 return HG

if __name__=='__main__':
 HG=grid()
 HG=makex(HG)
 HG=makey(HG)
 HG=makez(HG)
