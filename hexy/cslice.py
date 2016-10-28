from .cell import F,e
from .read import cell #is just F...,move todo:
from .util.deb import debset,deb

def grid_cslice(HG,f,t,d):
 if d=='V':
  ng=HG[f:t]
 if d=='H':
  ng=[]
  for r in HG:
   ng.append(r[f:t])
 #todo other directions,x,y,x, btw H=x
 #y=len(HG)
 #x=len(HG[0])
 #if x%2:
 # x+=1
 #debset(True)
 #deb('slice:res:', ng,x,y)
 #debset(False)
 return ng

