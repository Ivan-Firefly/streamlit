import streamlit as st

st.title('ECHO')


echo=st.text_input("Type something:", key="sting")
if echo != '':
    output='You typed:'+echo
else:
    output='Input string is empty'


st.write(output)
