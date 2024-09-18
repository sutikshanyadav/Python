# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 08:06:34 2024

@author: ADMIN
"""

a = 'sutikshan yadav'

#increasing pattern
for i in range(1, len(a) + 1):
    print(a[:i])

#decreasing pattern
for i in range(len(a) - 1, 0, -1):
    print(a[:i])