#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd


# In[13]:


from itunes_app_scraper.scraper import AppStoreScraper


# In[14]:


from app_store_scraper import AppStores
from pprint import pprint


# In[15]:


import datetime as dt
from tzlocal import get_localzone
import random
import time


# In[16]:


app_df = pd.read_csv('//fs-stf-home.hallam.shu.ac.uk/FS-STF-HOME1/7/uu8277/MyWork/Data/apps_ids.csv')


# In[17]:


app_df.head()


# In[18]:


app_names = list(app_df['iOS_app_name'])
app_ids = list(app_df['iOS_app_id'])


# In[19]:


scraper = AppStoreScraper()
app_store_list = list(scraper.get_multiple_app_details(app_ids))


# In[20]:


pprint(app_store_list[0])


# In[23]:


app_info_df = pd.DataFrame(app_store_list)
app_info_df.to_csv('//fs-stf-home.hallam.shu.ac.uk/FS-STF-HOME1/7/uu8277/MyWork/Data/apps_ids.csv', index=False)
app_info_df.head()


# In[24]:


my_app = AppStore(
  country='GB',        # required, 2-letter code
  app_name='bank-of-scotland-mobile-bank', # required, found in app's url
  app_id=485728109   # technically not required, found in app's url
)


# In[25]:


my_app.review(
  how_many=3500)


# In[26]:


my_app.reviews


# In[27]:


import numpy as np

import json


# In[28]:



df = pd.DataFrame(np.array(my_app.reviews),columns=['review'])

df2 = df.join(pd.DataFrame(df.pop('review').tolist()))

df2.head()


# In[29]:


df2


# In[30]:


df2.to_csv('C:/Users/uu8277/Desktop/Data/App Store Review BankofScotland.csv')


# In[ ]:




