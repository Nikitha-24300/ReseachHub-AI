import streamlit as st
import dashboard
import searchpapers
import uploadpdf
import Atools
import home
import workspace
import docspace
st.set_page_config(layout="wide")

# ------------------ SESSION ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>

/* Hide default radio circle */
div[role="radiogroup"] > label > div:first-child {
    display: none;
}

/* Sidebar background */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    padding-top: 20px;
    border-right: 1px solid #eee;
}

/* Sidebar Title */
.sidebar-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 5px;
}

.sidebar-subtitle {
    font-size: 14px;
    color: gray;
    margin-bottom: 15px;
}

/* Menu items */
div[role="radiogroup"] label {
    padding: 12px 15px !important;
    border-radius: 8px;
    margin-bottom: 6px;
    font-weight: 500;
    color: #444;
}

/* Hover effect */
div[role="radiogroup"] label:hover {
    background-color: #f3f0ff;
    color: #6a11cb;
}

/* Selected item */
div[role="radiogroup"] input:checked + div {
    background-color: #ede9fe;
    color: #6a11cb;
    font-weight: 600;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.markdown('<div class="sidebar-title">🔬 ResearchHub AI</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-subtitle">Navigation</div>', unsafe_allow_html=True)

menu = [
    "🏠 Home",
    "📊 Dashboard",
    "🔎 Search Papers",
    " workspace",
    "🤖 AI Tools",
    "📤 Upload PDF",
    "📁 DocSpace"
]

choice = st.sidebar.radio("", menu, label_visibility="collapsed")

st.session_state.page = choice

# ------------------ ROUTING ------------------
if choice == "🏠 Home":
    home.show()

elif choice == "📊 Dashboard":
    dashboard.show()

elif choice == "🔎 Search Papers":
    searchpapers.show()
elif choice==" workspace":
    workspace.show()

elif choice == "🤖 AI Tools":
    Atools.show()

elif choice == "📤 Upload PDF":
    uploadpdf.show()

elif choice == "📁 DocSpace":
    docspace.show()