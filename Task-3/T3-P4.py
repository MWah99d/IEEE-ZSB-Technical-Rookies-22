#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = list(map(int,input("Enter the data: ").split()))
x1,v1,x2,v2 = a[0],a[1],a[2],a[3]
if (x1-x2)*(v1-v2)<0:
    if(x2-x1)%(v1-v2)==0:
        print("Yes")
    else:
        print("No")
else:
        print("No")

