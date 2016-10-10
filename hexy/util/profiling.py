# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.
import arrow
try:
    from cProfile import Profile
except ImportError:
    from profile import Profile
from pstats import Stats
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

HEXY_PROFILE=False

def start_profile(*argv):
    # https://docs.python.org/3.4/library/profile.html#module-cProfile
    print('HEXY_PROFILE:start_profile')
    global HEXY_PROFILE
    HEXY_PROFILE = Profile()
    HEXY_PROFILE.enable()

def write_profile(pfile='./hexy_profile.out'):
    global HEXY_PROFILE
    if not HEXY_PROFILE:
        return
    HEXY_PROFILE.disable()
    #s = io.StringIO()
    s = StringIO()
    sortby = 'cumulative'
    ps = Stats(HEXY_PROFILE,stream=s).sort_stats(sortby)
    ps.print_stats()
    pstats_file='./hexy_profiling.pstats'
    profile_text='./hexy_profile.txt'

    HEXY_PROFILE.dump_stats(pstats_file)

    with open(profile_text,'a+') as pf:
        pf.write(s.getvalue())
    print("end_profile")
    print('HEXY_PROFILE:pstats_file:'+pstats_file)
    print('HEXY_PROFILE:profile_text:'+profile_text)
    print('HEXY_PROFILE:todo, show example for viewing, interacting with the profile files')

if __name__=='__main__':
    start_profile()
    def ok():pass
    ok()
    write_profile()

