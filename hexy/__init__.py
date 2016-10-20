# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import os
import sys
import arrow

from .util.bubble import Bubble
from .util.deb import deb,debset
from .grid import grid_make, grid_show, grid_set_point
from .draw import grid_draw
from .read import grid_read
from .cursor import grid_cursor

HEXY_START_ARROW=arrow.now()


from . import metadata

"""hexy, hexagonal ascii drawing toolkit"""
HEXY_SIMPLE_LOGO = """
#:     _ _ _ _
#:    / _ _ _ \
#:   / / _ _ \ \
#:  / / / _ \ \ \
#:  \ \ \_ _/ / /
#:   \ \_ _ _/ /
#:    \_ _ _ _/
#:     
"""

__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright


class Hexy(object):
 """ basic Hexagonal grid manager """
 def __init__(self,x=1,y=1):
  self.X=x
  self.Y=y
  #cursor
  self.cx=None
  self.cy=None
  self.cformat=None
  self.grid=grid_make(x,y)
 def show(self):
  grid_show(self.grid)
 def draw(self,xpos,ypos,size):
  grid_draw(self.grid,xpos,ypos,size,self.X,self.Y)
 def cursor(self,xpos,ypos,cformat):
  self.cx=xpos
  self.cy=ypos
  self.cformat=cformat
  self.grid=grid_cursor(self.grid,xpos,ypos,cformat,self.X,self.Y)
 def point(self,xpos,ypos,char):
  #self.cx=xpos
  #self.cy=ypos
  #self.cformat=cformat
  self.grid=grid_set_point(self.grid,xpos,ypos,char,self.X,self.Y)
 def read(self,fc=[]):
  g,x,y=grid_read(fc)
  self.X=x
  self.Y=y
  self.grid=g
  deb('read:',g,x,y)
  #return g,x,y
  #return self

if __name__=='__main__':
 h=Hexy(12,6)
 h.show()
 h.draw(2,2,3)
 h.show()
 hr=Hexy()
 fc=[':|1 |:',
     ':|__|:',
     ':|. |:1',
     ':|__|:',
     ':| 1|:']
 r=hr.read(fc)
 print(r)
