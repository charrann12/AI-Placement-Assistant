import streamlit as st 
import os 
from dotenv import load_dotenv 
load_dotenv()
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS



os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("langsmith_api_key")
os.environ["LANGCHAIN_PROJECT"] = "Placement-Assistant"


## Streamlit App Setup 

## API key
groq_api_key = st.sidebar.text_input("Enter your GROQ api Key", type="password")

st.title("AI Placement Assistant")
st.write("Upload your resume here for analysis")


## Vector Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)


if groq_api_key:
    llm = ChatGroq(
        groq_api_key = groq_api_key,
        model = "openai/gpt-oss-120b",
        streaming = True
    )

    session_id = st.text_input("Session Id", value = "default session")

    ## to manage chat history statefully 
    if 'store' not in st.session_state:
        st.session_state.store = {}
    
    uploaded_resume = st.file_uploader("Upload your Resume", type = "pdf", accept_multiple_files = False)

    if uploaded_resume:
        documents = []
        temppdf = f"./temp.pdf"
        with open(temppdf, "wb") as file:
            file.write(uploaded_resume.getvalue())
            file_name = uploaded_resume.name
        
        loader = PyPDFLoader(temppdf)
        docs = loader.load()
        documents.extend(docs)


        ## splitting and creating embeddings for the documents 
        chunk_size = 500
        chunk_overlap = 100
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
        docs = text_splitter.split_documents(documents)
        
        #To trace the chunks in langsmith
        for doc in docs:
            doc.metadata["chunk_size"] = chunk_size
            doc.metadata["chunk_overlap"] = chunk_overlap

        #building vector database
        if "vectorstore" not in st.session_state:
            st.session_state.vectorstore = FAISS.from_documents(documents = docs, embedding = embeddings)

        vectorstore = st.session_state.vectorstore

        ## retrieval
        ## Using history aware retriever along with hybrid search for better retrival process

        retriever = vectorstore.as_retriever(search_kwargs = {"k":4})

        query = st.text_input("Ask a question about your resume")

        if query:
            with st.spinner("Analysing Resume"):
                retrieved_docs = retriever.invoke(query)
                context = "\n\n".join(
                    [doc.page_content for doc in retrieved_docs]
                )
        

                ## Prompt for the model 

                prompt = f""" 
                You are an AI Placement Assistant.
                Answer the questions using only the resume context below.
                Resume context:
                {context}
                Question:
                {query}
                """

                ## Streaming response
                response_placeholder = st.empty()
                full_response = ""
                for chunk in llm.stream(prompt):
                    full_response+=chunk.content
                    response_placeholder.markdown(full_response)


else:
    st.warning("Please enter your API Key")

