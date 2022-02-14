#!/usr/bin/env python
# coding: utf-8

# In[ ]:


t = int(input("Enter the cases number: "))
l = []
for i in range (t):
    n,c,m = map(int,input().split())
    choco = count = int(n/c)
    while choco >= m:
        ret = choco // m
        count += ret
        choco = choco % m + ret
    l.append(count)
for i in l:
    print(i)

