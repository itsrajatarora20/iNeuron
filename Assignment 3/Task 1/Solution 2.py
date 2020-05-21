#!/usr/bin/env python
# coding: utf-8

# In[3]:


subjects=["Americans","Indians"]
verbs=["plays","watch"]
objects=["Baseball","Cricket"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            print(subjects[i],verbs[j],objects[k])

