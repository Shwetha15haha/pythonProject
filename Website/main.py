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

col3, col4 = st.columns(2)

with col3:
    st.title('App1')
    st.write('Descrition')
    st.image('images/1.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App3')
    st.write('Descrition')
    st.image('images/3.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App5')
    st.write('Descrition')
    st.image('images/5.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App7')
    st.write('Descrition')
    st.image('images/7.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App9')
    st.write('Descrition')
    st.image('images/9.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App11')
    st.write('Descrition')
    st.image('images/11.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App13')
    st.write('Descrition')
    st.image('images/13.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App15')
    st.write('Descrition')
    st.image('images/15.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App17')
    st.write('Descrition')
    st.image('images/17.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App19')
    st.write('Descrition')
    st.image('images/19.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

with col4:
    st.title('App2')
    st.write('Descrition')
    st.image('images/2.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App4')
    st.write('Descrition')
    st.image('images/4.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App6')
    st.write('Descrition')
    st.image('images/6.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App8')
    st.write('Descrition')
    st.image('images/8.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App10')
    st.write('Descrition')
    st.image('images/10.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App12')
    st.write('Descrition')
    st.image('images/12.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App14')
    st.write('Descrition')
    st.image('images/14.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App16')
    st.write('Descrition')
    st.image('images/16.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App18')
    st.write('Descrition')
    st.image('images/18.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")

    st.title('App20')
    st.write('Descrition')
    st.image('images/20.png')
    url = 'https://github.com/Shwetha15haha/pythonProject/blob/master/TodoWebApp/web.py'
    st.link_button('App code', url, type="secondary")
