#!/usr/bin/env python
# coding: utf-8

# In[ ]:


P = []
P.append(random.choice("@#$%&"))
P.append(random.choice(string.digits))
for i in range(8): P.append(random.choice(string.ascii_letters + string.digits + "@#$%&"))
random.shuffle(P)
print("".join(P))

