#!/bin/bash

#4.piemērs
echo "Tiek pildīts skripts: "$0
#echo $0
#echo $n
echo "Skriptam nodoto argumentu skaits: "$#
echo "Skriptam nodoti argumenti (attēlošana/grupēšana 1): "$*
echo "Skriptam nodoti argumenti (attēlošana/grupēšana 2): "$@
#echo $?
echo "Skriptam piešķirtais procesa numrus: "$$
echo ""$!

#3.piemērs
#NAME="Modris Upenieks"
#echo $NAME
#unset NAME
#echo $NAME

#2.piemērs
#NAME="Modris Upenieks"
#readonly NAME
#echo $NAME
#NAME="Upenieks Modris"
#echo $NAME

#1.piemērs
#NAME="Modris Upenieks"
#echo $NAME
