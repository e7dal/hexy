# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.
from itertools import cycle
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
#@click.option('--sizeend', like circle r->R?
#              '-s',
#              type=int,
#              default=3,
#              help='show the example with the name')
@pass_hexy
def cli(ctx, xsize,ysize,xpos,ypos,size):
 """Show example for doing some task in hexy(experimental)"""
 ctx.say(stuff=ctx)
 animate=ctx.get_config('animate')
 clear=ctx.get_config('clear')
 pulse=ctx.get_config('pulse')
 repeat=ctx.get_config('repeat')
 move=ctx.get_config('move')
 keep=ctx.get_config('keep')

 ctx.say('grid', stuff=(xsize,ysize),verbosity=100)
 g=Hexy(x=xsize,y=ysize)

 def nr(s,pulse,repeat):
  r=[]
  for i in range(s):
   r.append(i)
  if pulse:
   for i in range(s,1,-1):
    r.append(i)
  if repeat:
   return cycle(r)
  return r
 def pos(xpos,ypos):
  while True:
   xpos+=2
   ypos+=1
   print(xpos,ypos)
   yield (xpos,ypos)


 if animate:
  for i in nr(size,pulse,repeat):
   start=time.monotonic()
   if clear:
    g=Hexy(x=xsize,y=ysize)
   p=next(pos(xpos,ypos))
   g.draw(xpos=p[0],ypos=p[1],size=i)
   time.sleep(.1)
   click.clear()
   click.echo(g.show())
   end=time.monotonic()
   print('took:%.2f size:%d / %d '%(end-start,i,size))
 else:
   g.draw(xpos=xpos,ypos=ypos,size=size)
   click.echo(g.show())
  
