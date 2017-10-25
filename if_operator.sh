#!/bin/bash

#if (()) ... fi
a=$1
b=$2
c=$3
if (( $a > 0 )); then
   echo 'Galvenais zars (ja apakszars) -> tad, kad $a ir >0'
elif  (( $a == 0 )); then
   echo 'Alternativs zars (tikai ja gadijuma) -> tad, kad $a ir >1'
else
   echo 'Galvenais zars (ne apakszars) -> tad, kad $a nav >0'
fi
