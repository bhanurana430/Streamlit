import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        /* Sticky Navbar */
        .navbar {
            position: fixed;
            top: 0;
            width: 100%;
            background-color: #0d6efd;
            padding: 10px 0;
            z-index: 1000;
            text-align: center;
        }
        .navbar a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
        }
        .navbar a:hover {
            background-color: #0056b3;
            border-radius: 5px;
        }
        /* Smooth scrolling */
        html {
            scroll-behavior: smooth;
        }
        /* Adjust sections */
        .section {
            padding: 100px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
    <div class="navbar">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#skills">Skills</a>
        <a href="#contact">Contact</a>
    </div>
""", unsafe_allow_html=True)

# Spacing to push content below navbar
st.markdown("<br><br><br>", unsafe_allow_html=True)

# Home Section
st.markdown('<h2 id="home">🏠 Home</h2>', unsafe_allow_html=True)
st.write("Welcome to my personal portfolio! Here, you'll find details about my projects, skills, and contact information.")

# About Section
st.markdown('<h2 id="about">🧑 About Me</h2>', unsafe_allow_html=True)
st.write("I'm a passionate AI and Data Science student, building innovative solutions.")

# Projects Section
st.markdown('<h2 id="projects">🚀 Projects</h2>', unsafe_allow_html=True)
projects = [
    {"name": "AI Chatbot", "desc": "An AI-powered chatbot using NLP."},
    {"name": "Stock Price Predictor", "desc": "A machine learning model to predict stock prices."},
    {"name": "Portfolio Website", "desc": "This portfolio, built using Streamlit!"}
]
for project in projects:
    st.write(f"**{project['name']}** - {project['desc']}")

# Skills Section
st.markdown('<h2 id="skills">🛠 Skills</h2>', unsafe_allow_html=True)
st.write("- Python, SQL, Machine Learning, Data Analysis")
st.write("- TensorFlow, PyTorch, Scikit-Learn")
st.write("- Streamlit, Flask, FastAPI")

# Contact Section
st.markdown('<h2 id="contact">📬 Contact</h2>', unsafe_allow_html=True)
st.write("📧 Email: [your.email@example.com](mailto:your.email@example.com)")
st.write("🔗 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)")
st.write("🐦 Twitter: [twitter.com/yourhandle](https://twitter.com/yourhandle)")

# Footer
st.markdown("<br><br><hr><center>Made with ❤️ in Streamlit</center>", unsafe_allow_html=True)
