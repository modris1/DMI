#!/usr/bin/python
# -*- coding: utf-8 -*-

#a=10
#echo $a
#echo "MAinīgā a vērtība ir: $a"

a=65
print type(a)
print ("Mainīgā a vērtība kā decimāls skaitlis: %d"%(a))
print "Mainīgā a vērtība kā heksadecimāls skaitlis: %x" %a
print "Mainīgā a vērtība kā oktāls skaitlis: %o" %a
print "Mainīgā a vērtība simbols: %c" %a

a='A'
print type(a)
print ("Mainīgā a vērtība kā decimāls skaitlis: %d"%(ord(a)))
print "Mainīgā a vērtība kā heksadecimāls skaitlis: %x" %(ord(a))
print "Mainīgā a vērtība kā oktāls skaitlis: %o" %(ord(a))
print "Mainīgā a vērtība simbols: %c" %(ord(a))

a=6.5
print type(a)
print ("Mainīgā a vērtība kā decimāls skaitlis: %d"%(a))
print "Mainīgā a vērtība kā heksadecimāls skaitlis: %x" %a
print "Mainīgā a vērtība kā oktāls skaitlis: %o" %a
#print "Mainīgā a vērtība simbols: %c" %(ord(a))
print "Mainīgā a vērtība kā reāls skaitlis: %7.3f" %a
