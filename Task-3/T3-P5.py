#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input("Enter number of games: "))
S = list(map(int,input("Enter games scores: ").split()))
H = L = S[0]
Max = Min = 0
for i in S:
    if i > H:
        H = i
        Max += 1
    if i < L:
        L = i
        Min += 1
print(Max,Min)

