import streamlit as st

import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo)
    functions.write_todos(todos)


st.title('Todo App')
st.subheader('For personal use')
st.write('Jot down everything you need to do now')


for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Enter to do....', on_change=add_todo, key='new_todo')
