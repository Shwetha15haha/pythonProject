import streamlit as st
from Send_Mail import send_mail

st.header('Contact me for any feedback/message ')

with st.form(key='email_forms'):
    user_email = st.text_input(label='Please enter your email address', placeholder='Your email address')

    option = st.selectbox(
        label="What topic do you want to discuss?", placeholder="Choose an option",
        options = ("Email", "Home phone", "Mobile phone"),
    )

    raw_message = st.text_area(label='Text', placeholder='Your message')
    message = f"""\
Subject:New mail from {user_email}

From : {user_email}
{raw_message}
"""
    button = st.form_submit_button()
    if button:
        send_mail(message)
        st.info('Your email was sent successfully.Thank you for contacting.')

