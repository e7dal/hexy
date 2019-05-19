from colored import fg,bg,attr

def color(i,m):
 return '%s%s%s'%(fg(i),m,attr(0))

def bcolor(i,m):
 return '%s%s%s'%(bg(i),m,attr(0))


#def fib(i=0):
# if i == 0: yield 1
# if i == 1: yield 1
# if i >1 and i < 100: yield fib(i-1)+fib(i-2)
F=[0,1]
def fib(n=1):
 #print(n,len(F))
 if len(F) >= n:
  return F[n-1]
 for i in range(len(F),n):
  F.append(F[-1]+F[-2])
 return F[n-1]


def fibd(n=1):
 if n == 1: return 0
 if n == 2: return 1
 P1=0
 P2=1
 for i in range(3,n):
  T=P1+P2
  P2=P1
  P1=T
 return T

C={ 'CURRCOLOR':0,
    'BGCURRCOLOR':127,
    'COUNT':0,
    'FN':3,
    'FFG':1000,
    'FBG':2000}

def cycling_color(c,bg=True):
 """
 global FN
 global CURRCOLOR
 global FFC
 global BGCURRCOLOR
 global FBC
 global COUNT
 COUNT+=1
 """
 if C['COUNT']%C["FFG"] == 0:
  C["CURRCOLOR"]+=1
  C["CURRCOLOR"]%=255
  C["FFG"]=fib(C["FN"])
  C["FN"]+=1
 if C["COUNT"]%C["FBG"] == 0:
  C["BGCURRCOLOR"]+=1
  C["BGCURRCOLOR"]%=255
  C["FBG"]=fib(C["FN"])
  C["FN"]+=1
 if bg:
  #return bcolor(C["BGCURRCOLOR"],color(C["CURRCOLOR"],c))
  return bcolor(C["BGCURRCOLOR"],c)
 return  color(C["CURRCOLOR"],c)

CURRCOLORFUN=0
def cycling_color_fun():
 global CURRCOLORFUN
 CURRCOLORFUN+=1
 def colorer(c):return color(CURRCOLORFUN,c)
 return colorer

