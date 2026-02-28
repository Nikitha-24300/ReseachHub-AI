import streamlit as st

def show():

    st.set_page_config(layout="wide")

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

    .title {
        font-size: 26px;
        font-weight: 700;
    }

    .subtitle {
        color: #666;
        margin-bottom: 25px;
    }

    .card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }

    .paper-select {
        background: #f3f0ff;
        border: 1px solid #d6ccff;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 10px;
    }

    .tool-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
        text-align: center;
    }

    .btn-blue {
        background: #2563eb;
        color: white;
        padding: 8px 16px;
        border-radius: 6px;
        display: inline-block;
        margin-top: 10px;
    }

    .btn-orange {
        background: #d97706;
        color: white;
        padding: 8px 16px;
        border-radius: 6px;
        display: inline-block;
        margin-top: 10px;
    }

    .btn-green {
        background: #16a34a;
        color: white;
        padding: 8px 16px;
        border-radius: 6px;
        display: inline-block;
        margin-top: 10px;
    }

    .result-header {
        font-weight: 600;
        margin-bottom: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .download-btn {
        background: #374151;
        color: white;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 13px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ------------------ HEADER ------------------
    st.markdown('<div class="title">AI Tools</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-powered research analysis tools • 2 papers available • 2 selected</div>', unsafe_allow_html=True)

    # ------------------ PAPER SELECTION ------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Select Papers for Analysis")

    st.markdown('<div class="paper-select">✔ AI Agents and Agentic AI - Navigating Concepts</div>', unsafe_allow_html=True)
    st.markdown('<div class="paper-select">✔ Responsible AI Agents</div>', unsafe_allow_html=True)

    st.markdown("2 papers selected")
    st.markdown('</div>', unsafe_allow_html=True)

    # ------------------ TOOL CARDS ------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="tool-card">
            <h4>AI Summaries</h4>
            <p>Generate concise summaries of selected research papers</p>
            <div class="btn-blue">▶ Generate Summaries</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="tool-card">
            <h4>Key Insights</h4>
            <p>Extract key insights and trends from research papers</p>
            <div class="btn-orange">★ Extract Insights</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="tool-card">
            <h4>Literature Review</h4>
            <p>Generate comprehensive literature reviews automatically</p>
            <div class="btn-green">📄 Generate Review</div>
        </div>
        """, unsafe_allow_html=True)

    # ------------------ AI SUMMARIES RESULTS ------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="result-header"><span>AI Summaries Results</span><span class="download-btn">⬇ Download</span></div>', unsafe_allow_html=True)

    st.markdown("""
    **AI Agents and Agentic AI**

    This paper explores advancements in AI agents, LLM agents, and Agentic AI...

    ---
    **Responsible AI Agents**

    This paper discusses ethical concerns and value alignment in AI agents...
    """)

    st.markdown('</div>', unsafe_allow_html=True)

    # ------------------ KEY INSIGHTS RESULTS ------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="result-header"><span>Key Insights Results</span><span class="download-btn">⬇ Download</span></div>', unsafe_allow_html=True)

    st.markdown("""
    **Key Insights:**
    1. Rapid advancements in LLM agents.
    2. Agentic AI enables goal-directed autonomy.
    3. Responsible AI emphasizes value alignment.
    4. Human responsibility remains critical.

    **Trends:**
    - Increased focus on multimodal AI systems.
    - Growing attention to ethical deployment.
    """)

    st.markdown('</div>', unsafe_allow_html=True)

    # ------------------ LITERATURE REVIEW RESULTS ------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="result-header"><span>Literature Review Results</span><span class="download-btn">⬇ Download</span></div>', unsafe_allow_html=True)

    st.markdown("""
    **Comprehensive Literature Review: AI Agents and Responsible AI Agents**

    The research explores AI agents and Agentic AI developments, covering LLM-based systems, 
    multimodal capabilities, and autonomous decision-making. It also discusses risks and 
    value-alignment strategies necessary for safe deployment.
    """)

    st.markdown('</div>', unsafe_allow_html=True)
