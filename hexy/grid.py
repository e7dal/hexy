from operator import xor
from itertools import cycle
from math import hypot

from .util.deb import debget,debset,deb
from .util.nrange import nrange
from .util.colors import color,cycling_color
from .cell import Cell,GRIDCHAR

#todo put these in magic configuration/constants.
#b=':'           # the border character
bb=':|'           # the border character
be='|:'           # the border character

def grid(HG=[],xsize=7,ysize=5):
 X=xsize
 Y=ysize
 for y in nrange(Y):
  HG.append([])
  for x in nrange(X*2):
   if xor(x%2,y%2):
    HG[y-1].append(Cell(' ',x=x,y=y))
   else:
    HG[y-1].append(Cell(GRIDCHAR,x=x,y=y))
 return HG

def grid_make(x,y):
 return grid([],x,y)

def greset(HG=[],xsize=7,ysize=5):
 X=xsize
 Y=ysize
 for y in nrange(Y):
  for x in nrange(X*2):
   if xor(x%2,y%2):
    HG[y-1][x-1]=Cell(GRIDCHAR,x,y)
 return HG

def grid_reset(HG,x,y):
 return greset(HG,x,x)

def _bordered(s=''):return bb+s+be
_b=_bordered

def show(HG,X,Y):
 i=1
 r=[]
 X=len(HG[0])
 xc=X%2
 X=int(X/2)#+2*xc
 Y=len(HG)

 xr=xruler(X,Y)
 r.append(_b(xr))
 r.append(_b('_'*(len(xr))))
 for l in HG:
  s=''
  for c in l:
   s+=str(c.get())
  r.append(_b(s)+str(i))
  i+=1
 r.append(_b('_'*(len(xr))))
 if Y%2==0 and X > 0:
  r.append(_b(' '+xr[0:-1]))
 else:
  if X==0:
   r.append(_b())
  else:
   r.append(_b(xr))
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
   HG[y][x].set(c.get())
 return HG

def spoint(x,y,HG,c):
 deb('spoint',x,y,c)
 assert isinstance(c,Cell)
 X=len(HG[0]) #len ..self
 Y=len(HG)

 XL=X-1
 YL=Y-1
 x,y=x-1,y-1
 x,y=x%X,y%Y

 #shift up
 if x<0:x+=XL
 if y<0:y+=YL
 #shift down
 if x>XL:x-=XL
 if y>XL:y-=YL
 HG[y][x].set(c.get())
 return HG

def grid_set_point(HG,x,y,c,X,Y):
 c=Cell(c,x,y)
 return spoint(x,y,HG,c)

_hyp={}
def hyp(a,b):
   global _hyp
   k='%d,%d'%(a,b)
   if k in _hyp:return _hyp[k]
   _hyp[k]=int(hypot(a,b))
   return _hyp[k]

def grid_add_circle(HG,x,y,rmin,rmax,chars,X,Y):
 rr=[t for t in nrange(rmin,rmax)] # make static list...
 #ind=0
 ccycle=cycle(chars)
 for i in range(rmax*2):
  ih=int(i/2)+(i%2)
  for j in range(rmax):
   if hyp(ih,j) in rr:
    c=Cell(cycling_color(next(ccycle)),0,0)
    HG=spoint(x+i,y+j,HG,c)
    c=Cell(cycling_color(next(ccycle)),0,0)
    HG=spoint(x+i,y-j,HG,c)
    c=Cell(cycling_color(next(ccycle)),0,0)
    HG=spoint(x-i,y+j,HG,c)
    c=Cell(cycling_color(next(ccycle)),0,0)
    HG=spoint(x-i,y-j,HG,c)
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
 cell=Cell(cycling_color(c,bg=False),x,y)
 #this will break the nice tri-symmetric grid
 #todo: make sure in future resetting to add the empty space back
 return spoint(x,y,g,cell),x,y

#def grid_add_line(HG,x,y,size,direction,chars,X,Y):
def _get_dim(HG): return len(HG[1]),len(HG)
def grid_add_line(HG,x,y,size,direction,chars,X=None,Y=None):
 if not X:
  X,Y=_get_dim(HG)
 #print(x,y,size,direction,chars)
 ccycle=cycle(chars)
 #DEB=debget()
 #debset(True)
 for i in range(size):
  deb("i:",i,"size:",size)
  #debset(DEB)
  nc=next(ccycle)
  cnc=cycling_color(nc)
  HG,x,y=add_one_with_dir(x,y,HG,direction,X,Y,cnc)
  show(HG,X,Y)
 return HG,x,y

def grid_add_hexagon(HG,x,y,size,chars=''):
 ccycle=cycle(chars)
 hexpath='XYZxyz'
 z =( 0, 0)
 xp=( 1, 0)
 xm=(-1, 0)
 yp=( 0, 1)
 ym=( 0,-1)
 adjust=[z,z,xp,xp,yp,xm]
 #print(adjust)
 #dcycle=cycle(hexpath)
 for i in range(len(hexpath)):
  xa,ya=adjust[i]
  x+=xa
  y+=ya
  HG,x,y=grid_add_line(HG,x,y,size-1,hexpath[i],ccycle)
