#!/usr/bin/env python
# coding: utf-8

# In[3]:


#t2 q2
for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(5):
    for j in range(5-i-1):
        print("*",end=" ")
    print()

