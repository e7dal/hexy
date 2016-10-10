import re
def rem(s,r,flags=0):
 return re.match(s,r,flags) 

if __name__=='__main__':
 import biot 
 #DEBASS=True
 s='E7dal'
 r='.*'
 res=rem(r,s)
 biot.ass('==',True,res)

