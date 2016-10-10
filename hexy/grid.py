import arrow
#from pprint import pprint as pp
from operator import xor

from .util.deb import deb
from .util.nrange import nrange
from .cell import F,e

#X = 42
#X = 18 #3:
#Y = 12 #2:
X = Y = None 

b=':'
GRIDCHAR='.'

def grid(HG=[],xsize=7,ysize=5):
 global X,Y
 X=int(xsize)
 Y=int(ysize)

 for y in nrange(Y):
  HG.append([])
  for x in nrange(X*2):
   if xor(x%2,y%2):
    HG[y-1].append(e)
   else:
    HG[y-1].append(F(x=x,y=y))
 return HG

def grid_make(x,y):
 return grid([],x,y)

def show(HG):
 i=1
 xr=xruler()
 print(b+"|"+xr+"|"+b)
 print(b+"|"+'_'*(len(xr))+"|"+b)
 for l in HG:
  s=''
  for c in l:  
   s+=str(c)
  print(b+"|"+ s + "|"+b+str(i))
  i+=1
 print(b+"|"+'_'*(len(xr))+"|"+b)
 if Y%2==0 and X > 0:
  print(b+"|"+str(e)+xr[0:-1]+"|"+b)
 else:
  if X==0:
   #print(b+"|"+str(e)+xr[0:-1]+"|"+b)
   print(b+"||"+b)
  else:
   print(b+"|"+xr+"|:"+b)

def grid_show(g):show(g)

def xruler():
 x=[str(x) for x in nrange(9)]
 xs=' '.join(x)
 xs+=' 0 '
 xl=''
 xt=X
 while xt>0:
  if xt>10:
   xl+=xs
   xt-=10
  else:
   xl+=xs[0:xt*2]
   xt=0
 return xl

def fill(HG,l,c='X'):
 deb('fill',l,c)
 for x,y in l:
  if isinstance(c,str):
   HG[y][x].set(c,x=x,y=y)
  else:
   HG[y][x]=c
 return HG

def spoint(x,y,HG,c):
 deb('spoint',x,y,c)
 x,y=x-1,y-1
 xc,yc=int(y/Y),int(x/Y) #correction
 xc,yc=xc*Y,yc*X#correction
 x,y=x+xc,y+yc           #correction
 x,y=x%X,y%Y
 HG[y][x]=c
 return HG

def add_one_with_dir(x,y,g,d):
 c=''
 if d=='X':
  x+=2
  c='_'

 if d=='x':
  x-=2
  c='_'

 if d=='Y':
  x+=1
  y+=1
  c='\\'

 if d=='y':
  x-=1
  y-=1
  c='\\'

 if d=='Z':
  x-=1
  y+=1
  c='/'

 if d=='z':
  x+=1
  y-=1
  c='/'
 cell=F(c,x,y)
 #this will break the nice tri-symmetric grid
 #todo: make sure in future resetting to add the empty space back
 return spoint(x,y,g,cell),x,y

if __name__=='__main__':
 g=grid(xsize=12,ysize=8)
 show(g)
