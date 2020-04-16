# -*- coding: utf-8 -*-
"""
Created on Wed Apr  16 9:06:08 2020

@author: KM Zubair 
"""



if __name__ == '__main__':
    s = input()
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    for x in s:
        # alphanumeric
        if x.isalnum() == True:
            count1 += 1
        else: 
            count1 += 0
            
        # alpha    
        if x.isalpha() == True:
            count2 += 1
        else: 
            count2 += 0
        
        # digit 
        if x.isdigit() == True:
            count3 += 1
        else: 
            count3 += 0
        
        
        # lowercase
        if x.islower() == True:
            count4 += 1
        else: 
            count4 += 0
        
        # upper
        if x.isupper() == True:
            count5 += 1
        else: 
            count5 += 0

    # Printing the results     
    if count1 != 0:
            print('True')
    else : print('False')
        
    if count2 != 0:
            print('True')
    else : print('False')
    
    if count3 != 0:
            print('True')
    else : print('False')
    
    if count4 != 0:
            print('True')
    else : print('False')
    
    if count5 != 0:
            print('True')
    else : print('False')
