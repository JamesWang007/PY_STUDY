# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 20:00:20 2018

@author: bejin
"""

#create dict by list
#{x:x**2 for x in (2, 3, 4) }

for p in (1,0):
    print ("")
    for q in (1, 0):
        for r in (1, 0):
            if ((p&q)|(not q)|r):
                print ('T',end = " ")
            else:
                print ('F', end = " ")
                
            if (not q) | r:
                print ('T',end = " ")
            else:
                print ('F', end = " ")
                
            #if (((not p) | q)&(q & (not r)))|((not p) | r):
            if (not ((not p | q) & (not q |r))) | (not p | r ):
                print ('T')
            else:
                print ('F')
                



