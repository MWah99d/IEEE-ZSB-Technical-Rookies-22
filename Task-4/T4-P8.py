#!/usr/bin/env python
# coding: utf-8

# In[ ]:


T = int(input("Enter the cases number: "))
for i in range(T):
    n = int(input("Enter stones numbers: "))
    a = int(input("Enter the possible diffrence: "))
    b = int(input("Enter the other possible diffrence: "))
    print(*sorted(set(x * a + (n - 1 - x) * b for x in range(n))))

