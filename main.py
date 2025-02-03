import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import os 

st.image(os.path.join(os.getcwd(), 'static', 'bhanu-photo.jpeg'), width=200, caption='Bhanu Pratap Singh')

st.divider()

st.title('My first streamlit app')
st.header('I am bhanu')
st.subheader('I am a data scientist')
#st.markdown('## This is a markdown')
#st.caption('This is a caption')
p1 = st.write('Hello World')
pressed = st.button('Button')

st.divider()