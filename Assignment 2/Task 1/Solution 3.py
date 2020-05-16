#!/usr/bin/env python
# coding: utf-8

# In[1]:


def longestWord(lst):
    l=[]
    for i in lst:
        l.append(len(i))
    no=max(l)
    l1=[]
    for i in lst:
        if len(i)==no:
            l1.append(i)
    return(l1)

lst=input().split()
new=longestWord(lst)
print(new)

