#!/usr/bin/env python
# coding: utf-8

# In[ ]:


t = int(input("Enter the cases number: "))
l = []
for i in range(t):
    n , c = input("Enter number %i: "  %(i+1)) , 0
    tn , n = int(n) , list(map(int,n))
    for j in n:
        if j != 0 and tn % j == 0:
            c += 1
    l.append(c)
for i in l:
    print(i)

