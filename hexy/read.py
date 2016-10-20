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
  deb('make_row:curr:c',s)
  if l=="\n":break
  if s=='|' and l[x+3]==':':break
  r.append(s)
  deb('make_row:curr:r',r)
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
 #for l in fc[2:-2]: # make sure the empty lines are stripped
 for l in fc[2:-3]:
  deb('read line:>',l,len(l),'<')
  ls=l.strip()
  if ls!=l:deb('stripped',len(ls))
  r,x=make_row(ls)
  g.append(r)
  y+=1

 deb('read:res:', g,x,y)
 return g,x,y

