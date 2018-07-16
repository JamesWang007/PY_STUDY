# -*- coding: utf-8 -*-

import numpy as np
import math

def f1(n): # return  1 1 2 3 5 8 ... 
    if n == 1 or n == 0 :
        return 1
    a, b = 1, 1
    while n > 1:
         a, b = b, a+b
         n -= 1
         
    return b

for i in np.arange(10):
    print(f1(i))

def f2(n):      # use yield = push_back(...)
    if n == 1 or n == 0 :
        yield 1
        return 

    a, b = 0, 1
    while n > 1:
        yield b
        a, b = b, a + b
        n -= 1
    yield b

for i in f2(1):
    print(i)
    
def f3(n):
    res = ((1/math.sqrt(5))*((1+math.sqrt(5))/2)**(n+1)) - \
            ((1/math.sqrt(5))* ((1-math.sqrt(5))/2)**(n+1)) 
    return int(round(res))
            

for i in np.arange(10):
    print(f3(i))
    
























































































































































    
    