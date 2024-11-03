# Importing required packages
import streamlit as st
import pandas as pd

# Set page layout wide
st.set_page_config(layout='wide')

# Adding initial contents
st.title('The Best Company')
st.write("""
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of 
type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially 
unchanged.""")

st.subheader('Our Team')

# Define dataframe by reading csv file
df = pd.read_csv('data.csv')

# Create 3 columns to add contents
col1, col2, col3 = st.columns(3)

# Add contents to first column by iterating over df
with col1:
    for index, row in df[:4].iterrows():
        # Add first and last name
        st.subheader(f"{row['first name']} {row['last name']}".title())
        # Add role of employee
        st.write(row['role'])
        # Add image of employee
        st.image('images/'+row['image'])

# Add contents to second column by iterating over df
with col2:
    for index, row in df[4:8].iterrows():
        # Add first and last name
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image('images/'+row['image'])

# Add contents to third column by iterating over df
with col3:
    for index, row in df[8:].iterrows():
        # Add first and last name
        st.subheader(f"{row['first name']} {row['last name']}".title())
        # Add role of employee
        st.write(row['role'])
        # Add image of employee
        st.image('images/'+row['image'])



