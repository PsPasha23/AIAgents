import streamlit as st
from llm_service import ask_ai
from resume_prompt import resume_analysis_prompt_builder
from resume_service import extract_resume_text


st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="wide")
st.title("Resume Analyzer")
st.write("Upload a resume and optionally a job description to get a detailed analysis of the resume in the context of the job description.")
st.sidebar.title("About this App")
st.sidebar.write(
    """
This app helps you analyze your resume in the context of a job description.

User Interface -> Upload Resume and Job Description -> Get Resume Analysis
"""
)

st.sidebar.markdown("---")
st.sidebar.subheader("Instructions")
st.sidebar.write(
    """
For best results: 
- Upload a clean PDF, TXT or Docx file
- Add a job description for proper matching
- Do not upload any sensitive personal data
    """
)

uploaded_file = st.file_uploader("Upload your resume (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

manual_resume_txt = st.text_area("Or paste your resume text here (optional)", height=200)

job_description = st.text_area("Paste the job description here (optional)", height=200)

resume_text = ""

if uploaded_file:
    try:
        resume_text = extract_resume_text(uploaded_file)
    except Exception as e:
        st.error(f"Error extracting text from the uploaded file: {e}")

elif manual_resume_txt:
    resume_text = manual_resume_txt.strip()
    
if resume_text:
    with st.expander("Resume Text Preview", expanded=False):
        st.write(resume_text[:5000])
    
    st.caption(f"Extracted resume text length: {len(resume_text)} characters")
    
st.markdown("---")
analyze_button = st.button("Analyze Resume", type="primary")

if analyze_button:
    if not resume_text:
        st.error("Please upload a resume or paste the resume text before analyzing.")
    else:
        with st.spinner("Analyzing the resume..."):
            prompt = resume_analysis_prompt_builder(resume_text[:15000], job_description[:8000])
            
            messages = [
                {
                    "role": "system",
                    "content": "You are honest resume analyzer and career coach. Provide constructive feedback based on the resume and job description provided. Focus on strengths, weaknesses, missing keywords, and actionable improvements."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]            
            
            analysis_result = ask_ai(messages)
            st.subheader("Resume Analysis Report")
            st.markdown(analysis_result)
            
            st.download_button(
                label="Download Analysis Report",
                data=analysis_result,
                file_name="resume_analysis_report.md",
                mime="text/markdown"
            )
        st.markdown("---")    
