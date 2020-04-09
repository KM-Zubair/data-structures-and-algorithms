# -*- coding: utf-8 -*-
"""
Created on Wed Apr  10 01:25:56 2020

@author: KM Zubair 
"""
import statistics

if __name__ == '__main__':

    n = int(input())
    
    # Using a dictionary
    student_marks = {}
    
    for _ in range(n):
        # Here the * grabs rest of the input after 'name' and put in a list of strings like ['67', '68', '69', '70'] 
        name, *line = input().split()
        
        # Here map is used to convert strings into floats
        scores = list(map(float, line))
        # calling the key 'name' and change it's scores
        student_marks[name] = scores
        
    # Taking input of the name
    query_name = input()
    # Calling the values of this key(Here 'query_name') from the dictionary
    # And putting those values to a list
    average_list = student_marks[query_name]
    
    # using the preloaded statistic mean function to find the average
    print('%.2f' %(statistics.mean(average_list)))
