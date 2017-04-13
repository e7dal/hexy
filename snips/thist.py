import hexy
import hexy.util.nrange
h=hexy.Hexy(x=10,y=10)
for i in hexy.util.nrange.nrange(10,100,3):
 h.draw(1,2,i)
 print(h.show())
for f in h.grid:
 for i in f:
  print(len(i._hist))

