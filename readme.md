# 🚀 AI Placement Assistant

An Agentic AI-powered Placement Preparation Platform that helps students analyze resumes, evaluate ATS readiness, prepare for interviews, and interact with their resumes through conversational AI.

Built using **LangChain**, **LangGraph**, **Groq LLMs**, **FAISS**, **Streamlit**, and **LangSmith**.

---

## 🌟 Features

### 📄 Resume Analysis

* Upload a resume in PDF format.
* Get detailed strengths, weaknesses, and improvement suggestions.
* Structured feedback for better resume optimization.

### 🎯 ATS Score Checker

* Compare resumes against a Job Description (JD).
* Generate:

  * ATS Score
  * Matching Keywords
  * Missing Keywords
  * Improvement Suggestions
* Uses structured output with Pydantic models.

### 🎤 Interview Question Generator

* Generates personalized interview questions based on:

  * Resume content
  * Target role
* Covers:

  * Technical Questions
  * Project-Based Questions
  * CS Fundamentals
  * Behavioral Questions
* Categorized by difficulty level.

### 💬 Resume Q&A (RAG)

* Ask questions directly about your resume.
* Uses Retrieval-Augmented Generation (RAG) with FAISS.
* Retrieves relevant resume chunks before generating answers.

### 🤖 Agent Mode

An intelligent agent automatically selects the appropriate tool based on user intent.

Available tools:

* Resume Analysis Tool
* ATS Checker Tool
* Interview Question Generator Tool
* Resume Q&A Tool

The user can simply chat with the assistant without manually selecting a feature.

### 🧠 Conversational Memory

* Multi-turn conversations supported.
* Chat history maintained across interactions.
* LangGraph checkpointing used for memory management.

### 📊 Observability with LangSmith

* End-to-end tracing enabled.
* Tool calls and agent reasoning can be monitored through LangSmith.

---

## 🏗️ Architecture

```text
                    Resume PDF
                         │
                         ▼
                 PDF Loader
                         │
                         ▼
                Document Chunks
                         │
                         ▼
                     FAISS
                         │
                         ▼
               Retrieval Layer
                         │
                         ▼
                  Agent Layer
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
 Resume Analysis    ATS Checker    Interview Generator
         │
         ▼
      Resume Q&A
                         │
                         ▼
                 Groq LLM (GPT-OSS)
                         │
                         ▼
                    Streamlit UI
```

---

## 🛠️ Tech Stack

### LLM & Agent Framework

* LangChain
* LangGraph
* Groq API
* GPT-OSS-120B

### Retrieval

* FAISS
* HuggingFace Embeddings

### Frontend

* Streamlit

### Observability

* LangSmith

### Data Validation

* Pydantic

### Utilities

* Python
* dotenv

---

## 📂 Project Structure

```text
AI-Placement-Assistant/
│
├── app.py
├── agent.py
│
├── tools/
│   ├── resume_analysis.py
│   ├── ats_checker.py
│   ├── interview_qns.py
│   ├── resume_qa.py
│   └── agent_tools.py
│
├── schemas/
│   ├── ats_schema.py
│   └── interview_schema.py
│
├── utils/
│   ├── pdf_loader.py
│   └── vectorstore.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/charrann12/AI-Placement-Assistant.git
cd AI-Placement-Assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
langsmith_api_key=YOUR_LANGSMITH_API_KEY
```

Groq API Key is entered through the Streamlit sidebar.

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📸 Workflow

1. Upload Resume
2. Vector Store Creation
3. Chat with Agent
4. Agent Selects Appropriate Tool
5. Tool Executes
6. Response Returned to User

---

## 🔥 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Tool Calling
* Agentic AI Workflows
* Conversational Memory
* Structured Outputs
* Vector Databases
* Prompt Engineering
* LLM Application Development
* LangGraph Checkpointing
* LangSmith Tracing

---

## 🎯 Future Improvements

* Skill Gap Analyzer
* Learning Roadmap Generator
* Persistent Memory Storage
* Resume Version Comparison
* PDF Report Export
* Mock Interview Simulation
* Multi-Agent Architecture

---

## 👨‍💻 Author

**Sai Charan Nethi**

B.Tech Computer Science & Engineering
National Institute of Technology Durgapur

GitHub: https://github.com/charrann12

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
