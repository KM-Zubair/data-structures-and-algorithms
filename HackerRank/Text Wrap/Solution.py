# -*- coding: utf-8 -*-
"""
Created on Wed Apr  17 3:35:23 2020

@author: KM Zubair 
"""



import textwrap

def wrap(string, max_width):
    
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
