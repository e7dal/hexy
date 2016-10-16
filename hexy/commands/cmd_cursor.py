# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import click

from ..cli import pass_hexy
from .. import Hexy

@click.command('cursor',
               short_help='Add a cursor on point')
@click.option('--xpos',
              '-i',
              type=int,
              default=3,
              help='cursor x position')
@click.option('--ypos',
              '-j',
              type=int,
              default=3,
              help='cursor y posistion')
@click.option('--cformat',
              '-c',
              type=str,
              default="_|_|",
              help='cursor format, 4 characters which define the cursor LeftUpRightDown,for example <^>v')
@pass_hexy
def cli(ctx,xpos,ypos,cformat):
 """Show example for doing some task in hexy(experimental)"""
 ctx.say('cursor', stuff=(xpos,ypos),verbosity=100)
 #todo: this should be read, or at the very least kept in some object
 g=Hexy(10,10)
 #g.draw(1,1,3,'X')
 g.cursor(xpos=xpos,ypos=ypos,cformat=cformat)
 g.show()
 #todo: this should be written, or at the very least saved in some object
