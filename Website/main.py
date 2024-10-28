import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg')

with col2:
    st.title('Shwetha Moghe')
    content = """
    Hi I'm Shwetha from India. \n
    
    A data enthusiast who loves to read, code, and learn. 
    With a little over a year of experience,I'm passionate about turning data into simple, impactful insights.
    """
    st.info(content)