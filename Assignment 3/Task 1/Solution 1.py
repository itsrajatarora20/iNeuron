#!/usr/bin/env python
# coding: utf-8

# In[12]:


def zerodivision(x,y):
    try:
        z=x/y
        return z
    except ZeroDivisionError:
        return(" It's an EXCEPTION ")

x=int(input("Enter first number: "))
y=int(input("Enter first number: "))

print(zerodivision(x,y))

