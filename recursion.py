#!/usr/bin/env python
# coding: utf-8

# In[8]:


# def sagar (x,y):
def square(x,y):
    return(x*y)


# In[9]:


square(7,8)


# In[6]:


def factorial(x):
    if x==1 or x==0:
        return(x)
    else:
        return(x*(factorial(x-1)))


# In[7]:


print(factorial(2))

print(factorial(3))

print(factorial(0))

# print(factorial(/))


# # Generting Fibonacci Sequence

# In[23]:


def fibonacci(f):
    if f==0:
        
        return(0)
    elif f==1:
        return(1)
            
    else:
        return fibonacci(f-1)+fibonacci(f-2)


# In[26]:


fibonacci(8)


# In[ ]:




