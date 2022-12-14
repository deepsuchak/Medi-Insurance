#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


import pickle as pkl


# In[3]:


model=pkl.load(open('insurance.p','rb'))


# In[4]:


st.title('---------- Medical Insurance Cost Prediction ---------')


# In[5]:


age = st.number_input('Age', min_value=1, max_value=100, value=25)
sex = st.number_input('Sex', min_value=0, max_value=1)
bmi = st.number_input('BMI', min_value=10, max_value=50, value=10)
children = st.number_input('Children', min_value=0, max_value=5)
smoker = st.number_input('Smoker', min_value=0, max_value=1)
region_northeast = st.number_input('region_northeast', min_value=0, max_value=1)
region_northwest = st.number_input('region_northwest', min_value=0, max_value=1)
region_southeast = st.number_input('region_southeast', min_value=0, max_value=1)
region_southwest = st.number_input('region_southwest', min_value=0, max_value=1)
output=""
if st.button("Predict"):
    result = model.predict([[age,sex,bmi,children,smoker,region_northeast,
                            region_northwest, region_southeast, region_southwest]])
    st.success ('The output of the above is {}'.format(result))  

