import streamlit as st

def show():

    st.set_page_config(layout="wide")

    # ------------------ CUSTOM CSS ------------------
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

    /* Title */
    .page-title {
        font-size: 26px;
        font-weight: 700;
    }

    .subtitle {
        color: #666;
        margin-bottom: 20px;
    }

    /* Search Bar */
    .search-container {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
    }

    .search-button {
        background: linear-gradient(90deg, #6a11cb, #8e2de2);
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: 600;
    }

    /* Result Card */
    .paper-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    .paper-title {
        font-weight: 600;
        font-size: 16px;
        margin-bottom: 5px;
    }

    .paper-authors {
        font-size: 13px;
        color: #777;
        margin-bottom: 10px;
    }

    .paper-abstract {
        font-size: 14px;
        color: #555;
    }

    .tag {
        background-color: #ede9fe;
        color: #6a11cb;
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 12px;
        margin-right: 5px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ------------------ HEADER ------------------
    st.markdown('<div class="page-title">Search Research Papers</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Search across millions of research papers and import them to your workspace</div>', unsafe_allow_html=True)

    # ------------------ SEARCH SECTION ------------------
    col1, col2 = st.columns([6, 1])

    with col1:
        query = st.text_input("", placeholder="🔍 Search papers (e.g., agentic ai)")

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        search_clicked = st.button("Search")

    source = st.selectbox("Source", ["All Sources", "Arxiv", "IEEE", "Springer", "PubMed"])

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------ MOCK RESULTS ------------------
    if query:

        st.markdown("Found 10 papers")

        papers = [
            {
                "title": "AI Agents and Agentic AI: Navigating a Plethora of Concepts for Future Manufacturing",
                "authors": "Yinang Ren, Yuyang Liu, Yang & Xing Xiu",
                "abstract": "AI agents are autonomous systems designed to perceive, reason, and act within dynamic environments. With rapid advancements in generative AI...",
                "tags": ["AI", "Agents", "Manufacturing"]
            },
            {
                "title": "Responsible AI Agents",
                "authors": "Deven R Desai, Mark Riedl",
                "abstract": "Thanks to advances in large language models, a new type of software agent, the artificial intelligence (AI) agent, has entered the marketplace...",
                "tags": ["Responsible AI", "Ethics"]
            }
        ]

        for paper in papers:
            st.markdown(f"""
            <div class="paper-card">
                <div class="paper-title">{paper['title']}</div>
                <div class="paper-authors">{paper['authors']}</div>
                <div class="paper-abstract">{paper['abstract']}</div>
                <div style="margin-top:10px;">
                    {"".join([f'<span class="tag">{tag}</span>' for tag in paper['tags']])}
                </div>
            </div>
            """, unsafe_allow_html=True)