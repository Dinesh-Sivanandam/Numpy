#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np   # download numpy packagesby pip install numpy
np.arange(1,17,2,int)    # creating nd array
np.arange(1,16.0)       # for float element


# In[16]:


arr = np.arange(1,17)
#shaping
arr.shape=(4,4)
arr.size  #for array size


# In[18]:


#array
arr = np.array([1,2,3,4,5,6])
arr


# In[23]:


#3x3 matrix
arr = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
arr


# In[4]:


#zeros
arr = np.zeros((3,3), dtype=int)
arr


# In[5]:


#ones
arr = np.ones((3,3), dtype=int)
arr


# In[11]:


#empty
arr = np.empty((3,3), dtype=int)
arr


# In[18]:


#copying
#asignment copy
arr = np.ones(5)
arr1 = arr
get_ipython().run_line_magic('timeit', 'arr1 = arr')
print(id(arr))
print(id(arr1)) #same id
arr[2] = 3
arr1


# In[17]:


# shallow copy
arr = np.ones(5)
get_ipython().run_line_magic('timeit', 'arr1 = arr.view()')
arr1 = arr.view()
print(id(arr))
print(id(arr1)) #different id but same elemen referencee
arr1[2] = 3
arr


# In[20]:


#deep copy
arr = np.ones(5)
get_ipython().run_line_magic('timeit', 'arr1 = arr.copy()')
arr1 = arr.copy()
print(id(arr))
print(id(arr1)) #different id but same elemen referencee
arr1[2] = 3
print(arr)
print(arr1)


# In[23]:


#linear or sequential search
arr = np.array([1,2,2,4,5,3,2])
get_ipython().run_line_magic('timeit', 'index = np.where(arr%2==1)')
index = np.where(arr%2==1)
index


# In[25]:


#Binary search
arr = np.array([1,2,2,2,3,4,5])
get_ipython().run_line_magic('timeit', 'index = np.searchsorted(arr,2)')
index = np.searchsorted(arr,2)
index


# In[27]:


#multiplication
arr1 = np.array([100, 200, 300, 400]).reshape(2,2)
arr2 = np.array([1, 2, 3, 4]).reshape(2,2)
arr3 = arr1*arr2
arr3 = arr1.dot(arr2)
arr3 = arr1@arr2
arr3

