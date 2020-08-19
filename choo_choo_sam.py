#!/usr/bin/env python
# coding: utf-8

# In[39]:


import time
ts = time.sleep
from IPython.display import clear_output
def long_train():
    space_at_start = 50
    while space_at_start > 0:
        print(" " * space_at_start, end = '')
        print("\U0001F682" + ".", end ='')
        for n in range (20):
            print("\U0001F683" + ".", end = '')
        print("\U0001F683", end = '')
        space_at_start-=1
        ts(0.08)
        clear_output(wait=True)


# In[40]:


long_train()


# ## 
