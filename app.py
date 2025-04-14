import streamlit as st
import os
from resume_utils import extract_text_from_pdf, analyze_resume

# Set Streamlit page layout
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("📄 AI Resume Analyzer")

# Pass the key to the environment so OpenAI can find it (used inside resume_utils)
os.environ["OPENAI_API_KEY"] = st.secrets["openai_api_key"]

# File uploader UI
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.subheader("Resume Content:")
    st.text(resume_text[:1000])  # Preview first 1000 characters

    if st.button("Analyze"):
        with st.spinner("Analyzing with AI..."):
            ai_feedback = analyze_resume(resume_text)
        st.subheader("📊 AI Feedback")
        st.write(ai_feedback)
