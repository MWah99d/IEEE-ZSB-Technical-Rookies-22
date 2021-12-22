#!/usr/bin/env python
# coding: utf-8

# In[14]:


n = int(input("Enter +ve Number: ")) 
n1, n2 = 0, 1
count = 0
if n == 1:
    print("Fibonacci sequence upto",n,":")
    print(n1)
else:
    print("Fibonacci Numbers:")
    while count < n:
        print(n1,end = ' ')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


# In[ ]:




