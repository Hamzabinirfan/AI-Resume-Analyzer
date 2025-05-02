import streamlit as st
import os
from utils.parser import extract_text_from_pdf
from utils.similarity import get_similarity_scores

# Page configuration must be the first Streamlit command
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# Custom styles
st.markdown("""
    <style>
        .title {
            font-size: 30px;
            color: #4CAF50;
            font-weight: bold;
            text-align: center;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            margin-top: 50px;
            color: gray;
        }
        .footer a {
            color: #4CAF50;
            text-decoration: none;
        }
        .match-result {
            font-size: 18px;
            font-weight: bold;
        }
        .header {
            background-color: #f4f4f9;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .resume-upload, .job-description {
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Display title and name
st.markdown('<h1 class="title">📄 AI Resume Analyzer</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="header">Created by Hamza Ansari</h3>', unsafe_allow_html=True)

st.write("Upload resumes and a job description to get match scores.")

# Resume file upload
uploaded_resumes = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)

# Job description input
job_description = st.text_area("Paste Job Description here")

# Analyze button
if st.button("Analyze") and uploaded_resumes and job_description:
    resume_texts = []
    resume_names = []

    for uploaded_file in uploaded_resumes:
        text = extract_text_from_pdf(uploaded_file)
        resume_texts.append(text)
        resume_names.append(uploaded_file.name)

    scores = get_similarity_scores(resume_texts, job_description)
    results = sorted(zip(resume_names, scores), key=lambda x: x[1], reverse=True)

    st.subheader("📊 Match Results")
    for name, score in results:
        st.markdown(f'<p class="match-result">{name} - {score:.2f}% match</p>', unsafe_allow_html=True)

# Footer with LinkedIn link
st.markdown("""
    <div class="footer">
        <p>Find more about me on <a href="https://www.linkedin.com/in/hamza-ansari-176007220/" target="_blank">LinkedIn</a></p>
    </div>
""", unsafe_allow_html=True)
