import streamlit as st
from datetime import datetime

def show():

    # ------------------ INIT SESSION ------------------
    if "workspaces" not in st.session_state:
        st.session_state.workspaces = []

    if "papers_imported" not in st.session_state:
        st.session_state.papers_imported = 0

    if "selected_workspace" not in st.session_state:
        st.session_state.selected_workspace = None

    # ------------------ HEADER ------------------
    st.title("📊 Dashboard")
    st.caption("Manage your research workspaces")

    total_workspaces = len(st.session_state.workspaces)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Workspaces", total_workspaces)
    col2.metric("Papers Imported", st.session_state.papers_imported)

    # 🔥 QUICK ACTION
    if col3.button("🔎 Go To Search Papers"):
        st.session_state.page = "🔎 Search Papers"
        st.rerun()

    st.divider()

    # ------------------ CREATE WORKSPACE ------------------
    with st.expander("➕ Create New Workspace"):

        ws_name = st.text_input("Workspace Name")
        ws_desc = st.text_area("Description")

        if st.button("Create Workspace"):
            if ws_name:
                st.session_state.workspaces.append({
                    "name": ws_name,
                    "description": ws_desc,
                    "date": datetime.now().strftime("%d/%m/%Y"),
                    "papers": []
                })
                st.success("Workspace Created!")
                st.rerun()
            else:
                st.warning("Workspace name required")

    st.divider()

    # ------------------ IMPORT PAPER ------------------
    if total_workspaces > 0:

        st.subheader("📥 Import Paper to Workspace")

        workspace_names = [ws["name"] for ws in st.session_state.workspaces]

        selected_ws = st.selectbox("Select Workspace", workspace_names)

        paper_title = st.text_input("Paper Title")
        paper_link = st.text_input("Paper Link")

        if st.button("Import Paper"):

            if paper_title and paper_link:

                for ws in st.session_state.workspaces:
                    if ws["name"] == selected_ws:
                        ws["papers"].append({
                            "title": paper_title,
                            "link": paper_link
                        })

                st.session_state.papers_imported += 1

                st.success("Paper Imported Successfully!")
                st.rerun()

            else:
                st.warning("Enter paper title and link")

    st.divider()

    # ------------------ WORKSPACE LIST ------------------
    if total_workspaces == 0:
        st.info("No workspaces yet.")
        return

    st.subheader("📁 Your Workspaces")

    for ws in st.session_state.workspaces:

        with st.container():
            st.markdown(f"### {ws['name']}")
            st.caption(f"📅 Created {ws['date']}")
            st.write(ws["description"])

            st.write(f"📄 Papers: {len(ws['papers'])}")

            # Show papers
            for paper in ws["papers"]:
                st.markdown(f"- [{paper['title']}]({paper['link']})")

            st.divider()
