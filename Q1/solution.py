#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:33:58 2022

@author: sahab
"""

## Add code below with answer clearly stated
 
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
def sum_of_digit(n):
    return 0 if n == 0 else int(n % 10) + sum_of_digit(int(n / 10)) 

x = sum_of_digit(factorial(10))
assert x == 27

x = sum_of_digit(factorial(100))
assert x == 675
