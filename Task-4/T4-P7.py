#!/usr/bin/env python
# coding: utf-8

# In[ ]:


p = int(input())
q = int(input())
l = []
for i in range(p,q+1):
    sqr = str(i**2)
    n = len(sqr)
    if i == 1:
        l.append(i)
    elif n > 1 and i == int(sqr[:n // 2]) + int(sqr[n // 2:]):
        l.append(i)
if len(l) == 0:
    print('INVALID RANGE')
else:
    print(*l)

