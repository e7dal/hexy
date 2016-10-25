set -x
clear
echo 'hexy draw hexagon with increasing size, with clear betweeen frames'
sleep 1 
hexy draw -s 27 -x 42 -y 24 -a -c
echo 'hexy draw hexagon with increasing size with no clear...'
sleep 1
hexy draw -s 27 -x 42 -y 24 -a
