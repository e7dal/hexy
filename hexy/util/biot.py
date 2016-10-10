import operator as o

RERAISE=False
DEBASS=False
DEBASS=True

if DEBASS:
 def deb(*a):print('DEB:BIOT:',*a)
else:
 def deb(*a):pass

T=True
F=False
N=None

_o={}
_o['=='] = o.eq
_o['!='] = o.ne
_o['<']  = o.lt
_o['<='] = o.le
_o['>']  = o.gt
_o['>='] = o.ge
deb('_o=',_o)
def ass(o='==',l=True,r=True):
 deb('ASS:',o,l,r)
 try:
  assert _o[o](l,r)
  deb('ASS:ok')
 except AssertionError as ae:
  if RERAISE:
   deb('ASS:NO,reraising')
   raise ae
  deb('ASS:NO,noreraise')
 
 
if __name__=='__main__':
 DEBASS=True
 ass()           #defaults ok
 ass('==',1,1)
 ass('!=',2+2,5)
 ass('==',2+2,5) #assertion error no raise

