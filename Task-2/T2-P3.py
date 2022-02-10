#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
n = str(random.randint(100,999))
count = 0
print(n)
while(True):
    hit = 0
    miss = 0
    count += 1
    g = str(input("Guess a 3-digit number:"))
    if g == n:
        print("You did it after",count,"Tries")
        break
    else:
        for i in range(3):
            if g[i] == n[i]:
                hit += 1
        for i in range(3):
            for j in range(3):
                if g[i] == n[j]:
                    miss += 1
        print(hit,"hit",miss-hit,"miss") 


# In[ ]:




