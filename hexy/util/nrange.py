import arrow
from .deb import deb,debset

def nrange(i,j=None,step=1):
 deb('nrange',i,j,step)
 if step!=1:
  return range(i+1,j+1,step)
 if j:
  return range(i+1,j+1)
 else:
  return range(1,i+1)

if __name__=='__main__':
 debset(True)
 print(nrange(7))
 print(nrange(3,7))
 print(nrange(1,7,2))
 print(nrange(7,1,-2))
