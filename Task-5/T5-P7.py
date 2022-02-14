#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
def solution():
    r1 = 0
    c1 = 0
    for i in range(len(t)-1):
        for j in range(i+1, len(t)):
            tmp = bin(int(t[i], 2) | (int(t[j], 2))).count("1")
            if tmp > r1:
                r1 = tmp
                c1 = 1
            elif tmp == r1:
                c1 += 1
    return (r1, c1)
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
t = []
t_i = 0
for t_i in range(n):
    t_t = str(input().strip())
    t.append(t_t)
print("\n".join(map(str, solution())))

