import streamlit as st
import requests

API_BASE = "http://localhost:8000"

def show():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔐 User Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post(f"{API_BASE}/login",
                                 json={"email": email, "password": password})

        if response.status_code == 200:
            st.session_state.token = response.json()["access_token"]
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

    st.markdown('</div>', unsafe_allow_html=True)