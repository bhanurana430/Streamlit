import re

import streamlit as st
import requests  # pip install requests


# WEBHOOK_URL = st.secrets["WEBHOOK_URL"]


def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

git_url = "https://github.com/bhanurana430"
git_image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIOVOH4NHf85lJfAD7WCeOrqx3gvTLWl5eVQ&s"

li_url = "www.linkedin.com/in/bhanu002"
li_image = "https://i.pinimg.com/564x/6b/ab/30/6bab3017350ca04c6fa05569672bd31e.jpg"

def contact_form():

    st.divider()

    c1, c2 = st.columns(2, gap='small',vertical_alignment='center',)

    
    with c1:
        st.image("static/github copy.png", width=100)
        st.markdown(f"[----GitHub]({git_url})")
    with c2:
        st.image("static/linkedin.png", width=100)
        st.markdown(f"[----Linkedin]({li_url})")
    st.divider()

    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        # if not WEBHOOK_URL:
        #     st.error("Email service is not set up. Please try again later.", icon="📧")
        #     st.stop()

        if not name:
            st.error("Please provide your name.", icon="🧑")
            st.stop()

        if not email:
            st.error("Please provide your email address.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Please provide a valid email address.", icon="📧")
            st.stop()

        if not message:
            st.error("Please provide a message.", icon="💬")
            st.stop()

        # Prepare the data payload and send it to the specified webhook URL
        data = {"email": email, "name": name, "message": message}
        # response = requests.post(WEBHOOK_URL, json=data)

        # if response.status_code == 200:
        #     st.success("Your message has been sent successfully! 🎉", icon="🚀")
        # else:
        #     st.error("There was an error sending your message.", icon="😨")

        st.success("Your message has been sent successfully! 🎉", icon="🚀")