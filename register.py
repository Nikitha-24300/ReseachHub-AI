import streamlit as st
import requests

API_BASE = "http://localhost:8000"

def show():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📝 Create Account")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        response = requests.post(f"{API_BASE}/register",
                                 json={"name": name, "email": email, "password": password})

        if response.status_code == 200:
            st.success("Account created successfully!")
        else:
            st.error("Registration failed")

    st.markdown('</div>', unsafe_allow_html=True)