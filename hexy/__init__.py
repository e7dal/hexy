# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import os
import sys
import arrow

from .util.bubble import Bubble
from .grid import grid_make, grid_show
from .draw import grid_draw

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
 def __init__(self,x,y):
  self.X=x
  self.Y=y
  self.grid=grid_make(x,y)
 def show(self):
  grid_show(self.grid)
 def draw(self,xpos,ypos,size):
  grid_draw(self.grid,xpos,ypos,size)

if __name__=='__main__':
 h=Hexy(12,6)
 h.show()
 h.draw(2,2,3)
 h.show()
