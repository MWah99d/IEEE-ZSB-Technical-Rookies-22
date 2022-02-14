#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s = input("Enter the letters: ")
n = int(input("Enter n: "))
r = s.count("r")
r += s.count("R")
r *= (n//len(s))
for i in range(n%len(s)):
    if s[i] == "r" or s[i] == "R":
        r += 1
print(r)

