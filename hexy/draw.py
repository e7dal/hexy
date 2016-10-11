from .cell import F,e
from .grid import grid, show,add_one_with_dir
from .util.deb import debset

one=add_one_with_dir

#def hexy(g,x,y,s):
def grid_draw(g,x,y,s,X,Y):
 #debset(True)
 for i in range(s):
  g,x,y=one(x,y,g,'X',X,Y)
 for i in range(s-1):
  g,x,y=one(x,y,g,'Y',X,Y)
 x+=1
 for i in range(s-1):
  g,x,y=one(x,y,g,'Z',X,Y)
 x+=1
 for i in range(s):
  g,x,y=one(x,y,g,'x',X,Y)
 y+=1
 for i in range(s-1):
  g,x,y=one(x,y,g,'y',X,Y)
 x-=1
 for i in range(s-1):
  g,x,y=one(x,y,g,'z',X,Y)
 return g,x,y

if __name__=='__main__':
 g=grid()
 sx=14
 sy=4

 x=sx
 y=sy
 s=4 #size
 #inner
 g,x,y=grid_draw(g,x,y,s)
 x=sx-1
 y=sy-1
 s=s+1
 #outer
 g,x,y=grid_draw(g,x,y,s)
 show(g)
