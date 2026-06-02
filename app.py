import streamlit as st
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

from utils.pdf_loader import load_pdf

from tools.resume_analysis import resume_analysis_tool
from tools.ats_checker import ats_checker_tool
from tools.interview_qns import interview_questions_tool

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("langsmith_api_key")
os.environ["LANGCHAIN_PROJECT"] = "Placement-Assistant"

st.title("AI Placement Assistant")

feature = st.selectbox(
    "Choose the feature",
    [
        "Resume Analysis",
        "ATS Score Checker",
        "Interview questions",
        "Resume Q&A"
    ]
)

groq_api_key = st.sidebar.text_input("Enter your groq api key", type = "password")

if groq_api_key:
    llm = ChatGroq(
        groq_api_key = groq_api_key,
        model = "openai/gpt-oss-120b",
        streaming = True
    )

    uploaded_resume = st.file_uploader(
        "Upload resume",
        type="pdf",
        accept_multiple_files = True
    )

    if uploaded_resume:
        documents = []

        for file in uploaded_resume:
            docs = load_pdf(file)
            documents.extend(docs)
    
    ## Resume Analysis tool calling 

    if feature == "Resume Analysis":
        if st.button("Analyse Resume"):

            result = resume_analysis_tool(
                llm,
                documents
            )

            st.write(result)
    
    ## ATS Score checker tool calling 

    elif feature == "ATS Score Checker":
        jd = st.text_area("Paste the Job Description for better analysis")
        
        if st.button("Check Score"):

            result = ats_checker_tool(
                llm,
                documents
            )

            st.write(result)

    ## Interview questions tool

    elif feature == "Interview questions":
        target_role = st.text_input("Target role", placeholder = "Software Engineer, AI Engineer, ML Engineer...")
        if st.button("Ask questions"):
            result = interview_questions_tool(
                llm,
                documents
            )

            st.write(result)


else:
    st.warning("Please enter your GROQ API key")       

