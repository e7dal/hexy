# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

EXAMPLES=[]

def example(fun):
 global EXAMPLES
 EXAMPLES.append({'name':fun.__name__,'fun':fun})
 return fun

#(:. runnable examples for biotick testing  .:)
#todo heredocs working: http://www.tldp.org/LDP/abs/html/here-docs.html


EXAMPLE_TEMPLATE="""#name of example:{name}
#explanation (should be comments, starting with "#"
{explain}

# to try the example run:
# $ {full_cmd}

{full_cmd}  > example_cmd_{name}.out         #todo STDERR

#should show:
cat << "END_OF_EXAMPLE"  > expect_example_cmd_{name}.out
{expected_output}
END_OF_EXAMPLE

#check  and test example like:
# $ hexy examples -n {name}|bash

# todo check all: loop over all examples like above

#the hexy biot(basic input output test) is just a simple diff:
res=(diff expect_example_cmd_{name}.out  example_cmd_{name}.out)
ret=$?
if [ $ret -eq 0 ]; then
    echo "OK: {name}"
fi
if [ $ret -ne 0 ]; then
    echo $res
    echo "NO: {name}"
fi
#todo:red/green colors in check result
"""



@example
def example_cmd_start():
 """an example:starting"""
 name="start"
 explain="#starting the hexy cli tool"
 full_cmd="hexy"
 expected_output="""Usage: hexy [OPTIONS] COMMAND [ARGS]...

  hexy, hexagonal ascii drawing

Options:
  -c, --config KEY VALUE    overrides a config key/value pair.
  -v, --verbose INTEGER     sets verbose, bigger is more detail
  -b, --barverbose INTEGER  sets a bar, only show messages up to the bar
  -p, --profile             run hexy with profiling.
  --version                 Show the version and exit.
  --help                    Show this message and exit.

Commands:
  draw      Draw and show grid in hexy
  examples  Show example for doing some task in hexy
  grid      Show empty grid in hexy
  manual    Shows the man page packed inside the hexy tool
  read      Read ascii grid into an hexy grid
"""
 res=EXAMPLE_TEMPLATE.format(name=name,
                             explain=explain,
                             full_cmd=full_cmd,
                             expected_output=expected_output)
 return res


@example
def example_cmd_grid_default():
 """an example: hexy grid, with default values"""
 name="grid"
 explain="#hexy grid, with default values"
 full_cmd="hexy grid"
 expected_output=""":|1 2 3 4 5 6 7 |:
:|______________|:
:|. . . . . . . |:1
:| . . . . . . .|:2
:|. . . . . . . |:3
:| . . . . . . .|:4
:|______________|:
:| 1 2 3 4 5 6 7|:
"""
 res=EXAMPLE_TEMPLATE.format(name=name,
                             explain=explain,
                             full_cmd=full_cmd,
                             expected_output=expected_output)
 return res

def get_example_cmd_grid_default():
 """an example: hexy grid, with default values"""
 return  """# starting
$ hexy grid

should show:

:|1 2 3 4 5 6 7 |:
:|______________|:
:|. . . . . . . |:1
:| . . . . . . .|:2
:|. . . . . . . |:3
:| . . . . . . .|:4
:|______________|:
:| 1 2 3 4 5 6 7|:

"""

@example
def get_example_cmd_draw_default():
 """an example: hexy grid, with default values"""
 return  """# starting
$ hexy draw

should show:

:|1 2 3 4 5 6 7 8 9 0 |:
:|____________________|:
:|. . . . . . . . . . |:1
:| . . . . . . . . . .|:2
:|. . _ _ _ . . . . . |:3
:| . / . . \ . . . . .|:4
:|. / . . . \ . . . . |:5
:| .\. . . ./. . . . .|:6
:|. .\_ _ _/. . . . . |:7
:| . . . . . . . . . .|:8
:|. . . . . . . . . . |:9
:| . . . . . . . . . .|:10
:|____________________|:
:| 1 2 3 4 5 6 7 8 9 0|:

"""

@example
def get_example_cmd_read_default():
 """an example: hexy grid, with default values"""
 return  """# starting
$ hexy draw|hexy read

should show:

:|1 2 3 4 5 6 7 8 9 0 |:
:|____________________|:
:|. . . . . . . . . . |:1
:| . . . . . . . . . .|:2
:|. . _ _ _ . . . . . |:3
:| . / . . \ . . . . .|:4
:|. / . . . \ . . . . |:5
:| .\. . . ./. . . . .|:6
:|. .\_ _ _/. . . . . |:7
:| . . . . . . . . . .|:8
:|. . . . . . . . . . |:9
:| . . . . . . . . . .|:10
:|____________________|:
:| 1 2 3 4 5 6 7 8 9 0|:

"""
# vim: tabstop=1 expandtab shiftwidth=1 softtabstop=1
