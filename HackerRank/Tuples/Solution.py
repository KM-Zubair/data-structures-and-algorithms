# -*- coding: utf-8 -*-
"""
Created on Wed Apr  13 00:02:09 2020

@author: KM Zubair 
"""

if __name__ == '__main__':
    
    n = int(input())
    
    # Here map is used to convert all string inputs into integer
    integer_list = map(int, input().split())
    
    # After using map we need to use list() or tuple() to store inputs
    t = tuple(integer_list)
    print(hash(t))
    
