#!/usr/bin/env python
# coding: utf-8

# In[1]:


3#. import streamlit as st
st.header("celcius to farenheit")
st.write("temp conversion")
c = st.number_input("input the temp in celcius ")
st.write("temp in farenheit is ",(c*9/5)+32)


# In[2]:


# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles'%(kilometers,miles))
                         


# In[8]:


import streamlit as st
st.header('simple web app')
st.write('*my app*')
radius=st.slider('radius')
st.write( "5.96* 1024. 6.37 * 106m,")
print('volume * radius')


# In[ ]:




