# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:00:45 2018

@author: bejin
"""

import sys
print ('===============Python import mode==================')
print ('console parameters: ')
for i in sys.argv:
    print (i)
print ('\n python path is ', sys.path)
       

a, b, c, d = 20, 5.5, True, 4+3j
print (type(a), type(b), type(c), type(d))


isinstance(a, int)
type(a) == int


class A:
    pass

class B(A):
    pass

isinstance(A(), A) #True

type(A()) == A #True

isinstance(B(), A) #True

type(B()) == A #False







