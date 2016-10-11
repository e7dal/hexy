from .cell import F,e
from .grid import grid, show
from .util.deb import debset,deb

#one=add_one_with_dir
def cell(c):
 #if c=='.':return c
 return F(x,y,c)

def make_row(l):
 r=[]
 x=0
 for s in l[2:]:
  print(s)
  if s =='|' and l[x]==':':break
  r.append(s)
  x+=1
 return r,x


def grid_read(fc=[]):
 #read hexy 'encoded' ascii grid back into an hexy grid
 #fc is the  
 #debset(True)
 deb(fc)
 #g=[[e]]
 x=0
 y=0
 g=[]
 for l in fc[2:-2]:
  print('>',l,'<')
  r,x=make_row(l)
  g.append(r)
  y+=1
 #x
 print( g,x,y)
 return g,x,y

