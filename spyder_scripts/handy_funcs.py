#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:34:59 2019

@author: callum
"""

def fibonacci(n):
    # This if statement prints an error statement and returns no value if the provided n is not an integer
    if type(n)!=int:
        print('Please enter an integer')
        return
    fseq = []               # creates an empty list 
    a, b = 0, 1             # defining variables to start the fibonacci sequence
    while len(fseq) < n:    # Start a while loop that stopw when the list fseq is the lenght of the input number
        a, b = b, a + b     # Compute the next fibonacci number
        fseq.append(a)      # Append this number to the list

    return fseq             # Return the list