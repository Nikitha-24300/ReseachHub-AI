import streamlit as st

st.title("📄 Upload Research Paper")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")