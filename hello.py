# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:06:08 2018

@author: bejin
"""

print ("Hello, Python!");


def run(cb):
    cb()
    print('run\n')
    


run(lambda : print('this is lambda\n'))

add = lambda a, b: a+b

print(add(1,3))

a = [(1,2), (4, 1), (9, 10), (13,-3)]

a.sort(key=lambda x:x[1])

print(a)

list1 = [1,4,9]
list2 = [2,3,5]

