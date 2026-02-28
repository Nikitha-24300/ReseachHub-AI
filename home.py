import streamlit as st

def show():

    st.title("🏠 ResearchHub AI")

    st.markdown("### Powerful Features for Modern Research")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("#### 🔍 Smart Paper Search")
        if st.button("Explore Search"):
            st.session_state.page = "🔎 Search Papers"
            st.rerun()

    with col2:
        st.markdown("#### 💬 AI Chat Assistant")
        if st.button("Open AI Tools"):
            st.session_state.page = "🤖 AI Tools"
            st.rerun()

    with col3:
        st.markdown("#### 📤 Upload PDF")
        if st.button("Upload Now"):
            st.session_state.page = "📤 Upload PDF"
            st.rerun()

    with col4:
        st.markdown("#### 📁 DocSpace")
        if st.button("Open DocSpace"):
            st.session_state.page = "📁 DocSpace"
            st.rerun()

    st.markdown("---")

    st.markdown("### Why Choose ResearchHub AI?")
    st.write("✔ Save 80% time on literature review")
    st.write("✔ AI-powered summaries")
    st.write("✔ Collaborative workspace")
    st.write("✔ Export in multiple formats")
