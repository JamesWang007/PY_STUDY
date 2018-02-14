#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:56:09 2018

@author: haiyangwang
"""

# - 1
def AND(p, q):
    return p and q;

def OR (p, q):
    return p or q;

def IF (p, q):
    return not p or q;
    
def NOT (p):
    return not p;
    
def IFF (p, q):
    return (not p or q) and (not q or p);

def evaluate(formula):
    if(formula[0] == 'AND'):
        return AND (formula[1], formula[2]);
    elif (formula[0] == 'OR'): 
        return OR(formula[1], formula[2]);
    elif (formula[0] == 'IF'): 
        return IF(formula[1], formula[2]);
    elif (formula[0] == 'NOT'): 
        return NOT(formula[1]);
    elif (formula[0] == 'IFF'): 
        return IFF(formula[1], formula[2]);
    else:
        return False;


# - 2
x = ['e', 's']
y = [1,2,3,4]

list_2d = [[(i,j) for j in y] for i in x]



# - 3
def merge(l1, l2):
    l1.extend(l2);
    l1.sort(key = lambda x: x, reverse = False);
    return (l1);




# - 4
def gcd(a, b):
    c = a % b;
    while c:
        a = b;
        b = c;
        c = a % b;
    return b;


##############################################################################
# testing 1
p = True;
q = False;
print ("(p or q):   ", evaluate (('OR', p, q)))
print ("(p and q):  ",evaluate (('AND', p, q)))
print ("(p -> q):   ",evaluate (('IF', p, q)))
print ("(p <-> q):  ",evaluate (('IFF', p, q)))
print("-p:         ",evaluate (('NOT', p)))
        
# testing 4
print('the greatest common divisor of 128 and 60 is ', gcd(128,60));

# unittest     
import unittest;
class TestFunctions(unittest.TestCase):
    
    # hard coding is fine
    def test_1(self):
        self.assertTrue(evaluate(('OR', True, False)));
        self.assertFalse(evaluate(('AND', True, False)));
        self.assertFalse(evaluate(('IF', True, False)));
        self.assertFalse(evaluate(('IFF', True, False)));
        self.assertFalse(evaluate(('NOT', True)));

    def test_2(self):
        self.assertTrue(list_2d == [[('e', 1), ('e', 2), ('e', 3), ('e', 4)], \
                      [('s', 1), ('s', 2), ('s', 3), ('s', 4)]] ) 
    
    def test_3(self):
        self.assertTrue(merge([1,2,3,4], [5,6,7,8]) == [1,2,3,4,5,6,7,8])
    
    def test_4(self):
        self.assertEqual(gcd(128, 60), 4); 
        self.assertEqual(gcd(60, 128), 4);
        self.assertEqual(gcd(3, 10), 1);
        self.assertEqual(gcd(6, 2), 2);
        self.assertEqual(gcd(5, 3), 1);
        self.assertEqual(gcd(256, 128), 128);

if __name__ == '__main__':
    unittest.main()
    
    