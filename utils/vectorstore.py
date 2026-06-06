from langchain_community.vectorstores import FAISS 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.schema import Document

import os


def get_embeddings():
    ## Initialise HuggingFace Embeddings
    
    return HuggingFaceEmbeddings(
        model_name ="sentence-transformers/all-MiniLM-L6-v2"
    )

def create_vector_store(chunks: list[Document]):
    ## Create document chunks
    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        documents = chunks,
        embedding = embeddings
    )

    return vector_store



def get_retriever(vector_store):

    #Create retriever
    retriever = vector_store.as_retriever(
        search_type = "mmr",
        search_kwargs={"k":4,
                       "fetch_k":10}
    )
    return retriever


