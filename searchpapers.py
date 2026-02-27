import streamlit as st
from utils import search_papers

st.title("🔎 Search Research Papers")

query = st.text_input("Enter research topic")

if st.button("Search"):
    res = search_papers(query)
    if res.status_code == 200:
        papers = res.json()["papers"]
        for paper in papers:
            with st.expander(paper["title"]):
                st.write("**Authors:**", ", ".join(paper["authors"]))
                st.write("**Abstract:**", paper["abstract"])
                st.button("Import Paper", key=paper["title"])
    else:
        st.error("Search failed")