#!/usr/bin/env python
# coding: utf-8

# In[91]:


#PART-1
lst=['A','C','A','D','G','I','L','D']
print(lst)


# In[47]:


#PART-2
l=[(i*chr(a)) for a in range(120,123) for i in range(1,5) ]
print(l)


# In[92]:


#PART-3
l=[(i*chr(a)) for i in range(1,5) for a in range(120,123)]
print(l)


# In[51]:


#PART-4
l=[]
lst=list(l.append([p+q]) for q in range(1,4) for p in range(1,4))
print(l)


# In[88]:


#PART-5
s=[2,3,4,5]
l = [[j for j in range(s[a],s[a]+4)] for a in range(4)] 
print(l)


# In[90]:


#PART-6
m=[(j,i) for j in range(1,4) for i in range(1,4)]
print(m)

