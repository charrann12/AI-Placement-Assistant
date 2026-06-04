import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from utils.pdf_loader import load_pdf
from utils.vectorstore import create_vector_store

from tools.resume_analysis import resume_analysis
from tools.ats_checker import ats_checker
from tools.interview_qns import interview_questions
from tools.resume_qa import resume_qa

# for agent
from agent import build_agent

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("langsmith_api_key")
os.environ["LANGCHAIN_PROJECT"] = "Placement-Assistant"


if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("AI Placement Assistant")

##
# feature = st.selectbox(
  #  "Choose the feature",
   # [
    #    "Resume Analysis",
     #   "ATS Score Checker",
      #  "Interview questions",
       # "Resume Q&A"
    #]
#)


groq_api_key = st.sidebar.text_input("Enter your groq api key", type = "password")

if groq_api_key:
    llm = ChatGroq(
        groq_api_key = groq_api_key,
        model = "openai/gpt-oss-120b",
        streaming = True
    )
    st.session_state.llm = llm

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

        st.session_state.documents = documents
        create_vector_store(documents)

    ## Resume Analysis tool calling 

    #if feature == "Resume Analysis":
        
     #   if st.button("Analyse Resume"):
            
            #Check whether the resume exist or not
      #      documents = st.session_state.get("documents")
       #     if not documents:
        #        st.warning("Please upload your resume first.")
         #       st.stop()
          #  result = resume_analysis(
           #     llm,
            #    documents
            #)

            #st.write(result)
    
    ## ATS Score checker tool calling 

    #elif feature == "ATS Score Checker":
     #   jd = st.text_area("Paste the Job Description for better analysis")
        
      #  if st.button("Check Score"):
       #     documents = st.session_state.get("documents")
        #    if not documents:
         #       st.warning("Please upload your resume first.")
          #      st.stop()
           ##    llm,
             #   documents,
              #  jd
            #)

            #st.write(result)

    ## Interview questions tool

   # elif feature == "Interview questions":
    #    target_role = st.text_input("Target role", placeholder = "Software Engineer, AI Engineer, ML Engineer...")
     #   if st.button("Ask questions"):
      #      documents = st.session_state.get("documents")
       #     if not documents:
        ##       st.stop()
          #  result = interview_questions(
           #     llm,
            ##   target_role
            #)

            #st.write(result)

    ## Resume Q&A 
    #elif feature == "Resume Q&A":

     #   question = st.text_input(
      #      "Ask anything about your resume"
       # )

        #if st.button("Ask"):
         #   documents = st.session_state.get("documents")
          #  if not documents:
           #     st.warning("Please upload your resume first.")
            #    st.stop()
            #result = resume_qa(
             #   llm,
              #  question
            #)

            #st.write(result)
   


else:
    st.warning("Please enter your GROQ API key")       


## Agent Mode 
st.divider()
st.subheader("🤖 Agent Mode")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "placement_assistant"

config = {
    "configurable":{
        "thread_id":st.session_state.thread_id
    }
}


documents = st.session_state.get("documents")


if documents:

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    agent_query = st.chat_input(
        "Ask the Placement Agent anything..."
    )

    if agent_query:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": agent_query
            }
        )

        with st.chat_message("user"):
            st.markdown(agent_query)

        agent = build_agent(
            llm,
            documents
        )

        response = agent.invoke(
            {
                "messages": st.session_state.messages
            },
            config=config
        )

        assistant_response = response["messages"][-1].content

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_response
            }
        )

        with st.chat_message("assistant"):
            st.markdown(assistant_response)