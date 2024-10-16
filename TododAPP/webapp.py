import streamlit as st

import functions

st.title('Todo App')
st.subheader('For personal use')
st.write('Jotdown everything you need to do now')

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Enter to do....')


