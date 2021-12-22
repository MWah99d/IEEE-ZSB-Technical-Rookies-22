#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
n = random.randint(0,10)
Count = 0
while Count < n:
    Count += 1
    g = int(input("Guess A Number In Range(1:10):"))
    if g == n:
        print("Yah You Got It ",Count," Tries")
        break
    elif g != n:
        print("wrong Guess, Try Again")

