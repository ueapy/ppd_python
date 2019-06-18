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

# We can import stuff from our own scripts too
# This particular script "handy_funcs.py" is in the same folder as this script 
from handy_funcs import fibonacci,under_pressure

# If it doesn't find this other script, check Spyder is running in the right place,
# Look at the top of the editor for a path 

# Next we define any new functions we will use in this script
def introduce(my_name):
    print('Hi, my name is '+str(my_name))



#%%
# This pattern #%% breaks your script up into cells. This is handy as individual
# cells can be run with a keyboard shortcut set in Tools > Preferences

# Any command that produces output will print it to the console in the lower right
    
print('Hello world')

introduce('Spyder')

a = 15
b = 'foobar'
c =  np.empty((5,5))

# Check out the variable explorer in the upper right pane to see the variables
# you have created
#%%
# Let's run our pressure script

Pressure = under_pressure(100)
print(Pressure)
#%%
# And another function
fibonacci(6)
#%%

# We can import data from files just as we do in a Jupyter Notebook

fname = '../data/ship_ctd_short.csv'
ctd_data = pd.read_csv(fname)
ctd_data.head()

# One difference you'll notice is that Spyder lacks some of Jupyter Notebook's
# user friendly rendering of Pandas dataframes

