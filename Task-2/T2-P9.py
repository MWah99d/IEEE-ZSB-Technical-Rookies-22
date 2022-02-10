#!/usr/bin/env python
# coding: utf-8

# In[1]:


O = int(input("Enter the matrix order: "))
M = [list(map(int,input("Enter row %i: " %(i+1)).split())) for i in range(O)]
D1=D2=0
for i in range(O):
    D1 += M[i][i]
    D2 += M[i][O-i-1]
DD = abs(D1-D2)
print("Diagonals difference:",DD)

