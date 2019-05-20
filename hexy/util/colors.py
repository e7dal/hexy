from colored import fg,bg,attr

def color(i,m):
 return '%s%s%s'%(fg(i),m,attr(0))

def bcolor(i,m):
 return '%s%s%s'%(bg(i),m,attr(0))

C={ 'CURRCOLOR':0,
    'CURRCOLORFUN':0,
    'BGCURRCOLOR':127,
    'COUNT':0,
    'FN':3,
    'FFG':1000,
    'FBG':2000}

def cycling_color(c,bg=True):
 if C['COUNT']%C["FFG"] == 0:
  C["CURRCOLOR"]+=1
  C["CURRCOLOR"]%=256
  #C["FFG"]=fib(C["FN"])
  #C["FN"]+=1
 if C["COUNT"]%C["FBG"] == 0:
  C["BGCURRCOLOR"]+=1
  C["BGCURRCOLOR"]%=256
  #C["FBG"]=fib(C["FN"])
  #C["FN"]+=1
 if bg:
  #return bcolor(C["BGCURRCOLOR"],color(C["CURRCOLOR"],c))
  return bcolor(C["BGCURRCOLOR"],c)
 return  color(C["CURRCOLOR"],c)

def cycling_color_fun():
 C["CURRCOLORFUN"]+=1
 C["CURRCOLORFUN"]%=256
 def colorer(c):return color(C['CURRCOLORFUN'],c)
 return colorer

