import streamlit as st

def show():

    st.set_page_config(layout="wide")

    # ------------------ CUSTOM CSS ------------------
    st.markdown("""
    <style>

    body {
        background-color: #f6f7fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    /* Header */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .title {
        font-size: 28px;
        font-weight: 700;
    }

    .subtitle {
        color: #666;
        font-size: 14px;
    }

    .avatar {
        background-color: #8e2de2;
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: 600;
    }

    /* Summary Cards */
    .card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
    }

    .card-title {
        font-size: 14px;
        color: #777;
    }

    .card-value {
        font-size: 24px;
        font-weight: 700;
        margin-top: 5px;
    }

    /* Create Button */
    .create-btn {
        background: linear-gradient(90deg, #6a11cb, #8e2de2);
        color: white;
        padding: 10px 22px;
        border-radius: 8px;
        display: inline-block;
        margin-top: 20px;
        font-weight: 600;
    }

    /* Workspace Cards */
    .workspace-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    .workspace-title {
        font-weight: 600;
        font-size: 16px;
    }

    .workspace-meta {
        font-size: 13px;
        color: #777;
        margin-top: 5px;
    }

    .badge {
        background-color: #ede9fe;
        color: #6a11cb;
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

    # ------------------ HEADER ------------------
    col1, col2 = st.columns([8, 1])

    with col1:
        st.markdown('<div class="title">Dashboard</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Manage your research workspaces</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="avatar">R</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------ SUMMARY CARDS ------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">Total Workspaces</div>
            <div class="card-value">6</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">Papers Imported</div>
            <div class="card-value">0</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-title">Quick Actions</div>
            <div style="color:#6a11cb; margin-top:8px;">🔎 Search Papers</div>
        </div>
        """, unsafe_allow_html=True)

    # ------------------ CREATE BUTTON ------------------
    st.markdown('<div class="create-btn">+ Create New Workspace</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------ WORKSPACE GRID ------------------
    workspaces = [
        ("AI", "No description", "10/24/2025"),
        ("ML", "No description", "10/25/2025"),
        ("MR", "research analysis", "10/29/2025"),
        ("PRAMOD", "", "10/29/2025"),
        ("Project 1", "", "10/29/2025"),
        ("Agentic ai", "", "10/29/2025"),
    ]

    cols = st.columns(3)

    for i, ws in enumerate(workspaces):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="workspace-card">
                <div style="display:flex; justify-content:space-between;">
                    <div class="workspace-title">{ws[0]}</div>
                    <div class="badge">0 papers</div>
                </div>
                <div class="workspace-meta">{ws[1]}</div>
                <div class="workspace-meta">📅 Created {ws[2]}</div>
            </div>
            """, unsafe_allow_html=True)