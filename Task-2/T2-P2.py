#!/usr/bin/env python
# coding: utf-8

# In[1]:


X = list(input("Enter List Numbers Separated By Spaces:\n").split(" "))
Y = []
for num in X:
    if num not in Y:
        Y.append(num)
print(" ".join(Y))


# In[ ]:




