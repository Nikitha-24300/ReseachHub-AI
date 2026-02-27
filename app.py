import streamlit as st
from utils import login, register

st.set_page_config(page_title="ResearchHub AI", layout="wide")

if "token" not in st.session_state:
    st.session_state.token = None

st.title("🧠 ResearchHub AI")
st.subheader("Agentic AI Powered Research Platform")

if st.session_state.token is None:
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            res = login(email, password)
            if res.status_code == 200:
                st.session_state.token = res.json()["access_token"]
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        email_r = st.text_input("Email ", key="reg_email")
        password_r = st.text_input("Password ", type="password", key="reg_pass")

        if st.button("Register"):
            res = register(email_r, password_r)
            if res.status_code == 200:
                st.success("Registration successful. Please login.")
            else:
                st.error("Registration failed.")

else:
    st.sidebar.success("Logged in")
    st.sidebar.button("Logout", on_click=lambda: st.session_state.clear())
    st.write("Use the sidebar to navigate between features.")