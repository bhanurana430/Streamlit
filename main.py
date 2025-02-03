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

'This is a way to enter code nicely'

code = '''
# This is a code block
def hello():
    print("Hello, Streamlit!")
'''
st.code(code, language='python')

st.divider()

st.header('Dataframe')

btc = yf.download(tickers='BTC-USD', period='1d', interval='1m')

st.dataframe(btc)

st.divider()

'Editable dataframe'

df = pd.DataFrame({'Aadi': [1, 2, 3], 'Bhanu': [4, 5, 6]})

edit_df = st.data_editor(df)