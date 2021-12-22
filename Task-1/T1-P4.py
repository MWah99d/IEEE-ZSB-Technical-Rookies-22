#!/usr/bin/env python
# coding: utf-8

# In[1]:


S = input("Please, Enter A Sentence: ")
def frame(words):
    size = len(max(words, key=len))
    print('*' * (size + 4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
frame(S.split(" "))


# In[ ]:




