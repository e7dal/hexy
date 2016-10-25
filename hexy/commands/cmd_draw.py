# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.
import time
import click

from ..cli import pass_hexy
from .. import Hexy
from ..util.nrange import nrange

@click.command('draw',
               short_help='Draw and show grid in hexy')
@click.option('--xsize',
              '-x',
              type=int,
              default=10,
              help='show the example with the name')
@click.option('--ysize',
              '-y',
              type=int,
              default=10,
              help='show the example with the name')
@click.option('--xpos',
              '-i',
              type=int,
              default=3,
              help='show the example with the name')
@click.option('--ypos',
              '-j',
              type=int,
              default=3,
              help='show the example with the name')
@click.option('--size',
              '-s',
              type=int,
              default=3,
              help='show the example with the name')
@click.option('--clear',
              '-c',
              is_flag=True,
              default=False,
              help='clear when animating')
@click.option('--animate',
              '-a',
              is_flag=True,
              default=False,
              help='show animation for the nrange of size')
@pass_hexy
def cli(ctx, xsize,ysize,xpos,ypos,size,clear,animate):
 """Show example for doing some task in hexy(experimental)"""
 ctx.say('grid', stuff=(xsize,ysize),verbosity=100)
 g=Hexy(x=xsize,y=ysize)
 #g.draw(1,1,3,'X')
 if animate:
  
  for i in nrange(size):
   start=time.clock()
   if clear:
    g=Hexy(x=xsize,y=ysize)
   g.draw(xpos=xpos,ypos=ypos,size=i)
   time.sleep(.1)
   click.clear()
   g.show()
   end=time.clock()
   print('took:%.2f size:%d'%(end-start,i))
   
 else:
   g.draw(xpos=xpos,ypos=ypos,size=size)
   g.show()
  
