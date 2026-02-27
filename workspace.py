import streamlit as st

def show():

    st.set_page_config(layout="wide")

    if "tab" not in st.session_state:
        st.session_state.tab = "Papers"

    # ------------------ CSS ------------------
    st.markdown("""
    <style>

    .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    body {
        background-color: #f6f7fb;
    }

    .back {
        color: #6a11cb;
        font-size: 14px;
        cursor: pointer;
    }

    .title {
        font-size: 26px;
        font-weight: 700;
    }

    .subtitle {
        color: #666;
        font-size: 14px;
        margin-bottom: 20px;
    }

    .tabs {
        display: flex;
        gap: 25px;
        margin-bottom: 20px;
        font-weight: 500;
    }

    .tab-active {
        color: #6a11cb;
        border-bottom: 2px solid #6a11cb;
        padding-bottom: 5px;
    }

    .tab-inactive {
        color: #777;
        cursor: pointer;
    }

    .paper-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    .paper-title {
        font-weight: 600;
        margin-bottom: 5px;
    }

    .paper-authors {
        font-size: 13px;
        color: #777;
    }

    .paper-abstract {
        font-size: 14px;
        color: #555;
        margin-top: 10px;
    }

    .view-link {
        color: #6a11cb;
        font-size: 13px;
        margin-top: 10px;
        display: inline-block;
    }

    .chat-box {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
        height: 400px;
        overflow-y: auto;
        margin-bottom: 15px;
    }

    .user-msg {
        background: #8e2de2;
        color: white;
        padding: 8px 14px;
        border-radius: 15px;
        width: fit-content;
        margin-left: auto;
        margin-bottom: 10px;
    }

    .ai-msg {
        background: #f1f1f1;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 70%;
    }

    </style>
    """, unsafe_allow_html=True)

    # ------------------ HEADER ------------------
    st.markdown('<div class="back">← Back to Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">My Workspace</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">2 papers / 0 selected</div>', unsafe_allow_html=True)

    # ------------------ TABS ------------------
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        if st.button("Papers (2)"):
            st.session_state.tab = "Papers"

    with col2:
        if st.button("AI Chat"):
            st.session_state.tab = "AI Chat"

    with col3:
        if st.button("Generate Review"):
            st.session_state.tab = "Review"

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------ PAPERS TAB ------------------
    if st.session_state.tab == "Papers":

        papers = [
            {
                "title": "AI Agents and Agentic AI-Navigating a Plethora of Concepts for Future Manufacturing",
                "authors": "Yinang Ren, Yuyang Liu, Yang & Xing Xiu",
                "abstract": "AI agents are autonomous systems designed to perceive, reason, and act within dynamic environments..."
            },
            {
                "title": "Responsible AI Agents",
                "authors": "Deven R. Desai, Mark R. Riedl",
                "abstract": "Thanks to advances in large language models, a new type of software agent has entered the marketplace..."
            }
        ]

        for paper in papers:
            st.markdown(f"""
            <div class="paper-card">
                <div class="paper-title">{paper['title']}</div>
                <div class="paper-authors">{paper['authors']}</div>
                <div class="paper-abstract">{paper['abstract']}</div>
                <div class="view-link">View Paper →</div>
            </div>
            """, unsafe_allow_html=True)

    # ------------------ AI CHAT TAB ------------------
    elif st.session_state.tab == "AI Chat":

        st.markdown("### AI Research Assistant")
        st.markdown('<div class="subtitle">2 papers selected · Ask anything!</div>', unsafe_allow_html=True)

        st.markdown('<div class="chat-box">', unsafe_allow_html=True)

        st.markdown('<div class="user-msg">what are the key difference in both</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="ai-msg">
        The two research papers/articles discuss AI agents and their potential applications,
        but they have distinct focuses and approaches...
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([6,1])
        with col1:
            st.text_input("", placeholder="Ask about the selected papers...")
        with col2:
            st.button("Send")

    # ------------------ REVIEW TAB ------------------
    elif st.session_state.tab == "Review":
        st.markdown("### Generate Literature Review")
        st.write("AI-generated literature review will appear here.")