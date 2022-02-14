#!/usr/bin/env python
# coding: utf-8

# In[ ]:


dt = list(map(int,(input("Enter days and time: ").split())))
d = dt[0]
t = dt[1]
wt = list(map(int,(input("Enter day work time: ").split())))
r = 0
c = 0
for i in range(d):
    if r >= t:
        break
    r = 86400 - wt[i]
    c += 1
print(c)

