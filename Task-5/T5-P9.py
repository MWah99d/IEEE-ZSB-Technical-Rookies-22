#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hackerrankInString(s):
    l = ['h','a','c','k','e','r','r','a','n','k']
    for i in s:
        if(i == l[0]):
            l.pop(0)
        if(len(l) == 0):
            return "YES"
    return "NO"
n = int(input().strip())
for i in range(n):
    s = input()
    print(hackerrankInString(s))

