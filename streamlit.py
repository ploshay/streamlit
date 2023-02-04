#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd


# In[4]:


st.write("""
#my first app
Hello *world!*
""")

df = pd.read_csv('vilnius weather.csv')
st.line_chart(df)

