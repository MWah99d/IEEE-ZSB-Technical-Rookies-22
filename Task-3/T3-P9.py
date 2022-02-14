#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input("Enter steps number: "))
h = list(input("Enter steps' path: "))
p = ["D","U"]
v = 0
c = 0
for i in h:
    if i not in p:
        print("Invalid input")
        break
    if i == p[0]:
        c -= 1
    if i == p[1]:
        c += 1
    if i == p[1] and c == 0:
        v += 1
print(v)

