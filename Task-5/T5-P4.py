#!/usr/bin/env python
# coding: utf-8

# In[ ]:


m = list(map(int,(input("Enter elements number and diffrence: ").split())))
a = list(map(int,(input("Enter array: ").split())))
d,r,m = m[1],[],[]
for i in range(len(a)-1):
    if ((a[i]+d) in a)  and ((a[i]+2*d) in a):
        r.append(i)
        r.append(a.index(a[i]+d))
        r.append(a.index(a[i]+2*d))
        m.append(r)
print(len(m))

