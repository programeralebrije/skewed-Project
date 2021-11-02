#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
from scipy.stats import boxcox


# In[2]:


cruise_ship = pd.read_excel(r'/Users/rubenlarrazolo/Downloads/cruise_ship.xlsx')


# In[3]:


print(cruise_ship)


# In[4]:


pd.options.display.max_columns = None
cruise_ship.head()


# In[5]:


sns.pairplot(cruise_ship)


# # Transform Positively Skewed Data

# In[7]:


cruise_ship['TonnageSQRT'] = np.sqrt(cruise_ship['Tonnage'])


# In[8]:


cruise_ship.head()


# In[9]:


cruise_ship.TonnageSQRT.hist()


# In[10]:


cruise_ship['TonnageLOG'] = np.log(cruise_ship['Tonnage'])


# In[11]:


cruise_ship.head()


# In[12]:


cruise_ship.TonnageLOG.hist()


# In[13]:


cruise_ship['CabinsSQRT'] = np.sqrt(cruise_ship['Cabins'])


# In[14]:


cruise_ship.CabinsSQRT.hist()


# In[15]:


cruise_ship['passngrsSQRT'] = np.sqrt(cruise_ship['passngrs'])


# In[17]:


cruise_ship.head()


# In[18]:


cruise_ship.passngrsSQRT.hist()


# In[ ]:




