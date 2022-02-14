#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input("Enter number of bottles: "))
f = [list(map(int,input("Enter water volume and capacity: ").split())) for i in range(n)]
w,c = [],[]
for i in range(n):
    w.append(f[i][0])
    c.append(f[i][1])
c.sort()
if sum(w) <= (c[-1] + c[-2]):
    print("Yes")
else:
    print("No")

