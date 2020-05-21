#!/usr/bin/env python
# coding: utf-8

# In[62]:


import numpy as np
def gen_vander_matrix(ipvector, n, increasing=False):
    if not increasing:
        op_matx = np.array([x**(n-1-i) for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    elif increasing:
        op_matx = np.array([x**i for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    return(op_matx)

inputvector = np.array([1,2,3,4,5])
no_of_col=5
op_matx_dec_order = gen_vander_matrix(inputvector,no_of_col,False)
op_matx_inc_order = gen_vander_matrix(inputvector,no_of_col,True)
print("In decreasing order\n\n",op_matx_dec_order)
print('*'*50)
print("In Increasing order\n\n",op_matx_inc_order)

