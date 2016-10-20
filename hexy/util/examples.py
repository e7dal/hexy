# -*- coding: utf-8 -*-
# Part of hexy. See LICENSE file for full copyright and licensing details.

#biotick: basic input output test via examples
#you should have great expectations
#(:. runnable examples for biotick testing  .:)
#todo heredocs working: http://www.tldp.org/LDP/abs/html/here-docs.html


EXAMPLES=[]

def example(fun):
 global EXAMPLES
 EXAMPLES.append({'name':fun.__name__,'fun':fun})
 return fun

EXAMPLE_TEMPLATE="""#name of example:{name}
#explanation (should be comments, starting with "#"
{explain}

#first create an examples directory
if [ ! -d ./hexamples ];then
 mkdir ./hexamples
 echo "created ./hexamples for temporary example files"
#else: 
# echo "using ./hexamples for temporary example files"
fi


# to try the example run:
# $ {full_cmd}

{full_cmd}  > ./hexamples/example_cmd_{name}_result.out         #todo STDERR

#should show:
cat << "END_OF_EXAMPLE"  > ./hexamples/example_cmd_{name}_expect.out
{expected_output}
END_OF_EXAMPLE

#check  and test example like:
# $ hexy examples -n {name}|bash

# todo check all: loop over all examples like above

#the hexy biot(basic input output test) is just a simple diff:
res=$(diff ./hexamples/example_cmd_{name}_expect.out  ./hexamples/example_cmd_{name}_result.out)
ret=$?
if [ $ret -eq 0 ]; then
    echo "OK: {name}"
fi
if [ $ret -ne 0 ]; then
    echo $res
    echo "NO: {name}"
    hexy --version
    python --version
    echo side by side diff
    #todo: meld, diff commandd
    diff -y ./hexamples/example_cmd_{name}_expect.out  ./hexamples/example_cmd_{name}_result.out
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
  cursor    Add a cursor on point
  draw      Draw and show grid in hexy
  examples  Show example for doing some task in hexy
  grid      Show empty grid in hexy
  manual    Shows the man page packed inside the hexy tool
  point     Put a single point on a grid and show grid in hexy tool
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

@example
def example_cmd_point():
 """an example: hexy point"""
 name="point"
 explain="#hexy point"
 #full_cmd="hexy point -i 5 -j 5 -x 10 -y 10 -c e"
 full_cmd="hexy point -x 20 -y 20 -i 10 -j 10 -c erdal"
 expected_output=""":|1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 |:
:|________________________________________|:
:|. . . . . . . . . . . . . . . . . . . . |:1
:| . . . . . . . . . . . . . . . . . . . .|:2
:|. . . . . . . . . . . . . . . . . . . . |:3
:| . . . . . . . . . . . . . . . . . . . .|:4
:|. . . . . . . . . . . . . . . . . . . . |:5
:| . . . . . . . . . . . . . . . . . . . .|:6
:|. . . . . . . . . . . . . . . . . . . . |:7
:| . . . . . . . . . . . . . . . . . . . .|:8
:|. . . . . . . . . . . . . . . . . . . . |:9
:| . . . . e . . . . . . . . . . . . . . .|:10
:|. . . . . . . . . . . . . . . . . . . . |:11
:| . . . . . . . . . . . . . . . . . . . .|:12
:|. . . . . . . . . . . . . . . . . . . . |:13
:| . . . . . . . . . . . . . . . . . . . .|:14
:|. . . . . . . . . . . . . . . . . . . . |:15
:| . . . . . . . . . . . . . . . . . . . .|:16
:|. . . . . . . . . . . . . . . . . . . . |:17
:| . . . . . . . . . . . . . . . . . . . .|:18
:|. . . . . . . . . . . . . . . . . . . . |:19
:| . . . . . . . . . . . . . . . . . . . .|:20
:|________________________________________|:
:| 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0|:
"""
 res=EXAMPLE_TEMPLATE.format(name=name,
                             explain=explain,
                             full_cmd=full_cmd,
                             expected_output=expected_output)
 return res
@example
def example_cmd_draw_default():
 """an example: hexy draw, with default values"""
 name="draw"
 explain="#hexy draw, with default values"
 full_cmd="hexy draw"
 expected_output=""":|1 2 3 4 5 6 7 8 9 0 |:
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
 res=EXAMPLE_TEMPLATE.format(name=name,
                             explain=explain,
                             full_cmd=full_cmd,
                             expected_output=expected_output)
 return res

@example
def example_cmd_read_default():
 """an example: hexy read, with default values"""
 name="read"
 explain="#hexy read, with default values"
 full_cmd="hexy draw|hexy read"
 expected_output=""":|1 2 3 4 5 6 7 8 9 0 |:
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
 res=EXAMPLE_TEMPLATE.format(name=name,
                             explain=explain,
                             full_cmd=full_cmd,
                             expected_output=expected_output)
 return res

@example
def example_cmd_cursor_default():
 """an example: hexy cursor, with default values"""
 name="cursor"
 explain="#hexy cursor, with default values"
 full_cmd="hexy cursor"
 expected_output=""":|1 2 3 4 5 6 7 8 9 0 |:
:|____________________|:
:|. . . . . . . . . . |:1
:| .|. . . . . . . . .|:2
:|._._. . . . . . . . |:3
:| .|. . . . . . . . .|:4
:|. . . . . . . . . . |:5
:| . . . . . . . . . .|:6
:|. . . . . . . . . . |:7
:| . . . . . . . . . .|:8
:|. . . . . . . . . . |:9
:| . . . . . . . . . .|:10
:|____________________|:
:| 1 2 3 4 5 6 7 8 9 0|:

"""
 res=EXAMPLE_TEMPLATE.format(name=name,
                             explain=explain,
                             full_cmd=full_cmd,
                             expected_output=expected_output)
 return res

# vim: tabstop=1 expandtab shiftwidth=1 softtabstop=1
