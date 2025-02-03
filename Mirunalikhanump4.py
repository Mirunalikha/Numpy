#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([20,40,50,70,10])
b=np.array([6,2,9,7,11])
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)


# In[2]:


#dot product
print(a.dot(b))
sclr=3
print("scalar value:",sclr)
print("Array:",a)
print("Result:",a*sclr)


# In[4]:


#vector operation
a=np.array([[10,20],[30,40]])
b=np.array([[3,7],[5,9]])
print(a%b)


# In[8]:


def my_fun(x,y):
    if x>y: 
        return x-y
    else:
        return x+y
arr1=[10,7,2]
arr2=[6,5,3]
vect_fun=np.vectorize(my_fun)
print("Array1:",arr1)
print("Array2:",arr2)
print("Result:",vect_fun(arr1,arr2))


# In[ ]:




