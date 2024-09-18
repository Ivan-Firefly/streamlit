import streamlit as st

st.title('ECHO')

def func():
    echo= input("Type something:")
    if echo != '':
        output='You typed:'+echo
    else:
        output='Input string is empty'
    return output

st.write(func())
