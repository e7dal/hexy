# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import click
import sys

from ..cli import pass_hexy
from .. import Hexy

@click.command('read',
               short_help='Read ascii grid into an hexy grid')
@click.option('--gridfile',
              '-g',
              type=click.File('rb'),
              default=sys.stdin,
              help='the file to read from,todo type file ')
@pass_hexy
def cli(ctx, gridfile):
 """Show example for doing some task in hexy(experimental)"""
 ctx.say('read', stuff=(gridfile),verbosity=100)
 hr=Hexy()
 fc=[':|1 |:',
     ':|__|:',
     ':|. |:1',
     ':|__|:',
     ':| 1|:']
 fc=gridfile.readlines()
 r=hr.read(fc)
 ctx.say('read',stuff=r,verbosity=100)
 click.echo(hr.show())
  
