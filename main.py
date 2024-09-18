import streamlit as st

st.title('ECHO')

def func():
    echo= input("Type something:")
    if echo != '':
        return print('You typed:'+echo)
    else:
        return print('Input string is empty')

st.write(func)

