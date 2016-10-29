set -x
echo "make a line increasing in size and changing directions"
sleep 2
hexy draw|hexy cslice -f 2 -t 12 -d H|hexy cslice -f 2 -t 7 -d V
