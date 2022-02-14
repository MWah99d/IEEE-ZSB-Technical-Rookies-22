#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = input("Enter the arrays' orders: ")
a = list(map(int,input("Enter 1st array: ").split()))
b = list(map(int,input("Enter 2nd array: ").split()))
c = 0
for i in range(max(a),min(b)+1):
    F = True
    for j in a:
        if i % j != 0:
            F = False
            break
    for j in b:
        if j % i != 0:
            F = False
            break
    if F == True:
        c += 1
print(c)

