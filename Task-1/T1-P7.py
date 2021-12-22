#!/usr/bin/env python
# coding: utf-8

# In[14]:


n = int(input("Enter +ve Number:"))
Sum = sum(i for i in range(n+1) if i%3 == 0 or i%5 == 0)
print("Sum =",Sum)

