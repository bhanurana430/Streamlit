import streamlit as st

#page setup

landing = st.Page(
    page = 'views/landing.py',
    title = 'Home',
    icon = '🏠',
    default = True
)


projects = st.Page(
    page = 'views/projects.py',
    title = 'Projects',
    icon = '🔨'
)


#Navigation

# st.sidebar.title('Navigation')
st.sidebar.text('Made by Bhanu <3')

pg = st.navigation(
    {
        'Info': [landing],
        'Projects': [projects]
    }
)

# st.logo('static/bhanu-photo.jpeg')

#Run Navigation

pg.run()