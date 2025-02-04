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
    st.write('*The things you own end up owning you*')

with col2:
    st.title('Bhanu Pratap Singh')
    st.write('AI student - Passionate about AI use cases, their implementation in real world scenarios, as well as using data to make informed decisions.')

    if st.button('Contact Me'):
        show_contact()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- Education ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBi, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)