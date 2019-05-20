# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.
import sys
import time
from itertools import cycle
import click

from ..cli import pass_hexy
from .. import Hexy
from ..util.nrange import nrange

def hcc_get(ctx,name,cfg_type):
 val=ctx.get_config(name)
 if val: #todo:if False...?
     val=cfg_type(int(val))
 else:
     val=False
 return val


@click.command('rotate',
               short_help='Rotate a given amount of 90 degree turn')
@click.option('--gridfile',
              '-g',
              type=click.File('rb'),
              default=sys.stdin,
              help='the file to read from')
@click.option('--amount',
              '-a',
              type=int,
              default=1,
              help='rotate 90 degree counter clockwise(CCW)')
@click.option('--clockwise',
              '-c',
              type=bool,
              default=False,
              help='rotate clockwise(CW)')
@pass_hexy
def cli(ctx, gridfile, amount, clockwise):
 """ rotate grid given amount of 90 degree CCW """
 ctx.say('rotate', stuff=(gridfile,amount,clockwise),verbosity=100)
 
 hr=Hexy()
 fc=gridfile.readlines()
 r=hr.read(fc)
 ctx.say('rotate read',stuff=r,verbosity=100)
 click.echo(hr.show())
 #g=Hexy(x=xsize,y=ysize)

 showinfo = hcc_get(ctx,'showinfo',bool)
 clear    = hcc_get(ctx,'clear',   bool)

 hw=Hexy()
 from IPython import embed; embed()
 click.clear()
 click.echo(hw.show())
 if showinfo:
    print('took:%.2f size:%d/%d interval:%.2f clear:%s direction:%s'%(end-start,i,size,interval,clear,direction))




  
