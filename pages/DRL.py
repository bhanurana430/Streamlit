import streamlit as st

st.title("DRL for trading - Detailed View")

st.image("static/project img/DRL.jpg", width=600)  # Replace with actual image URL
st.write("### Detailed Description")
st.write("This is a detailed description of Project 1. It explains the purpose, features, and implementation of the project.")

st.write("### Video Demo")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Replace with actual video URL

st.write("### More Screenshots")
st.image(["https://via.placeholder.com/400", "https://via.placeholder.com/400"], width=300)

if st.button("Back to Projects"):
    st.switch_page("projects.py")  # Adjust this to your main projects page filename
