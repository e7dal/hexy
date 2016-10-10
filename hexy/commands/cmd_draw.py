# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import click

from ..cli import pass_hexy
from .. import Hexy

@click.command('draw',
               short_help='Draw and show grid in hexy')
@click.option('--xsize',
              '-x',
              type=int,
              default=7,
              help='show the example with the name')
@click.option('--ysize',
              '-y',
              type=int,
              default=4,
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
 ctx.say('grid', stuff=(xsize,ysize),verbosity=100)
 g=Hexy(x=xsize,y=ysize)
 #g.draw(1,1,3,'X')
 g.draw(xpos=xpos,ypos=ypos,size=size)
 g.show()
  
