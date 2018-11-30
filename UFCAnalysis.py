#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np


# In[13]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


df = pd.read_csv('UFCdata.csv')


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.columns


# In[51]:


df['B_Age'] = df['B_Age'].fillna(np.mean(df['B_Age']))
df['B_Height'] = df['B_Height'].fillna(np.mean(df['B_Height']))
df['R_Age'] = df['R_Age'].fillna(np.mean(df['R_Age']))
df['R_Height'] = df['R_Height'].fillna(np.mean(df['R_Height']))


# In[54]:


fig, ax = plt.subplots(1,2, figsize=(16, 4))
sns.distplot(df.B_Age, ax=ax[0])
sns.distplot(df.R_Age, ax=ax[1])


# In[64]:


fig, ax = plt.subplots(1,2, figsize=(16, 4))
sns.distplot(df.B_Height, ax=ax[0],bins=10)
sns.distplot(df.R_Height, ax=ax[1],bins=10)


# In[60]:


fig, ax = plt.subplots(1,2, figsize=(16, 4))
sns.distplot(df.B_Weight, ax=ax[0],bins=9)
sns.distplot(df.R_Weight, ax=ax[1],bins=9)


# In[ ]:




