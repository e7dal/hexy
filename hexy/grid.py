#from pprint import pprint as pp
from operator import xor
from itertools import cycle
from math import hypot

#import arrow

from .util.deb import debget,debset,deb
from .util.nrange import nrange
from .cell import F,e

#todo put these in magic configuration/constants.
b=':'
GRIDCHAR='.'

def grid(HG=[],xsize=7,ysize=5):
 X=xsize
 Y=ysize

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

def show(HG,X,Y):
 i=1
 r=[]
 xr=xruler(X,Y)
 r.append(b+"|"+xr+"|"+b)
 r.append(b+"|"+'_'*(len(xr))+"|"+b)
 for l in HG:
  s=''
  for c in l:  
   s+=str(c)
  r.append(b+"|"+ s + "|"+b+str(i))
  i+=1
 r.append(b+"|"+'_'*(len(xr))+"|"+b)
 if Y%2==0 and X > 0:
  r.append(b+"|"+str(e)+xr[0:-1]+"|"+b)
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
 print(rs)

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

def fill(HG,l,c='X'):
 deb('fill',l,c)
 for x,y in l:
  if isinstance(c,str):
   HG[y][x].set(c,x=x,y=y)
  else:
   HG[y][x]=c
 return HG

def spoint(x,y,HG,c,X,Y):
 deb('spoint',x,y,c)
 
 x,y=x-1,y-1
 #xc,yc=int(y/Y),int(x/Y) #correction
 #xc,yc=xc*Y,yc*X#correction
 #x,y=x+xc,y+yc           #correction
 x,y=x%(2*X),y%Y
 if isinstance(HG[y][x],F):
  if isinstance(c,F):
   HG[y][x].set(c.get())
  else:
   HG[y][x].set(c) #fingers crossed, should be str
 else:
  HG[y][x]=c
 return HG

def grid_set_point(HG,x,y,c,X,Y):
 return spoint(x,y,HG,c,X,Y)

def grid_add_circle(HG,x,y,rmin,rmax,c,X,Y):
 #print('todo:ciircle', rmin,rmax)
 #rr=nrange(rmin,rmax) # make static list...
 rr=[t for t in nrange(rmin,rmax)] # make static list...
 for i in range(rmax*2):
  for j in range(rmax):
   if int(hypot(i,j)) in rr:
    xc=0
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
 cell=F(c,x,y)
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

if __name__=='__main__':
 g=grid(xsize=12,ysize=8)
 show(g)
