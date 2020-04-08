# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:08:26 2020

@author: KM Zubair
"""

if __name__ == '__main__':
    
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())
    
    arr = [[i,j,k] for i in range(0, X + 1) for j in range(0, Y + 1) for k in range(0, Z + 1) if ((i + j + k)!= N)]
    # You can also use (( X + Y + Z ) != N) in the previos line, it's same
    print(arr)
