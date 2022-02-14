#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = input("Enter birds number: ")
b = list(map(int,input("Enter birds types: ").split()))
t = [0]*6
for i in b:
    t[i] += 1
print(t.index(max(t)))

