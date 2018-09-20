# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 13:05:04 2018

@author: bejin
"""

import numpy as np


#(a)
def fun_a(v, u, w):
    temp1 = np.dot(v, u)
    print("temp1 : v * u = " + str(temp1))
    res = np.inner(temp1, w)
    print("res = " + str(res))
    return res



#(b)
def fun_b(v, u, w):
    temp1 = np.subtract(v, w)
    print ("temp1 : v - u = " + str(temp1))
    res = np.dot(temp1, u)
    print("res = " + str(res))
    
    return res



#(c)
def fun_c(v, u):
    res = np.cross(u, np.array([0,0,c]))
    print("res = " + str(res))
    
    return res



#(d)
def fun_d(v, u, w):
    temp1 = np.cross(u, w)
    print("temp1 : " + str(temp1))
    res = np.cross(temp1, np.array([0,0,00]))
    return res



# Pepper
v = np.array([4, 2, -1])
u = np.array([0, 4, 6])
w = np.array([2, -1, 2])
c = -10


fun_a(v, u, w)
fun_b(v, u, w)
fun_c(v, u)
fun_d(v, u, w)

# Sugar
v = np.array([0, 1, -2])
u = np.array([0, 2, -6])
w = np.array([8, -4, -2])
c = 10


fun_a(v, u, w)
fun_b(v, u, w)
fun_c(v, u)
fun_d(v, u, w)

# Saffron
v = np.array([3, -4, 2])
u = np.array([0, 7, -2])
w = np.array([1, 2, 3])
c = 20


fun_a(v, u, w)
fun_b(v, u, w)
fun_c(v, u)
fun_d(v, u, w)

