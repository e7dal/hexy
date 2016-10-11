# -*- coding: utf-8 -*-
# Part of bubble. See LICENSE file for full copyright and licensing details.
# lazy as i am, just a bare copy for now
import os
import sys
import time
import arrow
from pprint import pprint


class Bubble(object):

    """ puts a tiny bubble of reality into existence """
    name = None

    birth = None
    home = None

    _bubble_lib_dir = None

    debug = False

    _verbose = 0
    _verbose_bar = 0

    _adaptive_verbose = True
    _msg_stats = {}
    _total_verbose = 0
    _total_verbose_bar = 0
    _total_verbose_self = 0

    def __init__(self,
                 name='NoName',
                 verbose=0,
                 verbose_bar=1,
                 logfile='',
                 statistics=False):
        self.say('base.Bubble:name=' + str(name) + ', verbose=' + str(verbose))
        self.name = name

        self.birth = arrow.now()
        self._verbose = verbose
        self._verbose_bar = verbose_bar


        self._adaptive_verbose = True
        self._msg_stats['___init_verbose'] = verbose
        self._bubble_lib_dir = os.path.dirname(__file__)

        self.say(self.name + ':here!', verbosity=101)
        self.say(self.name + ':config',
                 stuff={'verbose': self._verbose,
                        'verbose_bar': self._verbose_bar,
                        'bubble_lib_dir': self._bubble_lib_dir,
                        },
                 verbosity=101)

    def __enter__(self):
        if not self.debug:
            return

        print('entering:Bubble.name:' + str(self.name))
        print('entering:Bubble.birth:' + str(self.birth))


    def __exit__(self, exit_type=None, value=None, traceback=None):
        if not self.debug:
            return
        print('exiting:Bubble.name:' + str(self.name))
        print('exiting:Bubble.birth:' + str(self.birth))

        if exit_type:
            print('exiting:Bubble:type:' + str(exit_type))

        if value:
            print('exiting:Bubble:value:' + str(value))
        if traceback:
            print('exiting:Bubble:traceback' + str(traceback))
        if self._parent:
            pass
            # print('p:' + self._parent)
            # print('p:' + self._parent.name)

    def __del__(self):
        if self.debug:pprint(self._msg_stats)
        return self.__exit__()

    def _update_stat(self, stat_key):
        if stat_key not in self._msg_stats:
            self._msg_stats[stat_key] = 1
        else:
            self._msg_stats[stat_key] += 1

    def set_verbose(self, verbose=0):
        self._update_stat('___set_verbose')
        self._verbose = int(verbose)

    def get_verbose(self):
        return self._verbose

    def set_verbose_bar(self, verbose_bar=0):
        self._update_stat('___set_verbose_bar')
        self._verbose_bar = int(verbose_bar)

    def get_verbose_bar(self):
        return self._verbose_bar

    #: TODO: adaptive bar raising lowering, do we want/need this?
    def verbose_plus(self, amount=1):
        self._update_stat('___verbose_plus')
        if self._adaptive_verbose:
            verbose = self.get_verbose()
            self.set_verbose(verbose + amount)

    def verbose_minus(self, amount=1):
        #: TODO: never drop below 1, move to a magic value
        if self.debug: print('minus',amount,self.get_verbose())
        self._update_stat('___verbose_minus')
        if self._adaptive_verbose and self.get_verbose() > 1:
            verbose = self.get_verbose()
            if verbose > amount:
                self.set_verbose(verbose - amount)
            else:
                self.set_verbose(1)
        else:
            if self.debug:print('minus below',amount)
            self._update_stat('___verbose_minus_already_below_one')

    def _msg(self, msg='Msg',
             stuff=None,
             verb='SAY',
             verbosity=1,
             child_level=0,
             child_name='',
             from_cli=False):
        self._total_verbose += verbosity
        self._update_stat('___verb_' + verb)

        self._total_verbose_self += verbosity

        if verbosity > self.get_verbose() or \
           verbosity > self.get_verbose_bar():
            if self.debug:
                print("_msg: below verbose or verbose_bar,no show")
            return
        else:
            if self.debug:
                print("_msg: NOT below verbose or verbose_bar,continue")

        ignore_line = ['_msg','_say_color',
                       'say','say_green','say_yellow','say_yellow']
        f=sys._getframe(2)
        ff=f
        i=0
        while ff.f_back:
            i+=1
            c=ff.f_code
            if c.co_name not in ignore_line:
                break
            ff=ff.f_back
        # print('keeping:',i,c.co_filename,c.co_firstlineno,c.co_name)
        file_line = c.co_filename+':'+str(c.co_firstlineno)

        #tl_item = {'attime': arrow.now()-BUBBLE_START_ARROW,
        tl_item = {'attime': time.clock(),
                   'name': self.name,
                   'msg': msg,
                   'stuff': stuff,
                   'verb': verb,
                   'verbosity': verbosity,
                   'child_level': child_level,
                   'child_name': child_name,
                   'from': file_line,
                   'curr_verbose': self.get_verbose(),
                   'curr_verbose_bar':self.get_verbose_bar()
                   }
        #if not from_cli:
        #blog.info(**tl_item)
        pprint(tl_item)


    #def tl_from_child(self, exported_timeline=[]):
    #    for tli in exported_timeline:
    #        tli['name'] = self.name + ':parent of:' + tli['name']
    #        self._timeline.append(tli)

    def cry(self, msg='Crying', stuff=None, verbosity=1):
        self.verbose_plus(verbosity)
        self._msg(msg=msg, stuff=stuff, verb='CRY', verbosity=verbosity)

    def mumble(self, msg='Mumbling', stuff=None, verbosity=1):
        self.verbose_minus(verbosity)
        self._msg(msg=msg, stuff=stuff, verb='MUMBLE', verbosity=verbosity)

    def say(self, msg='Saying', stuff=None, verbosity=1):
        self._msg(msg=msg, stuff=stuff, verb='SAY', verbosity=verbosity)
        self.verbose_minus(verbosity)


    def get_total_verbose(self):
        return self._total_verbose

    def get_total_verbose_bar(self):
        return self._total_verbose_bar
