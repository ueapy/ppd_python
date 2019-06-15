#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:21:41 2019

@author: callum

An example python script to demonstrate some features of the Spyder IDE
"""

# The area above this comment enclosed in triple comments is where you document
# what your script is for

import numpy as np
import pandas as pd

# Scripts begin by importing all the moduels you will need. Don't scatter your
# import statements around!

# we can import stuff from our own scripts too

from handy_funcs import (fibonacci)

# If it doesn't find this other script, check Spyder is running in the right place
# Look at the top of the editor for a path 

# Next we define any new functions we will use in this script
def introduce(my_name):
    print('Hi, my name is '+str(my_name))



#%%
# This pattern #%% breaks your script up into cells. This is handy as individual
# cells can be run with a keyboard shortcut set in Tools > Preferences

print('Hello world')

introduce('Spyder')

# Any command that produces output will print it to the console in the lower right

a = 15
b = 'foobar'
c=  np.empty((5,5))

# Check out the variable explorer in the upper right pane to see the variables
# you have created

# Let's run our fibonacci function
fibonacci(5)