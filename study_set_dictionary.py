#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:42:00 2018

@author: haiyangwang
"""

2**5

str = 'Runoob'

print(str)
print(str[0:-1])
print(str[2:])
print(str*2)
print(str + "TEST")

print('Ru\noob')
print(r'Ru\noob')


#tuple
# - once defined, cannot change 
# - 

tup1 = ()
tup2 = (20,)

l1 = [1,2,3,'4',5]

tup3 = ([1,2,3,'4'], l1)
tup3[0][0] = 5
tup4 = tup2+tup3

#set
# - no duplicated items
# - single characters rather than one string
# - 


set1 = {1, 2}
set2 = set('3')

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

if('Rose' in student):
    print('Rose is a student')
else:
    print ('Rose is not a student')

a = set ('abracadabra')
b = set('alacazam')

print(a)
print(a - b)    #a - b
print(a | b)    #a OR b
print(a & b)    #a AND b
print(a ^ b)    #( a OR b ) - (a AND b)


#dictionary
# - no order
# - two elements: 'key': 'value'
# - key has to be unique
# - 

dict = {}
dict['one'] = "1 - toturial"
dict[2] = "2 - toolbox"

tinydict = {'name':'runoob', 'code':1, 'site':'www.ruoob.com'}

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

# - create dictionary type from a list
dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])

{x: x**2 for x in (2, 4, 6)}
# {1:4, 4:16, 6:36}

# - some functions for dictionary
# - e.g.: clear(), key(), values()


# return multiple 
def fun1(a, b):
    return (a+1, b+1)

fun1(3,4)


def fun2(*args):
    print(args)
    return args

print(type(fun2(1,2,3,4)))



#dictionary is using hashtable 
# - insertion costs about the same amount of time
d1 = {'one':1, 'two':2, 'three':3}


def fun3(d):
    for c in d:
        print (c,end=':') # only print the key not the value
        print(d1[c]) #print the value
        
        
fun3(d1)
        
    

# isinstance()
class father(object):
    pass

class son(father):
    pass

print (isinstance(son(), father))
print (type(son()) == father)


# define a dictionary using different ways
# - 1. tuple of list
dict_tl = dict(( ['one', 1], ['two', 2], ['three', 3] ))
print (dict_tl)

# - 2. set of tuple
dict_st = dict({ ('one', 1), ('two', 2), ('three', 3) })
print (dict_st)

# - 3. list of tuple
dict_lt = dict([ ('one', 1), ('two', 2), ('three', 3) ])
print(dict_lt)

# - 4. List of list
dict_ll = dict([ ['one', 1], ['two', 2], ['three', 3] ])
print (dict_ll)

# - 5. tuple of tuple
dict_tt = dict(( ('one', 1), ('two', 2), ('three', 3) ))
print (dict_tt)













