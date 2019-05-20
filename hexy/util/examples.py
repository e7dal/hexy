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
    diff -W 160 -yd ./hexamples/example_cmd_{name}_expect.out  ./hexamples/example_cmd_{name}_result.out
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
  circle    Put a fuzzy circle on an hexy  grid
  cslice    Select a slice out of the cycled grid (cilinder), in given
            direction
  cursor    Add a cursor on point
  draw      Draw and show grid in hexy
  examples  Show example for doing some task in hexy
  grid      Show empty grid in hexy
  line      Put a single line with direction(xyz) and size in hexy
  manual    Shows the man page packed inside the hexy tool
  point     Put a single point on a grid and show grid in hexy tool
  read      Read ascii grid into an hexy grid
  rotate    Rotate a given amount of 90 degree turn"""

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
def example_cmd_line():
 """an example: hexy line"""
 name="line"
 explain="#hexy line"
 full_cmd="hexy line -x 20 -y 20 -i 10 -j 10 -s 11 -c 'hello world' -d X"
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
:| . . . . . h e l l o   w o r l d . . . .|:10
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


@example
def example_cmd_cslice_select_H_and_V():
 """an example: hexy cslice, with from to to, for a piped in drawing, first Horizontal and then Vertical"""
 name="cslice"
 explain="#hexy slicing in horizontal an vertical directions"
 full_cmd="hexy draw|hexy cslice -f 2 -t 12 -d H|hexy cslice -f 2 -t 7 -d V" 
 expected_output=""":|1 2 3 4 5 |:
:|__________|:
:|. _ _ _ . |:1
:| / . . \ .|:2
:|/ . . . \ |:3
:|\. . . ./.|:4
:|.\_ _ _/. |:5
:|__________|:
:|1 2 3 4 5 |::
"""
 res=EXAMPLE_TEMPLATE.format(name=name,
                             explain=explain,
                             full_cmd=full_cmd,
                             expected_output=expected_output)
 return res

@example
def example_cmd_circle():
 """an example: hexy circle, with radius form r to R  to, seems to be flattened in H direction :("""
 name="circle"
 explain="#hexy circle, kind of, still WIP"
 full_cmd="hexy circle -x 30 -y 30 -i 30 -j 15 -r 10 -R 14 -c o"
 expected_output=""":|1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 |:
:|____________________________________________________________|:
:|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |:1
:| . . . . . . . ooooooooooooooooooooooooooooo . . . . . . . .|:2
:|. . . . . . .ooooooooooooooooooooooooooooooooo. . . . . . . |:3
:| . . . . ooooooooooooooooooooooooooooooooooooooooo . . . . .|:4
:|. . . .oooooooooooooo . . . . . . . . oooooooooooooo. . . . |:5
:| . . . oooooooooo. . . . . . . . . . . . .oooooooooo . . . .|:6
:|. . .oooooooooo . . . . . . . . . . . . . . oooooooooo. . . |:7
:| . oooooooooo. . . . . . . . . . . . . . . . .oooooooooo . .|:8
:|. .oooooooo . . . . . . . . . . . . . . . . . . oooooooo. . |:9
:| .ooooooooo. . . . . . . . . . . . . . . . . . .ooooooooo. .|:10
:|. ooooooo . . . . . . . . . . . . . . . . . . . . ooooooo . |:11
:| .ooooooo. . . . . . . . . . . . . . . . . . . . .ooooooo. .|:12
:|. ooooooo . . . . . . . . . . . . . . . . . . . . ooooooo . |:13
:| .ooooooo. . . . . . . . . . . . . . . . . . . . .ooooooo. .|:14
:|. ooooooo . . . . . . . . . . . . . . . . . . . . ooooooo . |:15
:| .ooooooo. . . . . . . . . . . . . . . . . . . . .ooooooo. .|:16
:|. ooooooo . . . . . . . . . . . . . . . . . . . . ooooooo . |:17
:| .ooooooo. . . . . . . . . . . . . . . . . . . . .ooooooo. .|:18
:|. ooooooo . . . . . . . . . . . . . . . . . . . . ooooooo . |:19
:| .ooooooooo. . . . . . . . . . . . . . . . . . .ooooooooo. .|:20
:|. .oooooooo . . . . . . . . . . . . . . . . . . oooooooo. . |:21
:| . oooooooooo. . . . . . . . . . . . . . . . .oooooooooo . .|:22
:|. . .oooooooooo . . . . . . . . . . . . . . oooooooooo. . . |:23
:| . . . oooooooooo. . . . . . . . . . . . .oooooooooo . . . .|:24
:|. . . .oooooooooooooo . . . . . . . . oooooooooooooo. . . . |:25
:| . . . . ooooooooooooooooooooooooooooooooooooooooo . . . . .|:26
:|. . . . . . .ooooooooooooooooooooooooooooooooo. . . . . . . |:27
:| . . . . . . . ooooooooooooooooooooooooooooo . . . . . . . .|:28
:|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |:29
:| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|:30
:|____________________________________________________________|:
:| 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0|:
"""
 res=EXAMPLE_TEMPLATE.format(name=name,
                             explain=explain,
                             full_cmd=full_cmd,
                             expected_output=expected_output)
 return res

@example
def example_cmd_line_animated_with_config():
 """an example: hexy line animated, with config arguments to main cli"""
 name="line_animated_with_config"
 explain="#hexy line, with animation for size and direction, clear and sleep will not be compared"
 full_cmd="hexy -c showinfo 0 -c interval 0.4 -c clear 1 -c cycledirection 1 -c animate 1 line -x 10 -y 8 -j 6 -i 12 -c 'hello ' -s 6 -d ZYXzyx"
 expected_output=""":|1 2 3 4 5 6 7 8 9 0 |:
:|____________________|:
:|. . . . . . . . . . |:1
:| . . . . . . . . . .|:2
:|. . . . . . . . . . |:3
:| . . . . . . . . . .|:4
:|. . . . . . . . . . |:5
:| . . . . . . . . . .|:6
:|. . . . . h . . . . |:7
:| . . . . . . . . . .|:8
:|____________________|:
:| 1 2 3 4 5 6 7 8 9 0|:

:|1 2 3 4 5 6 7 8 9 0 |:
:|____________________|:
:|. . . . . . . . . . |:1
:| . . . . . . . . . .|:2
:|. . . . . . . . . . |:3
:| . . . . . . . . . .|:4
:|. . . . . . . . . . |:5
:| . . . . . . . . . .|:6
:|. . . . . . h . . . |:7
:| . . . . . . e . . .|:8
:|____________________|:
:| 1 2 3 4 5 6 7 8 9 0|:

:|1 2 3 4 5 6 7 8 9 0 |:
:|____________________|:
:|. . . . . . . . . . |:1
:| . . . . . . . . . .|:2
:|. . . . . . . . . . |:3
:| . . . . . . . . . .|:4
:|. . . . . . . . . . |:5
:| . . . . . . h e l .|:6
:|. . . . . . . . . . |:7
:| . . . . . . . . . .|:8
:|____________________|:
:| 1 2 3 4 5 6 7 8 9 0|:

:|1 2 3 4 5 6 7 8 9 0 |:
:|____________________|:
:|. . . . . . . . . . |:1
:| . . . . . . . l . .|:2
:|. . . . . . . l . . |:3
:| . . . . . . e . . .|:4
:|. . . . . . h . . . |:5
:| . . . . . . . . . .|:6
:|. . . . . . . . . . |:7
:| . . . . . . . . . .|:8
:|____________________|:
:| 1 2 3 4 5 6 7 8 9 0|:

:|1 2 3 4 5 6 7 8 9 0 |:
:|____________________|:
:|. . . o . . . . . . |:1
:| . . . l . . . . . .|:2
:|. . . . l . . . . . |:3
:| . . . . e . . . . .|:4
:|. . . . . h . . . . |:5
:| . . . . . . . . . .|:6
:|. . . . . . . . . . |:7
:| . . . . . . . . . .|:8
:|____________________|:
:| 1 2 3 4 5 6 7 8 9 0|:

:|1 2 3 4 5 6 7 8 9 0 |:
:|____________________|:
:|. . . . . . . . . . |:1
:| . . . . . . . . . .|:2
:|. . . . . . . . . . |:3
:| . . . . . . . . . .|:4
:|. . . . . . . . . . |:5
:| o l l e h . . . .  |:6
:|. . . . . . . . . . |:7
:| . . . . . . . . . .|:8
:|____________________|:
:| 1 2 3 4 5 6 7 8 9 0|:
"""
 res=EXAMPLE_TEMPLATE.format(name=name,
                             explain=explain,
                             full_cmd=full_cmd,
                             expected_output=expected_output)
 return res
# vim: tabstop=1 expandtab shiftwidth=1 softtabstop=1
