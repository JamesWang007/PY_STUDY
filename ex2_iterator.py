# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:50:31 2018

@author: bejin
"""

# iterator
# iter(), next()

list = [1,2,3,4]
it = iter(list)     # create an iterator object
print (next(it))    # output the next element of iterator
print(next(it))


it = iter(list)
for x in it:
    print(x, end = ' ')

    
it = iter(list)
import sys
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()

# yield 
# 这里的迭代器可以用生成l列表来理解
import sys
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f is a iterator, created by a creator

while True:
    try:
        print (next(f), end = ' ')
    except StopIteration:
        sys.exit()

















