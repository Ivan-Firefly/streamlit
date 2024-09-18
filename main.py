import streamlit as st


@st.cache_data
def func():
    echo= input("Type something:")

if echo != '':
    print('You typed:'+echo)
else:
    print('Input string is empty')

