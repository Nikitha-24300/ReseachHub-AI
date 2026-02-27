import streamlit as st

def load_css():
    st.markdown("""
        <style>
        .main {
            background-color: #f4f7fb;
        }
        .header {
            background: linear-gradient(90deg, #1e3c72, #2a5298);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }
        .feature-box {
            background: linear-gradient(135deg, #667eea, #764ba2);
            padding: 15px;
            border-radius: 10px;
            color: white;
            text-align: center;
        }
        .success-box {
            background: #d4edda;
            padding: 10px;
            border-radius: 8px;
            color: #155724;
        }
        </style>
    """, unsafe_allow_html=True)