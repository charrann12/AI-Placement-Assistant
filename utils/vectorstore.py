from langchain_classic.vectorstores import Chroma 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.schema import Document

import os
import shutil

PERSIST_DIRECTORY = "chroma_db"


if os.path.exists(PERSIST_DIRECTORY):
    shutil.rmtree(PERSIST_DIRECTORY)



def get_embeddings():
    ## Initialise HuggingFace Embeddings
    
    return HuggingFaceEmbeddings(
        model_name ="sentence-transformers/all-MiniLM-L6-v2"
    )

def create_vector_store(chunks: list[Document]):
    ## Create and persist Chroma DB from document chunks 

    if os.path.exists(PERSIST_DIRECTORY):
        shutil.rmtree(PERSIST_DIRECTORY)
    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents = chunks,
        embedding = embeddings,
        persist_directory = PERSIST_DIRECTORY
    )

    return vector_store


def load_vector_store():
    ## Load existing Chroma DB
    embeddings = get_embeddings()
    vector_store = Chroma(
        embedding_function = embeddings,
        persist_directory = PERSIST_DIRECTORY
    )

    return vector_store


def get_retriever():

    #Create retriever for Chroma DB

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_type = "similarity",
        search_kwargs={"k":3}
    )
    return retriever


