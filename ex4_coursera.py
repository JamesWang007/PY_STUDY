# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 20:13:39 2018

@author: bejin
"""

import numpy as np

labels = np.array([1,2,3,0,2,1])

%timeit range(1000)

#%%timeit x = range(10000)
#max(x)