#!/usr/bin/env python
# coding: utf-8

# In[ ]:


np = input()
p = list(set(list(map(int,(input().split())))))
p.sort()
ng = int(input())
s = list(map(int,(input().split())))
l = len(p)
i = 0
for x in s:
    while i<l and p[i]<=x:
        i+=1
    print(l-i+1)

