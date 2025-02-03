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

contact = st.Page(
    page = 'views/contact.py',
    title = 'Contact Us',
    icon = '📞'
)

#Navigation

# st.sidebar.title('Navigation')
st.sidebar.text('Made by Bhanu <3')

pg = st.navigation(pages=[landing, projects, contact])

pg = st.navigation(
    {
        'Info': [landing,contact],
        'Projects': [projects]
    }
)

# st.logo('static/bhanu-photo.jpeg')

#Run Navigation

pg.run()