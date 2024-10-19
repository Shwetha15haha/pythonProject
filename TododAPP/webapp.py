import streamlit as st

import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title('Todo App')
st.subheader('For personal use')
st.write('Jot down everything you need to do now')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Enter to do....', on_change=add_todo, key='new_todo')
