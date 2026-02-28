import streamlit as st
from streamlit_quill import st_quill
from datetime import datetime

def show():

    # ---------------- CSS ----------------
    st.markdown("""
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    body {
        background-color: #f5f7fb;
    }

    .editor-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    .stButton>button {
        border-radius: 8px;
        font-weight: 500;
        padding: 8px 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- Session Storage ----------------
    if "documents" not in st.session_state:
        st.session_state.documents = {
            "rk": {"content": "", "date": "10/30/2025"},
            "agentic ai": {"content": "<h2>HELLO EVERYONE</h2>", "date": "11/2/2025"}
        }

    if "current_doc" not in st.session_state:
        st.session_state.current_doc = "agentic ai"

    if "rename_mode" not in st.session_state:
        st.session_state.rename_mode = False

    # ---------------- Layout ----------------
    col1, col2 = st.columns([1, 3])

    # -------- LEFT PANEL --------
    with col1:

        if st.button("+ New Document", use_container_width=True):
            new_name = f"Untitled {len(st.session_state.documents)+1}"
            st.session_state.documents[new_name] = {
                "content": "",
                "date": datetime.now().strftime("%m/%d/%Y")
            }
            st.session_state.current_doc = new_name
            st.rerun()

        st.markdown("### Documents")

        for doc in st.session_state.documents:
            if st.button(doc, use_container_width=True):
                st.session_state.current_doc = doc
                st.session_state.rename_mode = False
                st.rerun()

    # -------- RIGHT PANEL --------
    with col2:

        current_doc = st.session_state.current_doc

        colA, colB, colC, colD = st.columns([5,1,1,1])

        # Document Title / Rename
        with colA:
            if st.session_state.rename_mode:
                new_name = st.text_input("Rename Document", value=current_doc)

                if st.button("✅ Confirm Rename"):
                    if new_name and new_name not in st.session_state.documents:
                        st.session_state.documents[new_name] = \
                            st.session_state.documents.pop(current_doc)
                        st.session_state.current_doc = new_name
                        st.session_state.rename_mode = False
                        st.success("Renamed Successfully!")
                        st.rerun()
                    else:
                        st.error("Invalid or duplicate name")

            else:
                st.subheader(current_doc)

        # Rename Button
        with colB:
            if st.button("✏ Rename"):
                st.session_state.rename_mode = True
                st.rerun()

        # Save Button
        with colC:
            if st.button("💾 Save"):
                st.success("Document Saved!")

        # Download Button
        with colD:
            st.download_button(
                "⬇ Download",
                st.session_state.documents[current_doc]["content"],
                file_name=f"{current_doc}.html"
            )

        # Editor
        st.markdown('<div class="editor-card">', unsafe_allow_html=True)

        content = st_quill(
            value=st.session_state.documents[current_doc]["content"],
            html=True,
            key=current_doc
        )

        st.session_state.documents[current_doc]["content"] = content

        st.markdown('</div>', unsafe_allow_html=True)
