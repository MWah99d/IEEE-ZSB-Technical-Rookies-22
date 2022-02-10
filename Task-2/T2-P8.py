#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input("Please enter the number of students: "))
R = []
for i in range(1,N+1):
    S = input("Please enter student %i: " %i)
    G = float(input("%s's grade: "%S))
    R.append([G,S])
R.sort()
if R[1][0] == R[2][0]:
    print(R[1][1])
    print(R[2][1])
else:
    print(R[1][1])

