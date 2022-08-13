# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 09:54:07 2020

@author: haymarsoe
"""

set1 = {'red','green','blue'}
set2 = {'cyan','green','blue','magenta','red'}

for resutl in set1.union(set2):
    print(resutl)
    
print()
for resutl in set1.intersection(set2):
    print(resutl)
    
print()
for resutl in set1.difference(set2):
    print(resutl)
    
print()
for resutl in set2.difference(set1):
    print(resutl)
    
print()
for resutl in set1.symmetric_difference(set2):
    print(resutl)