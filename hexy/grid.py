#from pprint import pprint as pp
from operator import xor
from itertools import cycle
from math import hypot

from .util.deb import debget,debset,deb
from .util.nrange import nrange
from .cell import Cell
#F,e

#todo put these in magic configuration/constants.
b=':'           # the border character
#GRIDCHAR='.'    # the grid points

def grid(HG=[],xsize=7,ysize=5):
 X=xsize
 Y=ysize
 for y in nrange(Y):
  HG.append([])
  for x in nrange(X*2):
   if xor(x%2,y%2):
    HG[y-1].append(Cell(' ',x=x,y=y))
   else:
    HG[y-1].append(Cell('.',x=x,y=y))
 return HG

def grid_make(x,y):
 return grid([],x,y)

def greset(HG=[],xsize=7,ysize=5):
 X=xsize
 Y=ysize
 for y in nrange(Y):
  for x in nrange(X*2):
   if xor(x%2,y%2):
    HG[y-1][x-1]=Cell('.',x,y)
 return HG

def grid_reset(HG,x,y):
 return greset(HG,x,x)

def show(HG,X,Y):
 i=1
 r=[]
 X=len(HG[0])
 xc=X%2
 X=int(X/2)#+2*xc
 Y=len(HG)

 xr=xruler(X,Y)

 r.append(b+"|"+xr+"|"+b)
 r.append(b+"|"+'_'*(len(xr))+"|"+b)
 for l in HG:
  s=''
  for c in l:
   #s+=str(c)
   s+=str(c.get())
  r.append(b+"|"+ s + "|"+b+str(i))
  i+=1
 r.append(b+"|"+'_'*(len(xr))+"|"+b)
 if Y%2==0 and X > 0:
  r.append(b+"| "+xr[0:-1]+"|"+b)
 else:
  if X==0:
   r.append(b+"||"+b)
  else:
   r.append(b+"|"+xr+"|:"+b)
 return r

def grid_show(g):
 deb(g)
 X=len(g[0])/2
 Y=len(g)
 r=show(g,X,Y)
 rs=''
 for l in r:
  rs+=l+"\n"
 return rs

def xruler(X,Y):
 x=[str(x) for x in nrange(9)]
 xs=' '.join(x)
 xs+=' 0 '
 xl=''
 xt=int(X)
 while xt>0:
  if xt>10:
   xl+=xs
   xt-=10
  else:
   #debset(True)
   deb(xl)
   deb(xs)
   deb(xt)
   deb(len(xs))
   #debset(False)
   xl+=xs[0:xt*2]
   #xl+=xs[0:xt]
   #xl+=xs
   xt=0
 return xl

def fill(HG,l,c=' '):
 deb('fill',l,c)
 for x,y in l:
  if isinstance(c,str):
   HG[y][x].set(c,x=x,y=y)
  else:
   HG[y][x]=c
 return HG

def spoint(x,y,HG,c,X,Y):
 deb('spoint',x,y,c)

 X=len(HG[0])
 Y=len(HG)

 XL=X-1
 YL=Y-1
 
 x,y=x-1,y-1
 x,y=x%(2*X),y%Y
 #shift up
 if x<0:x+=XL
 if y<0:y+=YL
 #shift down
 if x>XL:x-=XL
 if y>XL:y-=YL
 HG[y][x].set(c.get())
 return HG
 
 #if isinstance(HG[y][x],F):
 # if isinstance(c,F):
 #  HG[y][x].set(c.get())
 # else:
 #  HG[y][x].set(c) #fingers crossed, should be str
 #else:
 # HG[y][x]=c
 return HG

def grid_set_point(HG,x,y,c,X,Y):
 return spoint(x,y,HG,c,X,Y)

def grid_add_circle(HG,x,y,rmin,rmax,c,X,Y):
 rr=[t for t in nrange(rmin,rmax)] # make static list...
 for i in range(rmax*2):
  ih=int(i/2)+(i%2)
  for j in range(rmax):
   if int(hypot(ih,j)) in rr:
    #xc=0
    #i=i*2
    #i=int(i/2)
    HG=spoint(x+i,y+j,HG,c,X,Y)
    HG=spoint(x+i,y-j,HG,c,X,Y)
    HG=spoint(x-i,y+j,HG,c,X,Y)
    HG=spoint(x-i,y-j,HG,c,X,Y)
 return HG

def add_one_with_dir(x,y,g,d,X,Y,char=''):
 c=''
 if char:
  c=char
 if d=='X':
  x+=2
  if not char:
   c='_'

 if d=='x':
  x-=2
  #x+=2
  if not char:
   c='_'

 if d=='Y':
  x+=1
  y+=1
  #x+=2
  if not char:
   c='\\'

 if d=='y':
  x-=1
  y-=1
  #x+=2
  if not char:
   c='\\'

 if d=='Z':
  x-=1
  y+=1
  #x+=2
  if not char:
   c='/'

 if d=='z':
  x+=1
  y-=1
  #x+=2
  if not char:
   c='/'
 cell=Cell(c,x,y)
 #this will break the nice tri-symmetric grid
 #todo: make sure in future resetting to add the empty space back
 return spoint(x,y,g,cell,X,Y),x,y

def grid_add_line(HG,x,y,size,direction,chars,X,Y):
 ccycle=cycle(chars)
 #DEB=debget()
 #debset(True)
 for i in range(size):
  deb("i:",i,"size:",size)
  #debset(DEB)
  HG,x,y=add_one_with_dir(x,y,HG,direction,X,Y,next(ccycle))
  show(HG,X,Y)
 return HG

