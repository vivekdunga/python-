# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 23:33:20 2025

@author: lenovo
"""

year=int(input())
leap=False
if year%100==0 and year%400!=0:
    leap=False
elif year%4==0:
    leap=True
else:
    leap=False
print(leap)