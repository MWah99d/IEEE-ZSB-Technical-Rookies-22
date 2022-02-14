#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = input("Enter 4-digit number: ")
count = 0
if len(n)>4:
    print("Invalid number")
else:
    while n != "6174":
        if 4 - len(n) == 1:
            n += "0"
        if 4 - len(n) == 2:
            n += "00"
        if 4 - len(n) == 3:
            n += "000"
        asc = sorted(n)
        desc = sorted(n,reverse=True)
        asc_i = int("".join(asc))
        desc_i = int("".join(desc))
        subtract = desc_i - asc_i
        s_subtract = str(subtract)
        n = s_subtract
        count += 1
    print(count)

