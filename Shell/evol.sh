#!/bin/bash


total=0

for i in {1..10}
do
	eval x$i=$i
	total=$((total + $x$i))
done

echo $x1 $x2 $x3 $x4 $x5 $x6 $x7 $x8 $x9 $x10

echo Total is: $total
