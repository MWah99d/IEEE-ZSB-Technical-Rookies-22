#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input("Enter socks number: "))
c = list(map(int,input("Enter socks' colors: ").split()))
p = []
count = 0
for i in c:
    if i not in p:
        p.append(i)
    else:
        p.remove(i)
        count += 1
print(count)

