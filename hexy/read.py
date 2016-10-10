from .cell import F,e
from .grid import grid, show,add_one_with_dir
from .util.deb import debset,deb

one=add_one_with_dir

def grid_read(fc=[]):
 #read hexy 'encoded' ascii grid back into an hexy grid
 #fc is the  
 debset(True)
 deb(fc)
 g=[[e]]
 x=1
 y=1
 return g,x,y

