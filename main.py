import streamlit as st

#page setup

landing = st.Page(
    page = 'views/landing.py',
    title = 'Home',
    icon = '',
    default = True
)


projects = st.Page(
    page = 'views/projects.py',
    title = 'Projects',
    icon = ''
)

blogs = st.Page(
    page = 'views/blogs.py',
    title = 'Blogs',
    icon = ''
)


#Navigation

# st.sidebar.title('Navigation')
st.sidebar.text('Made by Bhanu <3')

pg = st.navigation([landing, projects, blogs])

# st.logo('static/bhanu-photo.jpeg')

#Run Navigation

pg.run()