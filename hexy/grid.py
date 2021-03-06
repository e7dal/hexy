#123456789012345678901234567890123456789012 #
from operator import xor
from itertools import cycle
from math import hypot
#123456789012345678901234567890123456789012 #
from .util.deb import debget,debset,deb
from .util.nrange import nrange
from .util.colors import color,cycling_color,cycling_color_fun
from .cell import Cell,GRIDCHAR

#123456789012345678901234567890123456789012 #
#todo put these in magic configuration/constants.
#b=':'           # the border character
bb=':|'           # the border character
be='|:'           # the border character

#123456789012345678901234567890123456789012 #
dirs={}
dirs['X']={'xd': 2,'yd': 0,'c':'_'}
dirs['x']={'xd':-2,'yd': 0,'c':'_'}
dirs['Y']={'xd': 1,'yd': 1,'c':'\\'}
dirs['y']={'xd':-1,'yd':-1,'c':'\\'}
dirs['Z']={'xd':-1,'yd': 1,'c':'/'}
dirs['z']={'xd': 1,'yd':-1,'c':'/'}
#123456789012345678901234567890123456789012 #
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

#123456789012345678901234567890123456789012 #
def grid_make(x,y):
 return grid([],x,y)

#123456789012345678901234567890123456789012 #
def greset(HG=[],xsize=7,ysize=5):
 X=xsize
 Y=ysize
 for y in nrange(Y):
  for x in nrange(X*2):
   if xor(x%2,y%2):
    HG[y-1][x-1]=Cell(GRIDCHAR,x,y)
 return HG

#123456789012345678901234567890123456789012 #
def grid_reset(HG,x,y):
 return greset(HG,x,x)

#123456789012345678901234567890123456789012 #
def _bordered(s=''):return bb+s+be
_b=_bordered
#123456789012345678901234567890123456789012 #
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

#123456789012345678901234567890123456789012 #
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

#123456789012345678901234567890123456789012 #
def fill(HG,l,c=' '):
 deb('fill',l,c)
 for x,y in l:
  if isinstance(c,str):
   HG[y][x].set(c,x=x,y=y)
  else:
   HG[y][x].set(c.get())
 return HG

#123456789012345678901234567890123456789012 #
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

#123456789012345678901234567890123456789012 #
def grid_set_point(HG,x,y,c,X,Y):
 c=Cell(c,x,y)
 return spoint(x,y,HG,c)

#123456789012345678901234567890123456789012 #
def grid_add_circle(HG,x,y,rmin,rmax,chars,X,Y):
 rr=[t for t in nrange(rmin,rmax)] # make static list...
 #ind=0
 ccycle=cycle(chars)
 cfun=cycling_color_fun()
 for i in range(rmax*2):
  ih=int(i/2)+(i%2)
  for j in range(rmax):
   if int(hypot(ih,j)) in rr:
    c=Cell(cfun(next(ccycle)),0,0)
    HG=spoint(x+i,y+j,HG,c)
    c=Cell(cfun(next(ccycle)),0,0)
    HG=spoint(x+i,y-j,HG,c)
    c=Cell(cfun(next(ccycle)),0,0)
    HG=spoint(x-i,y+j,HG,c)
    c=Cell(cfun(next(ccycle)),0,0)
    HG=spoint(x-i,y-j,HG,c)
 return HG

#123456789012345678901234567890123456789012 #
def add_one_with_dir(x,y,g,d,X,Y,char=''):
 x+=dirs[d]['xd']
 y+=dirs[d]['yd']
 c=char
 if not char:
  c=dirs[d]['c']

 cell=Cell(cycling_color(c),x,y)
 #this will break the nice tri-symmetric grid
 #todo: make sure in future resetting to add the empty space back
 return spoint(x,y,g,cell),x,y

#123456789012345678901234567890123456789012 #
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

#123456789012345678901234567890123456789012 #
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
#123456789012345678901234567890123456789012 #
