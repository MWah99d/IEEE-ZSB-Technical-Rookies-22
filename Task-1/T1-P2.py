#!/usr/bin/env python
# coding: utf-8

# In[1]:


X = int(input("Please Enter A Number > 1: "))    
for num in range(1,X+1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num, end = ' ')  


# In[ ]:




