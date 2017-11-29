Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print hello

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print hello
NameError: name 'hello' is not defined
>>> print "hello"
hello
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> print()
()
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> vars.__doc__
'vars([object]) -> dictionary\n\nWithout arguments, equivalent to locals().\nWith an argument, equivalent to object.__dict__.'
>>> print vars.__doc__
vars([object]) -> dictionary

Without arguments, equivalent to locals().
With an argument, equivalent to object.__dict__.
>>> print x.__doc__

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print x.__doc__
NameError: name 'x' is not defined
>>> x=5
>>> print x.__doc__
int(x=0) -> int or long
int(x, base=10) -> int or long

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is floating point, the conversion truncates towards zero.
If x is outside the integer range, the function returns a long instead.

If x is not a number or if base is given, then x must be a string or
Unicode object representing an integer literal in the given base.  The
literal can be preceded by '+' or '-' and be surrounded by whitespace.
The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
>>> from math import sin
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 5, '__name__': '__main__', 'sin': <built-in function sin>, '__doc__': None}
>>> sin(0.56)
0.5311861979208834
>>> sin(0.56)
0.5311861979208834
>>> snuss

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    snuss
NameError: name 'snuss' is not defined
>>> import math
>>> math.cos(0.56)
0.8472551110134161
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 5, '__name__': '__main__', 'sin': <built-in function sin>, '__doc__': None, 'math': <module 'math' (built-in)>}
>>> import math as abc
>>> vars()
{'abc': <module 'math' (built-in)>, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 5, '__name__': '__main__', 'sin': <built-in function sin>, '__doc__': None, 'math': <module 'math' (built-in)>}
>>> import *
SyntaxError: invalid syntax
>>> import math import *
SyntaxError: invalid syntax
>>> 
