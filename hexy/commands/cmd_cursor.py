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
 c=''
 
 g=Hexy(10,10)
 g.cursor(xpos=xpos,ypos=ypos,cformat=cformat)
 click.echo(g.show())
 move=False
 if not move:return
 click.echo("please use  u,d,l,r (up,down,left,right for cursor movement")
 while c!='q':
  c=click.getchar()
  if c=='u':ypos-=1
  if c=='d':ypos+=1
  if c=='l':xpos-=1
  if c=='r':xpos+=1
  g.reset()
  g.cursor(xpos=xpos,ypos=ypos,cformat=cformat)
  click.echo(g.show())
  click.echo("cursor pos: xpos=%d ypos=%d cursor move:%s"%(xpos,ypos,c))
