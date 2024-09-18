import streamlit as st



def func():
    echo= input("Type something:")
    if echo != '':
        print('You typed:'+echo)
    else:
        print('Input string is empty')

st.write(func)

