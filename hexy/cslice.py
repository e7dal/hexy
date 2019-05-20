def grid_cslice(HG,f,t,d):
 if d=='V':
  ng=HG[f:t]
 if d in ['H','x']:
  ng=[]
  for r in HG:
   ng.append(r[f:t])
 if d=='y':
  ng=grid_cslice(HG,f,t,'H')
  ng=grid_cslice(ng,f,t,'V')
 if d=='z':
  ng=grid_cslice(HG,f,t,'H')
  ng=grid_cslice(ng,f,t,'V')
 return ng
