# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 03:13:46 2020

@author: KM Zubair
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    for times in range(n):
        arr
    
    new_list = set(arr)
    new_list.remove(max(arr))
    print(max(new_list))
