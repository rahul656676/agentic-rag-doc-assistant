# Agentic RAG Documentation Assistant

An advanced Agentic Retrieval-Augmented Generation (RAG) system built using LangGraph, FastAPI, ChromaDB, and Groq LLMs.

This project implements a self-corrective AI workflow capable of:
- semantic document retrieval
- document relevance grading
- conditional query rewriting
- grounded answer generation
- dynamic PDF/TXT ingestion

---

# Features

## Agentic RAG Workflow
- Built using LangGraph
- Multi-step AI workflow execution
- Stateful graph orchestration

## Semantic Retrieval
- ChromaDB vector database
- Sentence-transformer embeddings
- Similarity-based retrieval

## Self-Corrective RAG
- LLM-based document grading
- Query rewriting
- Retry mechanism
- Hallucination reduction

## Dynamic Document Upload
- Upload TXT/PDF files
- Automatic ingestion
- Automatic vector indexing

## FastAPI Backend
- REST API endpoints
- Swagger documentation
- JSON responses

---

# Tech Stack

- FastAPI
- LangGraph
- ChromaDB
- LangChain
- Groq LLM
- Sentence Transformers
- Python

---

# Workflow Architecture

User Query
↓
Query Analyzer
↓
Retriever
↓
Document Grader
↓
Relevant Documents?
├── YES → Generate Answer
└── NO → Rewrite Query → Retry Retrieval

---

# API Endpoints

## POST /query
Query the RAG system.

### Example Request
```json
{
  "query": "What is LangGraph?"
}
```

---

## POST /upload
Upload TXT/PDF documents for indexing.

---

## GET /documents
Returns total indexed documents.

---

## POST /feedback
Submit user feedback.

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd agentic-rag-doc-assistant
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

---

# Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

# Swagger API Docs

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Project Structure

```text
agentic-rag-doc-assistant/
│
├── app/
│   ├── nodes/
│   ├── services/
│   ├── ingestion/
│   ├── utils/
│   ├── graph.py
│   ├── state.py
│   └── main.py
│
├── data/
├── chroma_db/
├── README.md
├── requirements.txt
└── .env
```

---

# Future Improvements

- Streamlit/React frontend
- Hybrid search
- Reranking
- Multi-agent workflows
- Conversation memory
- Docker deployment

---

# Author

Rahul Jangir