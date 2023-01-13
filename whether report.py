#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("1. Weather Data.csv", sep=",")
data


# In[2]:


data.head()


# In[3]:


data.columns


# In[4]:


data.dtypes


# In[5]:


data.shape


# In[6]:


data.index


# In[9]:


data["Weather"].unique()


# In[10]:


data.nunique()


# In[11]:


data.head()


# In[12]:


data["Wind Speed_km/h"].nunique()


# In[13]:


data.info()


# In[14]:


data.count()


# In[16]:


data.head()


# In[18]:


data["Wind Speed_km/h"].unique()


# 

# In[19]:


data.head()


# In[22]:


data.Weather.value_counts()


# In[23]:


data[data.Weather=='Clear']


# In[25]:


data.groupby('Weather').get_group('Clear')


# In[28]:


data[data['Wind Speed_km/h']==4]


# In[29]:


data.head(2)


# In[31]:


data.isnull().sum()


# In[32]:


data.notnull().sum()


# In[33]:


data.head(2)


# In[41]:


data.rename(columns={'Weather':'Weather_condition'},inplace=True)


# In[40]:


data.head(2)


# In[42]:


data.head()


# In[44]:


data.head(2)


# In[45]:


data["Weather_condition"].value_counts()


# In[55]:


data[data['Weather_condition'] =='Snow ']


# In[58]:


data[data['Weather_condition'].str.contains('snow')].head(20)


# In[59]:


data.head(1)


# In[61]:


data[(data['Wind Speed_km/h'] >24) & (data['Visibility_km']==25)]


# In[64]:


data.groupby('Weather_condition').mean()


# In[65]:


data.head(2)


# In[68]:


data.groupby('Weather_condition').min()


# In[69]:


data.groupby("Weather_condition").max()


# In[70]:


data.groupby('Weather_condition').mean()


# In[71]:


data.head()


# In[74]:


data['Weather_condition'].value_counts()


# In[75]:


data[data['Weather_condition'] =='	Weather_condition']


# In[76]:


data.head()


# In[ ]:




