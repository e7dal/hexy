# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import click

from ..cli import pass_hexy
from ..util.examples import EXAMPLES as examples

@click.command('examples',
               short_help='Show example for doing some task in hexy')
@click.option('--name',
              '-n',
              default=None,
              help='show the example with the name')
@click.option('--all',
              '-a',
              is_flag=True,
              default=False,
              help='show all the examples')
@pass_hexy
def cli(ctx, name,all):
    """Show example for doing some task in hexy"""
    ctx.gbc.say('examples',stuff=examples, verbosity=1000)

    for example in examples:
        if all or (name and example['name'] == name):
            if all:
                ctx.gbc.say('example',stuff=example, verbosity=100)
                name = example['name']
            #click.echo_via_pager(example['fun']())
            click.echo("#"*80)
            click.echo("### start of hexy example: "+name)
            click.echo("#"*80)
            click.echo(example['fun']())
            click.echo("#"*80)
            click.echo("### end of hexy example: "+name)
            click.echo("#"*80)
            click.echo()

        else:
            click.echo("available example: " + example['name'])


