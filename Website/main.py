import streamlit as st
import pandas as pd

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:11].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        # url1 = row['url']
        # st.page_link(url1, label='Source Code')
        # st.link_button('Source Code', url1)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[11:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        # url2 = row['url']
        # st.page_link(url2, label='Source Code')
        # st.link_button('Source Code', url2)
        st.write(f"[Source Code]({row['url']})")

