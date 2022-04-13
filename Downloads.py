#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[81]:


df = pd.read_csv('Cars.csv')
df.head()


# In[ ]:


#حذف الاعمدة الغير مهمة 

#Delete uncons task columns

df.drop('Unnamed: 26', axis=1 , inplace=True)
df.drop('Unnamed: 27', axis=1 , inplace=True)


# In[88]:


df.head()


# In[37]:


#معرفة حجم البيانات وعدد الاعمدة 

#Find out the size of the data and the number of columns 

df.shape


# In[38]:


#وصف البينات

#Data description 

df.describe()


# In[39]:


#روئية البيانات بطريقة اوضح

#check data types

df.info()


# In[40]:


#معرفة عدد البيانات

#Find out how many data

df.count()


# In[41]:


#معرفة عدد اللاعمدة المتكررة او النوع

#Find out how many columns are repeated or type

df.duplicated().sum()


# In[42]:


#معرفة نوع القيم 

#Type of values

df.value_counts()


# # Analysis phase

# In[43]:


df.head()


# In[44]:


#معرفة انوع السيارتا

#Knowing the types of cars

df['aspiration'].unique()


# In[45]:


#معرفة العدد والانواع

#Know the number and types

df['aspiration'].value_counts()


# In[46]:


#التعديل ع الاسماء الاعمدة
    
#Editing the names is deliberate    
    
num=df.describe()

num.columns

df[['symboling', 'normalized-losses', 'make', 'fuel-type', 'width',
       'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'bore',
       'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',
       'highway-mpg', 'price', 'Unnamed: 26', 'Unnamed: 27']]


# In[47]:


#معرفة سعر السيارات 

#Find out the price of cars 

df.groupby('aspiration')['highway-mpg'].mean()


# In[50]:


df.columns


# In[58]:


#عرض نوع مكان المحرك لكل سيارة

#View engine location and Types for each car


df.groupby(['engine-location','engine-type']).mean()


# In[89]:


#عرض الطول والعرض والمقارنة بينهم 

# Show height width and comparison

df[['height', 'width', 'length']].describe()


# # small Visualization data
# 

# In[123]:


#عرض المخططات لجميع البيانات

#View charts for all data

df.hist(figsize=(10,10));


# In[143]:


#حجم المحرك الاكثر استخداما

#The most commonly used engine size

df['fuel-system'].hist(figsize=(8,8));


# In[142]:


#عرض المخطط لجميع انوع السيارات

#View the chart for all types of cars

df['aspiration'].value_counts().plot(kind='bar',figsize=(10,10));


# In[ ]:




