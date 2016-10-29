set -x
echo "make a line increasing in size and changing directions"
sleep 2
time hexy -c showinfo 0 -c interval 0.4 -c clear 1 -c cycledirection 1 -c animate 1 line -x 10 -y 8 -j 6 -i 12 -c 'hello ' -s 6 -d ZYXzyx 

