import streamlit as st
import send_email

# GUI layout
st.set_page_config(layout='centered')
st.title("Contact me")
st.write("Feel free to send me a message. I'd be happy to hear from you at any time.")

# contact form
with st.form(key='email'):
    user = st.text_input("Your name").title()
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    message = f"""\
Subject: Portfolio contact form submission

New message from {user}

Message:
{message}

{user}'s email: {user_email}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email.send_email(message)
        st.info("Email sent. I'll get in touch with you soon.")