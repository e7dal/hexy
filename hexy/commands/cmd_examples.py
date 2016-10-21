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
@click.option('--showcmd',
              '-c',
              is_flag=True,
              default=False,
              help='show the command to run and check the example with the name')
@click.option('--all',
              '-a',
              is_flag=True,
              default=False,
              help='show all the examples')
@pass_hexy
def cli(ctx, showcmd,name,all):
    """Show example for doing some task in hexy"""
    ctx.say('examples',stuff=examples, verbosity=1000)

    for example in examples:
        if all or (name and example['name'] == name):
            if all:
                ctx.say('example',stuff=example, verbosity=100)
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
        if not all and not name:
            if showcmd:
                click.echo("#####  to show full the example for "+example['name']+" just run:")
                click.echo("####   hexy examples --name " + example['name'])
                click.echo("###    to run the example as a test, pipe it to a shell:")
                click.echo("##     hexy examples --name " + example['name'] +"|sh")
                click.echo("#")
            else:
                click.echo("available example: " + example['name'])
    if name and showcmd:
        click.echo("#####  to show full the example for "+name+" just run:")
        click.echo("####   hexy examples --name " + name)
        click.echo("###    to run the example as a test, pipe it to a shell:")
        click.echo("##     hexy examples --name " + name +"|sh")
        click.echo("#")
    if not all:
        click.echo("###    to run all the example as tests, pipe it to a shell:")
        click.echo("##     hexy examples --all|sh")
        click.echo("#")


