#!/usr/bin/env python
# coding: utf-8

# In[1]:


X = list(input("Enter List Numbers Separated By Spaces:\n").split(" "))
min = len(X)
for i in range (len(X)):
        for j in range (i+1,len(X)):
            if X[i]==X[j]:
                temp=(j-i)
                if temp < min :
                    min=temp
print(min)

