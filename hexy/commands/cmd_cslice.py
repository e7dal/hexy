# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import click
import sys

from ..cli import pass_hexy
from .. import Hexy

@click.command('cslice',
               short_help='Select a slice out of the cycled grid (cilinder), in given direction')
@click.option('--gridfile',
              '-g',
              type=click.File('rb'),
              default=sys.stdin,
              help='the file to read from,todo type file ')
@click.option('--fromindex',
              '-f',
              type=int,
              default=0,
              help='slice from index in the grid')
@click.option('--toindex',
              '-t',
              type=int,
              default=0,
              help='slice to index in the grid')
@click.option('--direction',
              '-d',
              type=str,
              default='H',
              help='one the axis directions H,V,x,y,z')

@pass_hexy
def cli(ctx, gridfile,fromindex,toindex,direction):
 """Show example for doing some task in hexy(experimental)"""
 ctx.say('slice', stuff=(gridfile,
                        fromindex,
                        toindex,
                        direction),verbosity=100)
 hr=Hexy()
 fc=gridfile.readlines()
 r=hr.read(fc)
 ctx.say('read',stuff=r,verbosity=100)
 if direction=='H':
  if (toindex-fromindex)%2==1:
    ctx.cry('due to the nature of the hexy grid, in the H or x direction we cannot draw a ruler for uneven range, adjusting toindex+=1')
    toindex+=1
 s=hr.cslice(fromindex,toindex,direction)
 click.echo(hr.show())



