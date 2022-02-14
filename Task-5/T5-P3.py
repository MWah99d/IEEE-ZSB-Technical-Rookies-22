#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import copy
l1=list(map(int,(input("Enter N, k and q:\n").split())))
a=list(map(int,(input("Enter array:\n").split())))
k=l1[1]
q=l1[2]
n=[]
h=copy.deepcopy(a)
for i in range (0,k):
    h.insert(0,h.pop(len(h)-1))
g = h
for i in range(0,q):
    n.append(int(input()))
for i in n:
    print(g[i])

