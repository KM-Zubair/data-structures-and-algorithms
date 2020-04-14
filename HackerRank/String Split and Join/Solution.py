# -*- coding: utf-8 -*-
"""
Created on Wed Apr  14 9:40:09 2020

@author: KM Zubair 
"""



def split_and_join(line):
    line = line.split(" ")
    line = ("-").join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
