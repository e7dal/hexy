# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

import os
import sys
import arrow
import click
import pprint
#from bubble import Bubble
from .util.bubble import Bubble

from . import metadata
from . import Hexy
from .util.profiling import start_profile, write_profile

# do not show if verbosity is above current verbose on Bubble(), todo USE magic
VERBOSE = 0
# do not show verbosities above the bar, todo USE magic
VERBOSE_BAR = 100


CONTEXT_SETTINGS = dict(auto_envvar_prefix='HEXY')


HEXY_CLI_GLOBALS={}
GLOBAL_START_ARROW = arrow.now()
HEXY_CLI_GLOBALS['start_arrow']=GLOBAL_START_ARROW


class HexyCli(Bubble):

    """Hexy, the Bubble for the Command Line Interface,

       this the bubble to be passed around as the 'ctx' for the cli commands"""

    def __init__(self,
                 home=None, verbose=VERBOSE,
                 verbose_bar=VERBOSE_BAR):
        Bubble.__init__(self, 'HexyCli', verbose, verbose_bar)
        self.GLOBALS = HEXY_CLI_GLOBALS
        self.debug = False

        self.adaptive_verbose = True

        if verbose:
            self.say('current hexy path:' + os.path.abspath(home),
                         verbosity=2)

        self.config = {}  # runtime config (dynamic via options)
        self.cfg = {}     # static config todo: yaml file

        self.set_verbose(verbose)
        self.set_verbose_bar(verbose_bar)

        self.debug = False
        if home:
            self.home = home
        else:
            self.home = os.getcwd()

        self.env = os.environ

    def set_config(self, key, value):
        self.config[key] = value
        self.say('set config[%s] = %s' % (key, value), verbosity=100)

    def get_config(self, key):
        if key in self.config:
            value=self.config[key]
            self.say(' get config[%s] = %s' % (key, value), verbosity=100)
            return value
        else:
            self.cry('get config[%s], key does not exist, returning None' % (key))
            return None

    def _say_color(self, msg, verbosity=0, stuff=None, fgc='green'):
        self._msg(msg=msg,
                  verb='cli._say_color',
                  verbosity=verbosity,
                  stuff=stuff,
                  from_cli=True)
        if verbosity <= self.get_verbose():
            click.secho(msg, fg=fgc)
            if stuff:
                click.echo('  stuff:')
                click.secho(pprint.pformat(stuff), fg=fgc)

    # shortcuts for stoplight colors
    def say_green(self, msg, verbosity=0, stuff=None):
        self._say_color(msg, verbosity, stuff, 'green')

    def say_yellow(self, msg, verbosity=0, stuff=None):
        self._say_color(msg, verbosity, stuff, 'yellow')

    def say_red(self, msg, verbosity=0, stuff=None):
        self._say_color(msg, verbosity, stuff, 'red')

    def __repr__(self):
        return '<HexyCli %s@%s since: %s>' % (self.name,
                                                self.home,
                                                self.birth)
    def __exit__(self, exit_type=None, value=None, traceback=None):
        self.say('exit',stuff=HEXY_CLI_GLOBALS,verbosity=111)
        if HEXY_CLI_GLOBALS['profiling']:
            write_profile()



pass_hexy = click.make_pass_decorator(HexyCli, ensure=True)

hexy_lib_dir = os.path.dirname(__file__)
commands_path = os.path.join(hexy_lib_dir, 'commands')
cmd_folder = os.path.abspath(commands_path)


class ComplexCLI(click.MultiCommand):

    def list_commands(self, ctx):
        # ctx.say('list_commands', verbosity=100)
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('hexy.commands.cmd_' + name,
                             None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI,
               context_settings=CONTEXT_SETTINGS)
@click.option('--config',
              '-c',
              nargs=2,
              multiple=True,
              metavar='KEY VALUE',
              help='overrides a config key/value pair.')
@click.option('--verbose',
              '-v',
              type=int,
              default=1,
              help='sets verbose, bigger is more detail')
@click.option('--barverbose',
              '-b',
              type=int,
              default=-1,
              help='sets a bar, only show messages up to the bar')
@click.option('--profile',
              '-p',
              envvar='HEXY_PROFILE',
              is_flag=True,
              default=False,
              help='run hexy with profiling.')
@click.version_option(metadata.version)
@click.pass_context
def cli(ctx, config, verbose, barverbose, profile):
    """ hexy, hexagonal ascii drawing """
    cis = ctx.invoked_subcommand

    HEXY_CLI_GLOBALS['profiling'] = profile
    if profile:
        start_profile()

    global VERBOSE
    VERBOSE = verbose

    global VERBOSE_BAR
    VERBOSE_BAR = barverbose

    HEXY_CLI_GLOBALS['full_command'] = ' '.join(sys.argv)

    hexy_home_abs = os.path.abspath(os.getcwd())
    ctx.obj = HexyCli(home=hexy_home_abs,
                      verbose=verbose,
                      verbose_bar=barverbose)

    for key, value in config:
        ctx.obj.set_config(key, value)

