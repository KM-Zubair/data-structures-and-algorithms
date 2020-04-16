# -*- coding: utf-8 -*-
"""
Created on Wed Apr  16 6:36:31 2020

@author: KM Zubair 
"""



def count_substring(string, sub_string):
    
    c=0
    for i in range(len(string)):
        # If string is 'Hello' then s[1:4] is 'ell' -- 
        # because, chars starting at index 1 and extending up to but not including index 4
        # So here string[i:i+len(sub_string)] will work as range i to len(sub_string)
        if string[i:i + len(sub_string)] == sub_string:
            c +=1
            
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
