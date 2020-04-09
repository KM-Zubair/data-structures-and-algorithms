# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 22:20:06 2020

@author: KM Zubair ( Got most part of this solution from the internet )
"""
# print function must be inserted in the very beginnig of the code, excluding some exceptions
from __future__ import print_function

if __name__ == '__main__':

    # using a dictionary
    score_dict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
    
        if score in score_dict:
        # This way, if the score is already inserted it will append more names
            score_dict[score].append(name)
        else:
            # If the score is not yet inserted then it will add both score and name
            score_dict[score] = [name]

    nested_list = []
    # Converting dictionary (score_dict) into list and putting into nested_list
    for i in score_dict:
        nested_list.append([i, score_dict[i]])
        
        nested_list.sort()

    # If you put new_list[1] it will return that list of index 1
    # If you put new_list[1][1] it will return second part of the list of that index
    # In this case it's returning the names
    result = nested_list[1][1]
    result.sort()

    # Calling the print function here
    print (*result, sep = "\n")
