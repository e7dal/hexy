# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import click

from ..cli import pass_hexy
from .. import Hexy

@click.command('point',
               short_help='Put a single point on a grid and show grid in hexy tool')
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
@click.option('--char',
              '-c',
              type=str,
              default='x',
              help='the character to put in the given point i,j')
@pass_hexy
def cli(ctx, xsize,ysize,xpos,ypos,char):
 """Show example for doing some task in hexy(experimental)"""
 ctx.say('grid', stuff=(xsize,ysize),verbosity=100)
 ctx.say('point',stuff=(xpos,ypos,char),verbosity=100)
 if len(char)>1:
  ctx.mumble('point, the character is longer than one, using first char',verbosity=100)
  char=char[0]

 g=Hexy(x=xsize,y=ysize)
 g.point(xpos=xpos,ypos=ypos,char=char)
 click.echo(g.show())
  
