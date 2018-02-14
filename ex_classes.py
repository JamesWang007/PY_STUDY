# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 00:11:21 2018

@author: bejin
"""
class MyClass:
    i = 12345
    
    def f(self):
        return 'Hello World'
    
    def __init__(self):
        self.data = []
    
    
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
x = Complex(3.0, -4.5)
print (x.r, x.i)


class Test:
    def prt(self):
        print (self)
        print (self.__class__)
        
t = Test()
t.prt()



#private members use __ as prefix
class JustCounter:
    __secretCount = 0
    publicCount = 0
    
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
        print (self.__le__(self.__secretCount))
        
counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secretCount)
    
    
class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return '这个人的名字是%s,已经有%d岁了！'%(self.name,self.age)

a=people('孙悟空',999)
print(a)

















