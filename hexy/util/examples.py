# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

EXAMPLES=[]
def example(fun):
 global EXAMPLES
 EXAMPLES.append({'name':fun.__name__,'fun':fun})
 return fun

@example
def get_example_cmd_start():
 """an example:stsrting"""
 return  """# starting
$ hexy
"""

# vim: tabstop=1 expandtab shiftwidth=1 softtabstop=1
