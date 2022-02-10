#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Please enter the number of array elements:"))
A = list(map(int, input("Please enter the array elements separated by spaces:").split()))
A2 = sorted(set(A))
print("The second maximum number is:",A2[-2])

