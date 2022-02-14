#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for i in range(int(input())):
   fc, rc = map(int, input().split())
   f = map(int, input().split())
   l = []
   for j in f:
       while rc and l and l[-1] < j:
           l.pop()
           rc -= 1
       l.append(j)
   print("Popularity after deleting: ")
   print(' '.join(map(str, l)))
   print("--------------------------")

