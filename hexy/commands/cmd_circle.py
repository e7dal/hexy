# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import click

from ..cli import pass_hexy
from .. import Hexy

@click.command('circle',
               short_help='Put a fuzzy circle on an hexy  grid')
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
              help='set the y position for the point')
@click.option('--rmin',
              '-r',
              type=int,
              default=3,
              help='set the minimum for radius to add apoint on the circle')
@click.option('--rmax',
              '-R',
              type=int,
              default=5,
              help='set the maxiimum for radius to add apoint on the circle')
@click.option('--char',
              '-c',
              type=str,
              default='x',
              help='the character to put in the given point i,j')
@pass_hexy
def cli(ctx, xsize,ysize,xpos,ypos,rmin,rmax,char):
 """Add a circle to the hexy grid with a range radius"""
 ctx.say('grid', stuff=(xsize,ysize),verbosity=100)
 ctx.say('circle',stuff=(xpos,ypos,rmin,rmax,char),verbosity=100)

 g=Hexy(x=xsize,y=ysize)
 g.circle(xpos=xpos,ypos=ypos,rmin=rmin,rmax=rmax,char=char)
 g.show()
 g.reset()
 g.show()
  
