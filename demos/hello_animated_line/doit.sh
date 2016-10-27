set -x
echo "make a line increasing in size and changing directions"
sleep 2
time hexy -c interval 0.4 -c clear 1 -c cycledirection 1 -c animate 1 line -x 16 -y 16 -j8 -i 16 -c ".hello! " -s 42 -d ZYXzyx
