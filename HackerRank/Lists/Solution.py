# -*- coding: utf-8 -*-
"""
Created on Wed Apr  12 23:34:09 2020

@author: KM Zubair 
"""
if __name__ == '__main__':
    N = int(input())
    
    list = []
    command = []
    
    for x in range(N):
        # Taking split input and putting into a list named command
        command = (input().split())
        if 'insert' in command:
            # using the insert method list.insert(index, element)
            # Converting the index and element to int
            list.insert(int(command[1]), int(command[2]))
        if 'print' in command:
            print(list)
        if 'remove' in command:
            list.remove(int(command[1]))
        if 'append' in command:
            list.append(int(command[1]))
        if 'sort' in command:
            list.sort()
        if 'pop' in command:
            list.pop()
        if 'reverse' in command:
            list.reverse()
