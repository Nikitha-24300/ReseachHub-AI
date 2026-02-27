import streamlit as st
from pypdf import PdfReader

def show():

    st.set_page_config(layout="wide")

    # -------------------- CUSTOM CSS --------------------
    st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
        padding-left: 4rem;
        padding-right: 4rem;
    }

    body {
        background-color: #f5f7fb;
    }

    .page-header {
        font-size: 28px;
        font-weight: 700;
    }

    .subtext {
        color: #6b7280;
        margin-bottom: 30px;
    }

    .upload-container {
        border: 2px dashed #d1d5db;
        border-radius: 12px;
        padding: 60px;
        text-align: center;
        background: #fafafa;
        margin-bottom: 25px;
    }

    .file-success {
        background: #e6f4ea;
        padding: 12px;
        border-radius: 8px;
        margin-top: 15px;
        color: #15803d;
        font-weight: 500;
    }

    .result-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-top: 25px;
    }

    .stButton>button {
        border-radius: 8px;
        font-weight: 500;
        padding: 10px 18px;
    }

    div[data-testid="stDownloadButton"] > button {
        border-radius: 8px;
        font-weight: 500;
        padding: 10px 18px;
    }

    </style>
    """, unsafe_allow_html=True)

    # -------------------- HEADER --------------------
    st.markdown('<div class="page-header">Upload Research Paper</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtext">Upload a PDF to extract text and generate AI insights</div>', unsafe_allow_html=True)

    # -------------------- UPLOAD SECTION --------------------
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        label_visibility="collapsed"
    )

    st.markdown("Drop your PDF file here or click to browse")

    st.markdown('</div>', unsafe_allow_html=True)

    # -------------------- FILE PROCESSING --------------------
    if uploaded_file:

        st.markdown(
            f'<div class="file-success">📄 {uploaded_file.name} ✓</div>',
            unsafe_allow_html=True
        )

        extracted_text = ""

        try:
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"
        except:
            st.error("Unable to read PDF file.")
            st.stop()

        # -------------------- ACTION BUTTONS --------------------
        col1, col2, col3 = st.columns([1,1,1])

        with col1:
            if st.button("⚡ Generate AI Summary", use_container_width=True):
                st.session_state.summary = extracted_text[:1500] + "..."

        with col2:
            st.button("💾 Save to Workspace", use_container_width=True)

        with col3:
            st.download_button(
                "⬇ Download Text",
                extracted_text,
                file_name="extracted_text.txt",
                use_container_width=True
            )

        # -------------------- EXTRACTED TEXT --------------------
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.subheader("Extracted Text:")
        st.text_area("", extracted_text, height=300)
        st.markdown('</div>', unsafe_allow_html=True)

        # -------------------- SUMMARY RESULT --------------------
        if "summary" in st.session_state:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.subheader("AI Summary:")
            st.write(st.session_state.summary)
            st.markdown('</div>', unsafe_allow_html=True)