#!/usr/bin/env python
# coding: utf-8

# In[4]:


lst = []
Size = int(input("Enter Size Of List:"))
lst = list(map(int, input("Enter List Numbers Separated By Spaces:").split(" ")))
print("Sum =",sum(lst))

total = 0
for num in lst:
    total = total + num
print("Sum =", sum(lst))

total = 0
loop_counter = 0
while loop_counter < Size:
    total = total + lst[loop_counter]
    loop_counter = loop_counter + 1
print("Sum =", total)

def recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + recursive(lst[1:])
total = recursive(lst)
print("Sum =",total)

