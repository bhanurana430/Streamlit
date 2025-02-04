import streamlit as st
from forms.form import contact_form

# st.title('Hi, I am Bhanu')
# st.write('I am a Data Scientist and Machine Learning Engineer')

@st.dialog('Contact Me')
def show_contact():
    contact_form()

#hero section
col1, col2 = st.columns(2, gap='small',vertical_alignment='center')

with col1:
    st.image('static/bhanu-photo.png', width=250)
    st.write('***The things you own end up owning you***')

with col2:
    st.title('Bhanu Pratap Singh')
    st.write('AI student - Passionate about AI use cases, their implementation in real world scenarios, as well as using data to make informed decisions.')

    st.divider()

    b1,b2 = st.columns(2, gap='small',vertical_alignment='center')
    with b1:
        if st.button('Contact Me'):
            show_contact()
    with b2:
        if st.button('Resume'):
            st.write('Resume')

st.divider()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 2+ Years experience with ***python*** programming
    - Strong hands-on experience and knowledge about ***machine learning*** and ***deep learning*** algorithms
    - Good understanding of ***statistical*** principles and their respective applications
    - Currently keen about learning ***Deep Reinforcement Learning*** and ***Time Series*** problems
    """
)

# --- Education ---
st.write("\n")
st.subheader("Education", anchor=False)
st.write(
    """
    - B.SC. Artificial Intelligence, ***Deggendorf University Of Technology***
       - Oct 2022 - Present
       - ***Grade: 2.2*** (German Grading System)
       - During my 5 semesters of study here, I gained a lot of knowledge and experience in basic foundation of computer science, mathematics, machine learning, web development, and data science.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python, SQL, JavaScript - Basic
    - ML/DL/DRL: Scikit-learn, Pytorch, TensorFlow - Keras API, Stable Baselines3, OpenAI Gym etc.
    - Data Visualization: Matplotlib, PowerBI
    - Databases: Postgres
    - Web Development: HTML, CSS, Flask, Streamlit, Basic knowledge of fronted frameworks like React and VueJS
    """
)