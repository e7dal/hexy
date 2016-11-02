from colored import fg,bg,attr
#from a import a
#from d import d
#from m import m
#from p import p
#from r import r
def c(i,m):
 i=i%255
 return '%s%s%s'%(fg(i),m,attr(0))

def b(i,m):
 i=i%255
 return '%s%s%s'%(bg(i),m,attr(0))

def D():
 s=''
 x='colors available'
 l=len(x)
 for i in range(1,l+1):
  s+=c(i*10,x[i-1])
 print(s) 

#a(c(65,'colors available'))
for i in range(0,256,1):
  print(c(i,str(i)))
  print(b(i,str(i)))

