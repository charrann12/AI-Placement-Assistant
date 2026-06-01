# AI Placement Assistant 🚀

An AI-powered Placement Assistant built using **LangChain**, **FAISS**, **Hugging Face Embeddings**, **Groq LLMs**, **LangSmith**, and **Streamlit**. The application allows users to upload their resume and ask questions about their profile using Retrieval-Augmented Generation (RAG).

## Features

* 📄 Upload Resume (PDF)
* ✂️ Intelligent Text Chunking
* 🔍 Semantic Search using FAISS Vector Store
* 🤖 Resume Question Answering using Groq LLM
* ⚡ Real-time Streaming Responses
* 📊 LangSmith Tracing and Monitoring
* 🧠 Retrieval-Augmented Generation (RAG)
* 🎯 Context-Aware Resume Analysis

## Tech Stack

### Frontend

* Streamlit

### LLM

* Groq
* GPT OSS 120B

### Embeddings

* Hugging Face Embeddings
* sentence-transformers/all-MiniLM-L6-v2

### Vector Database

* FAISS

### Observability

* LangSmith

### Framework

* LangChain

## Project Workflow

```text
Resume PDF
    ↓
PyPDFLoader
    ↓
RecursiveCharacterTextSplitter
    ↓
HuggingFace Embeddings
    ↓
FAISS Vector Store
    ↓
Retriever
    ↓
Groq LLM
    ↓
Generated Answer
```

## Installation

### Clone Repository

```bash
git clone https://github.com/charrann12/Placement_Assistant.git
cd Placement_Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Mac/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
```

## Run the Application

```bash
streamlit run app.py
```

## LangSmith Integration

The application uses LangSmith for tracing and observability.

Tracked Components:

* Retrieval Latency
* LLM Latency
* Retrieved Chunks
* Prompt Execution
* End-to-End RAG Pipeline

## Current Features

* Resume Upload
* PDF Parsing
* Vector Embeddings
* FAISS Retrieval
* Streaming Responses
* LangSmith Tracing

## Planned Enhancements

* Conversational Memory
* History-Aware Retriever
* Hybrid Search (FAISS + BM25)
* Resume ATS Score Analysis
* Job Description Matching
* Interview Question Generator
* Resume Improvement Suggestions

