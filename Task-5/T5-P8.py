#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
r = []
for i in range (n):
    sm = 0
    f = list(str(input()))
    s = list(str(input()))
    for j in f:
        if j not in s:
            f.remove(j)
            sm += 1
    for k in s:
        if k not in f:
            f.append(k)
            sm += 1
    r.append(sm)
for l in r:
    print(l)

