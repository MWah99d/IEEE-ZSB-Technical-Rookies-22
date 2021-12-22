#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
array = list(map(int, input("Enter List Numbers In Ascending Order Separated By Spaces:").split(" ")))
print("Your List Is: ",array)
x = int(input("Enter List Number: "))
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print("Number is present at index: " + str(result))
else:
    print("Not found")


# In[ ]:




