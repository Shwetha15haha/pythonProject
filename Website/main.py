import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg')
    st.markdown(
        """
        <style>
        img {
            border: 3px solid #4CAF50;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.title('Shwetha Moghe')
    content = """
    Hi I'm Shwetha from India. \n
    
    A data enthusiast who loves to read, code, and learn. 
    With a little over a year of experience,I'm passionate about turning data into simple, impactful insights.
    """
    st.info(content)

content2 = """
Below you can find details of some basic Python apps built by me"""
st.info(content2)

