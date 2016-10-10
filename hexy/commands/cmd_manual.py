# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import click
import os
import subprocess
from ..cli import pass_hexy,hexy_lib_dir

@click.command('manual', short_help='Shows the man page packed inside the hexy tool')
@pass_hexy
def cli(ctx):
    """Shows the man page packed inside the hexy tool

    this is mainly too overcome limitations on installing manual pages in a distribution agnostic and simple way
    and the way hexy has been developed, in virtual python environments,
    installing a man page into a system location makes no sense,
    the system manpage will not reflect the development version.

    and if your is system is really bare like : docker.io/python,
    you will not even have man installed
    """
    manfile = hexy_lib_dir+os.sep+'extras'+os.sep+'Hexy.1.gz'
    mancmd = ["/usr/bin/man", manfile]
    try:
        return subprocess.call(mancmd)
    except Exception as e:
        print('cannot run man with hexy man page')
        print('you can always have a look at: '+manfile)

