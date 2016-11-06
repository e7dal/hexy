from colored import fg,bg,attr
#from a import a
#from d import d
#from m import m
#from p import p
#from r import r
def color(i,m):
 i=i%255
 return '%s%s%s'%(fg(i),m,attr(0))

def bcolor(i,m):
 i=i%255
 return '%s%s%s'%(bg(i),m,attr(0))

CURRCOLOR=0
def cycling_color(c):
 global CURRCOLOR
 CURRCOLOR+=1
 return color(CURRCOLOR,c)
