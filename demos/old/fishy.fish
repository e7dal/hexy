for i in (seq 1 3 80)
 hexy draw -x 24 -y 6 -i $i -j 1 -s 3
 sleep 0.2
 clear
end

for i in (seq 3 100)
 set m (echo "$i/3"|bc|sed 's/\..*//')
 set s (echo "$i*1.2"|bc|sed 's/\..*//')
 time hexy draw -x $i -y $i -i$m -j$m -s $s
 echo $i $m $s;sleep 0.2
end
