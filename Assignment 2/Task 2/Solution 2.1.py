#!/usr/bin/env python
# coding: utf-8

# In[1]:


def wordtolength(lst):
    l=[]
    for i in lst:
        l.append(len(i))
    return(l)
    
lst=input("Enter the elements seperated by space ").split()
print(wordtolength(lst))

