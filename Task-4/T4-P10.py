#!/usr/bin/env python
# coding: utf-8

# In[ ]:


b, n, m = map(int, input().split())
k = list(map(int,input().split()))[:n]
d = list(map(int,input().split()))[:m]
me = []
for i in k:
    for j in d:
        if i+j <= b:
            me.append(i+j)
print(max(me))

