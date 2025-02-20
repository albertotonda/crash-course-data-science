# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:58:16 2025

@author: Alberto
"""

if __name__ == "__main__" :
    
    list_a = [1, 2, 3, 4, 5]
    dict_a = {"key1" : "value1", "key2" : 2}
    
    for element in list_a :
        print(element)
        
    for key, value in dict_a.items() :
        print("key:", key, " -> value:", value)
        
    list_b = ["a", "b", "c", "d", "e"]
    for index, element in enumerate(list_b) :
        # as you might notice, Python indexes start at 0
        print("Element at index %d is \"%s\"" % (index, element))