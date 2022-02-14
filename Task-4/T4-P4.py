#!/usr/bin/env python
# coding: utf-8

# In[ ]:


d1, m1, y1 = map(int, input("Enter the expected return date: ").split())
d2, m2, y2 = map(int, input("Enter the expected return date: ").split())
f = [(d1-d2)*15,(m1-m2)*500,(y1-y2)*10000]
if sum(f)>0:
    print(max(f))

