#!/usr/bin/env python
# coding: utf-8

# In[1]:


X = list(map(int, input("Enter List Numbers Separated By Spaces:\n").split(" ")))
for i in range(1,len(X)):
    Y = X[i]
    j = i - 1
    while j >= 0 and Y < X[j]:
            X[j+1] = X[j]
            j -= 1
    X[j+1] = Y
print("Sorted List:\n",X)

