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
@pass_hexy
def cli(ctx, xsize,ysize,xpos,ypos,size):
 """Show example for doing some task in hexy(experimental)"""
 ctx.say(stuff=ctx)
 animate=ctx.get_config('animate')
 clear=ctx.get_config('clear')
 ctx.say('grid', stuff=(xsize,ysize),verbosity=100)
 g=Hexy(x=xsize,y=ysize)
 if animate:
  for i in nrange(size):
   start=time.clock()
   if clear:
    g=Hexy(x=xsize,y=ysize)
   g.draw(xpos=xpos,ypos=ypos,size=i)
   time.sleep(.1)
   click.clear()
   click.echo(g.show())
   end=time.clock()
   print('took:%.2f size:%d'%(end-start,i))
 else:
   g.draw(xpos=xpos,ypos=ypos,size=size)
   click.echo(g.show())
  
