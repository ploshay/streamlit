#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd


# In[5]:


df = pd.read_csv('vilnius weather.csv')


# In[13]:


df['day'] = pd.to_datetime(df['day'])


# In[21]:


st.write("""
#my first app
Hello *world!*
""")


st.line_chart(df.groupby(df.day)['temperature'].max())

