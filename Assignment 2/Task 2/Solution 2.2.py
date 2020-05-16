#!/usr/bin/env python
# coding: utf-8

# In[10]:


def chartobool(string):
    for i in range(len(string)):
        if string[i].lower() in ["a","e","i","o","u"]:
            print("True")
        else:
            print("False")
    
    
string=input("Enter the string ")
chartobool(string)

