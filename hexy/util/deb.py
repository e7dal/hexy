import time

_DEB=False

def deb(*a):
 if debget(): print(time.clock(),a)

def debset(d):
 global _DEB
 _DEB=d

def debget():
 global _DEB
 return _DEB

if __name__=='__main__':
 debset(True)
 print('deb',debget())
 deb('show:)')
 debset(False)
 print('deb',debget())
 deb('no show:(')
