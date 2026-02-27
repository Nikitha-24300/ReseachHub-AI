import streamlit as st

st.title("📊 Dashboard")

st.write("Welcome to your ResearchHub AI dashboard.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Active Workspaces", 3)

with col2:
    st.metric("Imported Papers", 24)

with col3:
    st.metric("AI Conversations", 12)