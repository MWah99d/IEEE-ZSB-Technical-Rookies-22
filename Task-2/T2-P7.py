#!/usr/bin/env python
# coding: utf-8

# In[1]:


S = input("Please Enter a string: ")
SS = input("Please enter a substring: ")
count = 0
for i in range(len(S)):
    if SS == S[i:i+ len(SS)]:
        count+=1
print("Number of occurrences of the substring in the string is:",count)

