import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('The Best Company')
st.write("""
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of 
type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially 
unchanged.""")

st.subheader('Our Team')

df = pd.read_csv('data.csv')

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image('images/'+row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image('images/'+row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image('images/'+row['image'])



