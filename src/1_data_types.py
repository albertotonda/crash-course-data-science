# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:18:44 2025

@author: Alberto
"""

if __name__ == "__main__" :
    # we can write all our code directly here,
    # or invoke a function, having the script return its return code
    # sys.exit( main() )
    
    integer_a = 1
    integer_b = integer_a + 1
    print("integer_a: %d" % integer_a)
    print("integer_b:", integer_b)
    print(f"integer_a: {integer_a}")
    
    float_a = 32.12
    float_b = 7.000000000000002
    print(float_b)
    
    dictionary_a = dict()
    dictionary_b = {}
    
    dictionary_a["key1"] = "value1"
    dictionary_a["key2"] = 12
    
    print(dictionary_a)
    
    # what's happening here? is this the expected behavior?
    list_a = [1, 2, 3]
    list_b = list_a
    list_b[0] += 1
    print(list_a)
    print(list_b)
    # try modifying the the assignment with list_b = list(list_a)