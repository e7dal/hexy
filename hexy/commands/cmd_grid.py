# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import click

from ..cli import pass_hexy
from .. import Hexy

@click.command('grid',
               short_help='Show empty grid in hexy')
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
@pass_hexy
def cli(ctx, xsize,ysize):
 """Show example for doing some task in hexy(experimental)"""
 ctx.say('grid', stuff=(xsize,ysize),verbosity=100)
 g=Hexy(x=xsize,y=ysize)
 g.show()
  
