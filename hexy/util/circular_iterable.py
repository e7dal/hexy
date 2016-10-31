from collections import Iterable
class circluar_iterable():
 def __init__(i,it):
  if isinstance(it,Iterable):
   i.ol=it
  else:
   i.ol=[it] #just make it iterable
 def __getitem__(i,s):
  r=''
  if isinstance(s,int):
   s=range(s,1,s+1)
   step =s.step
   if not step:
    step=1
   stop =s.stop
   for p in range(start,step,stop):
    yield i.__getitemcircular__(p)
 def __getitemcircular__(i,p):
   l=len(i.ol)
   while p<0:
    p+=l
   p%=l
   r=i.ol[p]
