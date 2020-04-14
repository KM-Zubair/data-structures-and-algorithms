# -*- coding: utf-8 -*-
"""
Created on Wed Apr  15 4:27:01 2020

@author: KM Zubair 
"""



def mutate_string(string, position, character):
    result = string[:position] + character + string[position+1:]
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
