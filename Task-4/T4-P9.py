#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
m = []
for x in range(n):
    m.append(list(input()))
m2 = [list(y) for y in m]
for i in range(1,len(m2)-1):
    for j in range(1,len(m2)-1):
        if m2[i][j]>m2[i-1][j] and m2[i][j]>m2[i+1][j] and m2[i][j]>m2[i][j-1] and m2[i][j]>m2[i][j+1]:
            m2[i][j] = "X"
for k in range(n):
    print("".join(m2[k]))

