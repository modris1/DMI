#!/bin/bash

array=("$@")
#echo ${array[0]}
n=$# #savaditie argumenti
k=0

while (( $k < $n ))
do
	echo ${array[k]}
	k=`expr $k + 1`
done

if(( $array[0] > $array[1] )); then
if(( $array[0] > $array[2] )); then
if(( $array[1] > $array[2] )); then
echo ${array[2]} ${array[1]} ${array[0]}
else
echo ${array[1]} ${array[2]} ${array[0]}
