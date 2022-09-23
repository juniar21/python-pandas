#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Tips dan Trik Pandas WEEK 1


# In[ ]:


# 1. Membuat Suffix dan Prefix pada kolom Data Frame


# In[29]:


import pandas as pd
import numpy as np
import pandas.util.testing


# In[10]:


# Data Frame sederhana

a_row = 5
a_col = 5
col = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(a_row,a_col)),columns=col)

df


# In[7]:


tuple('ABCDE')


# In[11]:


# Menambahkan Prefix

df.add_prefix('kolom_')


# In[12]:


# Menambahkan Suffix

df.add_suffix('_field')


# In[ ]:





# In[ ]:


# 2. Pemilihan baris pada Data Frame


# In[14]:


# Selection dengan opeator logika | (OR)

df[(df['A'] == 1) | (df['A'] == 3)]


# In[15]:


# Selection dengan fungsi isin()

df[df['A'].isin([1,3])]


# In[16]:


# Mengenal operator negasi ~

df[~df['A'].isin([1,3])]


# In[ ]:





# In[ ]:


# 3 Konversi tipe data String ke Numerik pada kolom Data Frame


# In[18]:


# Data Frame Sederhana 

data = {'col1':['1','2','3','teks'],
       'col2':['1','2','3','4']}

df = pd.DataFrame(data)

df


# In[19]:


df.dtypes


# In[23]:


# Konversi tipe data denga fungsi astye()

df_x = df.astype({'col2':'int'})
df_x


# In[24]:


df_x.dtypes


# In[25]:


df.apply(pd.to_numeric,errors='coerce')


# In[ ]:





# In[ ]:


# 4 Pemilihan kolom (columns selection) pada Data Frame berdasarkan tipe data


# In[31]:


# Data Frame Sederhana

a_row = 5
a_col = 2
col = ['bil_pecahan','bil_bulat']

df = pd.DataFrame(np.random.randint(1, 20, size=(a_row, a_col)),
                 columns=col)
df['bil_pecahan'] = df['bil_pecahan'].astype('float')

df.index = pd.util.testing.makeDateIndex(a_row, freq='H')
df = df.reset_index()

df['teks'] = list('ABCDE')

df


# In[32]:


df.dtypes


# In[33]:


# Memilih bertipe data numerik

df.select_dtypes(include='number')


# In[34]:


df.select_dtypes(include='float')


# In[35]:


#Memilih kolom bertipe data string atau object

df.select_dtypes(include='object')


# In[36]:


#Memilih kolom bertipe data date time

df.select_dtypes(include='datetime')


# In[37]:


#Memilih kolom dengan kombinasi tipe data

df.select_dtypes(include=['datetime','object'])


# In[ ]:




