# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 23:18:05 2025

@author: lenovo
"""

a=input()
x,y,z=a.split(",")
num1=int(x)
num2=int(y)
num3=int(z)
if num1>num2 and num1>num3:
    print("largest number is:",num1)
elif num2>num1 and num2>num3:
    print("largest number is:",num2)
else:
    print("largest number is:",num3)