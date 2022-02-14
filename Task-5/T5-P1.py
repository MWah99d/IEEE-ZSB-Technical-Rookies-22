#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxHeap(arr, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    max = i
    if left < n and arr[left] > arr[i]:
        max = left
    if right < n and arr[right] > arr[max]:
        max = right
    if max != i:
        arr[i], arr[max] = (arr[max], arr[i])
        maxHeap(arr, max, n)
def buildMaxHeap(arr, n):
    for i in range(int(n - 2)//2, -1, -1):
        maxHeap(arr, i, n)
arr = list(map(int, input().split()))
n = len(arr)
buildMaxHeap(arr, n)
print(" ".join(map(str,arr)))

