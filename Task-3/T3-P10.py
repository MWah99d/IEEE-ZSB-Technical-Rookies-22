#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input("Enter the pages number: "))
p = int(input("Enter the page number: "))
print(min(int(n/2)-int(p/2),int(p/2)))

