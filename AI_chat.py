import streamlit as st
from utils import chat

st.title("🤖 AI Research Assistant")

workspace_id = st.number_input("Workspace ID", min_value=1, value=1)

message = st.text_area("Ask a research question")

if st.button("Ask AI"):
    res = chat(workspace_id, message)
    if res.status_code == 200:
        st.success("AI Response:")
        st.write(res.json()["response"])
    else:
        st.error("Chat failed")