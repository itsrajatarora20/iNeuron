#!/usr/bin/env python
# coding: utf-8

# In[1]:


def myreduce(myfun,values):
    result=values[0]
    for i in values[1:]:
        result=myfun(result,i)
    return(result)

def myfunction(p,q):
    return(p+q)


values=[10,20,30,50,60,80,10]
a=myreduce(myfunction,values)
print(a)

