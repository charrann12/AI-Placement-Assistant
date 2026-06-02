# 🚀 AI Placement Assistant

An AI-powered career companion built to help students improve their resumes, optimize ATS performance, and prepare for technical interviews.

The application leverages Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and modern AI engineering practices to provide personalized career guidance from a single resume upload.

---

## ✨ Features

### 📄 Resume Analysis

Get detailed feedback on your resume, including:

* Strengths
* Weaknesses
* Missing sections
* Formatting suggestions
* Resume improvement recommendations

---

### 🎯 ATS Score Checker

Evaluate your resume against ATS (Applicant Tracking Systems).

**Outputs include:**

* ATS Score (/100)
* Missing Keywords
* Skill Gaps
* ATS Optimization Suggestions

**Optional:** Paste a Job Description (JD) for a more realistic ATS evaluation.

---

### 🎤 Interview Question Generator

Generate personalized interview questions based on your resume.

Questions are categorized into:

* Technical Questions
* Project-Based Questions
* CS Fundamentals
* Behavioral Questions

Each question includes:

* Why the interviewer asks it
* What a strong answer should contain

---

### 💬 Resume Q&A (In Progress)

Ask questions about your resume using a Retrieval-Augmented Generation (RAG) pipeline.

Example:

> What project is most relevant for an AI Engineer role?

> Which technologies have I used in backend development?

---

## 🏗️ Architecture

```text
                    Resume PDF
                         │
                         ▼
                 PDF Processing
                         │
                         ▼
                LangChain Documents
                         │
                         ▼
                 Feature Selection
        ┌────────────┬─────────────┬─────────────┐
        ▼            ▼             ▼
 Resume Analysis  ATS Checker  Interview Generator
        │            │             │
        └────────────┴─────────────┘
                     │
                     ▼
                 Groq LLM
                     │
                     ▼
                 AI Response
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### LLM

* Groq
* GPT-OSS-120B

### AI Framework

* LangChain

### Embeddings

* HuggingFace Embeddings
* all-MiniLM-L6-v2

### Vector Database

* FAISS

### PDF Processing

* PyPDFLoader

### Monitoring & Observability

* LangSmith

---

## 📂 Project Structure

```text
AI-Placement-Assistant/
│
├── app.py
│
├── tools/
│   ├── resume_analysis.py
│   ├── ats_checker.py
│   ├── interview_questions.py
│   └── resume_qa.py
│
├── utils/
│   ├── pdf_loader.py
│   ├── embeddings.py
│   └── vectorstore.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/charrann12/AI-Placement-Assistant.git

cd AI-Placement-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

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

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
langsmith_api_key=YOUR_LANGSMITH_API_KEY
```

Groq API Key is entered directly through the Streamlit sidebar during runtime.

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

---

## 📸 Workflow

1. Enter Groq API Key
2. Select a Feature
3. Upload Resume
4. Generate AI Insights
5. Improve Resume & Placement Readiness

---

## 🎯 Why This Project?

Most students receive generic career advice.

This project aims to provide:

* Personalized Resume Feedback
* ATS Optimization
* Interview Preparation
* AI-Driven Career Guidance

using modern Generative AI workflows.

---

## 🚀 Future Enhancements

* Skill Gap Analysis
* Personalized DSA Roadmaps
* History-Aware Resume Chat
* LangGraph Agent Workflow
* Job Description Matching
* Resume Tailoring
* Multi-Resume Comparison
* Career Recommendation Engine

---

## 📊 Key Concepts Demonstrated

* LLM Integration
* Prompt Engineering
* Retrieval-Augmented Generation (RAG)
* Vector Search with FAISS
* Document Processing
* Streamlit Application Development
* LangChain Pipelines
* AI Product Architecture
* Modular Software Design

---

## 👨‍💻 Author

**Sai Charan Nethi**

B.Tech Computer Science & Engineering
National Institute of Technology Durgapur

GitHub: https://github.com/charrann12

---

⭐ If you found this project useful, consider starring the repository.
