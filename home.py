import streamlit as st

def show():

    st.set_page_config(layout="wide")

    # -------- CUSTOM CSS --------
    st.markdown("""
    <style>

    .block-container {
        padding-top: 2rem;
        padding-left: 4rem;
        padding-right: 4rem;
    }

    body {
        background-color: #f6f7fb;
    }

    /* Section Title */
    .section-title {
        text-align: center;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 50px;
    }

    /* Feature Cards */
    .feature-box {
        text-align: center;
        padding: 20px;
    }

    .feature-icon {
        background: #ede9fe;
        color: #6a11cb;
        font-size: 24px;
        padding: 15px;
        border-radius: 50%;
        display: inline-block;
        margin-bottom: 15px;
    }

    .feature-title {
        font-weight: 600;
        margin-bottom: 10px;
    }

    .feature-desc {
        font-size: 14px;
        color: #666;
    }

    /* Purple Gradient Section */
    .why-section {
        margin-top: 70px;
        background: linear-gradient(90deg, #6a11cb, #8e2de2);
        padding: 60px 40px;
        border-radius: 12px;
        color: white;
        text-align: center;
    }

    .why-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 30px;
    }

    .why-list {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 40px;
        font-size: 15px;
    }

    .why-item {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    </style>
    """, unsafe_allow_html=True)

    # -------- FEATURES SECTION --------
    st.markdown('<div class="section-title">Powerful Features for Modern Research</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🔍</div>
            <div class="feature-title">Smart Paper Search</div>
            <div class="feature-desc">
            Find research papers across multiple databases with AI-powered search
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">💬</div>
            <div class="feature-title">AI Chat Assistant</div>
            <div class="feature-desc">
            Ask questions about your research papers and get intelligent responses
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📄</div>
            <div class="feature-title">DocSpace Editor</div>
            <div class="feature-desc">
            Create and edit documents with rich text formatting like Google Docs
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📖</div>
            <div class="feature-title">Literature Review</div>
            <div class="feature-desc">
            Generate comprehensive literature reviews from selected papers
            </div>
        </div>
        """, unsafe_allow_html=True)

    # -------- WHY CHOOSE SECTION --------
    st.markdown("""
    <div class="why-section">
        <div class="why-title">Why Choose ResearchHub AI?</div>
        <div class="why-list">
            <div class="why-item">✔ Save 80% time on literature review</div>
            <div class="why-item">✔ Access millions of research papers</div>
            <div class="why-item">✔ AI-powered insights and summaries</div>
            <div class="why-item">✔ Collaborative workspace features</div>
            <div class="why-item">✔ Export to multiple formats</div>
        </div>
    </div>
    """, unsafe_allow_html=True)