import streamlit as st
from backend.utils import extract_text_from_pdf, save_project

def render():
    st.header("Admin Panel")
    uploaded_file = st.file_uploader("Upload Project Brochure", type=["pdf"])
    if uploaded_file:
        text = extract_text_from_pdf(uploaded_file)
        st.text_area("Extracted Text", text, height=300)
        if st.button("Save Project"):
            save_project(uploaded_file.name, text)
            st.success("Project Saved")
