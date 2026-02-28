import streamlit as st

# -------- IMPORT ALL PAGE FILES --------
import register
import login
import dashboard
import searchpapers
import uploadpdf
import Atools
import home
import workspace
import docspace


# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="ResearchHub AI",
    layout="wide"
)

# -------- SESSION STATE INIT --------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = None

if "token" not in st.session_state:
    st.session_state.token = None

if "page" not in st.session_state:
    if st.session_state.logged_in:
        st.session_state.page = "🏠 Home"
    else:
        st.session_state.page = "Register"


# -------- SIDEBAR HEADER --------
st.sidebar.markdown("## 🔬 ResearchHub AI")

if st.session_state.logged_in:
    st.sidebar.caption(f"Logged in as: {st.session_state.username}")
else:
    st.sidebar.caption("Navigation")


# -------- SIDEBAR MENU --------
if not st.session_state.logged_in:
    menu = ["Register", "Login"]
else:
    menu = [
        "🏠 Home",
        "📊 Dashboard",
        "🔎 Search Papers",
        "🧠 Workspace",
        "🤖 AI Tools",
        "📤 Upload PDF",
        "📁 DocSpace",
        "Logout"
    ]

# Keep radio synced with session page
selected = st.sidebar.radio(
    "",
    menu,
    index=menu.index(st.session_state.page)
    if st.session_state.page in menu else 0
)

# Update session page
st.session_state.page = selected


# -------- ROUTING SYSTEM --------

# ----- NOT LOGGED IN -----
if not st.session_state.logged_in:

    if selected == "Register":
        register.show()

    elif selected == "Login":
        login.show()


# ----- LOGGED IN -----
else:

    if selected == "🏠 Home":
        home.show()

    elif selected == "📊 Dashboard":
        dashboard.show()

    elif selected == "🔎 Search Papers":
        searchpapers.show()

    elif selected == "🧠 Workspace":
        workspace.show()

    elif selected == "🤖 AI Tools":
        Atools.show()

    elif selected == "📤 Upload PDF":
        uploadpdf.show()

    elif selected == "📁 DocSpace":
        docspace.show()

    elif selected == "Logout":
        st.session_state.clear()
        st.success("Logged out successfully!")
        st.rerun()
