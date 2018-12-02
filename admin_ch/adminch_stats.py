#!/usr/bin/env python
# coding: utf-8

# In[4]:


## Calculating statistics out of clean admin.ch Veranstaltungen data
## WORK IN PROGRESS
##


# In[5]:


import glob
import pandas as pd


# In[6]:


# Read the clean data
#
#
df = pd.read_csv('working.csv')


# In[ ]:





# In[7]:


df.head()


# In[ ]:


# search
#
# 




# In[11]:


df.dtypes
df.head()
df['Year'].value_counts()
df.groupby('Year')['Veranstalter'].value_counts()
df.groupby('Year')['Veranstalter'].value_counts()
#df_all.groupby('Organisator')['Year'].value_counts()
#df_all[(df_all['Year'] == '2015')]


df[
    (df['Year'] == 2015)
]['Veranstalter'].value_counts()


# In[ ]:


df_all.groupby('Year')['Organisator'].value_counts()
#df_all.groupby('Organisator')['Year'].value_counts()
df_all['Year']
df_all[df_all['Organisator'].isin(df_all['Organisator'].value_counts()[df_all['Organisator'].value_counts()>540].index)]


# In[ ]:




#df_all['New Date'].head()

#df_all['New Date'=='2010-01-01']
df_all[
    (df_all['New_Date'] > '2010-01-01') #| (df['PTS']>32000)
].count()

pd.DataFrame(df_all.New_Date.str.split('-',2).tolist(), columns = ['Year','Month','Day'])


# In[ ]:



#df_all.groupby('Organisator').count()
df_all['Address'].value_counts().head()
#df_all.iloc[1]

