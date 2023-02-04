#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd


# In[5]:


df = pd.read_csv('vilnius weather.csv')


# In[13]:


df['day'] = pd.to_datetime(df['day'])


# **This is my first app in  Streamlit.**
# 
# The graph below represents daily temperature in Vilnius in January 2023.

# In[22]:


st.write("""
**This is my first app in *Streamlit*!**

The graph below represents daily temperature in Vilnius in January 2023.
""")


st.line_chart(df.groupby(df.day)['temperature'].max())

