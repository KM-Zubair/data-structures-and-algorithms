# -*- coding: utf-8 -*-
"""
Created on Wed Apr  17 17:29:43 2020

@author: KM Zubair (Got the idea from internet)
"""


def print_formatted(number):
    # your code goes here
    # Here -2 is used just to match the width for hackerrank answer, the answer remains same without it
    # Same as width = len(bin(n))
    width = len(bin(n)) -2
    
    for i in range(1, n + 1):
        # Same as print("{0:{width}d} {1:{width}o} {2:{width}X} {3:{width}b}".format(i,i,i,i,width = width))
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width = width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
