import streamlit as st

st.header('Contact me for any feedback/message ')

with st.form(key='email_forms'):
    user_email = st.text_input(label='Please enter your email address below:', placeholder='Your email address')
    message = st.text_area(label='Please share any query or feedback below:', placeholder='Your message')
    button = st.form_submit_button()
    if button:
        print(button)
        print("I was pressed")
