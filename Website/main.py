# Import packages
import streamlit as st
import pandas as pd

# Create layout of 2 columns for introduction
col1, col2 = st.columns(2)

# Add content to the first column
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
# Add content to the second column
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

# Create column layout for project details
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# Create dataframe using pandas
df = pd.read_csv('data.csv', sep=';')

# Add content to column by iterating over df
with col3:
    for index, row in df[:11].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        # url1 = row['url']
        # st.page_link(url1, label='Source Code')
        # st.link_button('Source Code', url1)
        st.write(f"[Source Code]({row['url']})")

# Add content to column by iterating over df
with col4:
    for index, row in df[11:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        # url2 = row['url']
        # st.page_link(url2, label='Source Code')
        # st.link_button('Source Code', url2)
        st.write(f"[Source Code]({row['url']})")
