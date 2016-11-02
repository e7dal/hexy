def grid_cslice(HG,f,t,d):
 if d=='V':
  ng=HG[f:t]
 if d=='H':
  ng=[]
  for r in HG:
   ng.append(r[f:t])
 return ng

 #todo other directions,x,y,x, btw H=x
 #y=len(HG)
 #x=len(HG[0])
 #if x%2:
 # x+=1
 #debset(True)
 #deb('slice:res:', ng,x,y)
 #debset(False)

