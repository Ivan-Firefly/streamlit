import streamlit as st

st.title('ECHO')

def func():
    echo= input("Type something:")
    if echo != '':
        returnt print('You typed:'+echo)
    else:
        returnt print('Input string is empty')

st.write(func)

