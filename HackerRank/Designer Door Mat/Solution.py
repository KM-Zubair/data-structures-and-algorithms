# -*- coding: utf-8 -*-
"""
Created on Wed Apr  17 4:47:15 2020

@author: KM Zubair 
"""


if __name__ == '__main__':
    n,m = map(int, input().split())

    # Range gap is 2 so the .|. prints as the sequnce as 1,3,5 like this
    for i in range(1,n,2):
        # center(width, '-') is used as text alignment
        print(('.|.'*i).center(m,'-'))
    
    print(('WELCOME').center(m,'-'))

    # Using the reverse function to print values from high to low like 5,3,2
    for i in reversed(range(1,n,2)):
        print(('.|.'*i).center(m,'-'))
