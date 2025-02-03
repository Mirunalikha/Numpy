#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np. array([10,20,30,40])
print("one dimensional array:",a)


# In[6]:


import numpy as np
b = np.array ([[10,20,30],[40,50,60]])
print("two dimensional array:",b)


# In[8]:


import numpy as np
c = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("three dimensionl array:",c)


# In[9]:


import numpy as np
d = np.zeros((3,5))
print("\n array with all zeros\n:",d)


# In[13]:


import numpy as np
d = np.random.random((3,5))
print("\n random value:\n",d)


# In[15]:


import numpy as np
e = np.arange(0,10,1)
print("\n sequence value:\n",e)


# In[17]:


import numpy as np
orgarr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
newarr = orgarr.reshape(4,3)
print("\n orginal array:\n",orgarr)
print("\n reshaped array:\n",newarr)


# In[23]:


import numpy as np
orgarr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
flatarr = orgarr.flatten()
print("\n original array:\n",orgarr)
print("\n flatten array:\n",flatarr)


# In[ ]:


impo

