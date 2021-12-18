# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:16:48 2021

@author: kevmm
"""

import math

def check_fermat(a, b, n):
    num1 = a
    num2 = b
    num3 = n
    c2 = (math.pow(a, n)) + (math.pow(b, n))
    
    if num3 > 2:
        print("Holy smokes, Fermat was wrong!")
        return c2
    else:  
        2 > num3
        print("No, that doesn't work.")
        return c2
    
    
num1 = int(input("Enter number 1 here :"))
num2 = int(input("Enter number 2 here :"))
num3 = int(input("Enter number 3 here :"))
        
c2 = check_fermat(num1, num2, num3)
print(c2)
    