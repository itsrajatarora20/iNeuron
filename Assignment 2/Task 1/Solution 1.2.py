#!/usr/bin/env python
# coding: utf-8

# In[2]:


def myfilter(myfun,values):
    result=values[0]
    for i in values[1:]:
        result=myfun(result,i)
    return(result)

def myfunction(p,q):
    return(p if p>q else q) 


values=[10,20,30,20,50,30,50,90,10,20]
a=myreduce(myfunction,values)
print(a)

