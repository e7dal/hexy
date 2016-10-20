# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import click

from ..cli import pass_hexy
from .. import Hexy

@click.command('point',
               short_help='Put a single line with direction(xyz) and size in hexy')
@click.option('--xsize',
              '-x',
              type=int,
              default=10,
              help='set the x size (horizontal) for the grid')
@click.option('--ysize',
              '-y',
              type=int,
              default=10,
              help='set the y size (vertical) for the grid')
@click.option('--xpos',
              '-i',
              type=int,
              default=3,
              help='set the x position for the point')
@click.option('--ypos',
              '-j',
              type=int,
              default=3,
              help='set the y posistin for the point')
@click.option('--size',
              '-s',
              type=int,
              default=3,
              help='set the size for the line')
@click.option('--chars',
              '-c',
              type=str,
              default='X',
              help='the cycled character(s) to put in the given line from i,j')
@click.option('--direction',
              '-d',
              type=str,
              default='x',
              help='the direction in positive: x,y,z or negative: X,Y,Z')
@pass_hexy
def cli(ctx, xsize,ysize,xpos,ypos,size,chars,direction):
 """ Add a line with a direction and a string to get characters to put on line """
 ctx.say('grid', stuff=(xsize,ysize),verbosity=100)
 ctx.say('line',stuff=(xpos,ypos,size,direction,chars),verbosity=100)

 g=Hexy(x=xsize,y=ysize)
 g.line(xpos=xpos,ypos=ypos,chars=chars,direction=direction,size=size)
 g.show()
  
