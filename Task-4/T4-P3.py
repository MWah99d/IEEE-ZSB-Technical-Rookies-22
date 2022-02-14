#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date
from mimetypes import init
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class linked:
    def __init__(self):
        self.head=None
        self.counter=0
    def show(self):
        node=self.head
        while(node):
            print(node.data)
            node=node.next
    def insertion(self,p,n):
        n = node(n)
        n.next = p.next
        p.next = n
    def deletion(self,d):
        store = self.head
        if (store is not None):
            if (store.data == d):
                self.head = store.next
                store = None
                return
        while(store is not None):
            if store.data == d:
                break
            prev = store
            store = store.next
        if(store == None):
            return
    def count(self, li, key):    
        if(not li):   #return 0 if there is no list 
            return self.counter
        if(li.data == key):
            self.counter = self.counter + 1
        return self.count(li.next, key)

