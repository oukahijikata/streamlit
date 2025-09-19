import streamlit as st

st.header('st.button')

if st.button('Click me!'):
    st.write('Button clicked!')
else:
    st.write('Button not clicked yet.')

if st.button('Say hello'):
    st.write('clicked! Why hello there')
else:
    st.write('not clicked yet! ')


ouka = st.button('Ouka', help='Click to see a message', icon='🌸')
if ouka:
    st.write('Ouka clicked! 🌸')

st.button('Reset', help='Click to reset the app', type="primary")
