from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

import shutil
import os

from app.graph import graph
from app.services.vectorstore import get_vectorstore

from app.ingestion.ingest import ingest_documents

app = FastAPI(
    title="Agentic RAG Documentation Assistant"
)

UPLOAD_DIR = "data"

class QueryRequest(BaseModel):
    query: str

class FeedbackRequest(BaseModel):
    feedback: str
    comment: str = ""

@app.get("/")
def home():

    return {
        "message": "Agentic RAG API Running"
    }

@app.post("/query")
def query_rag(request: QueryRequest):

    initial_state = {
        "query": request.query,
        "rewritten_query": "",
        "documents": [],
        "filtered_documents": [],
        "answer": "",
        "retries": 0
    }

    result = graph.invoke(initial_state)

    sources = []

    for i, doc in enumerate(
        result["filtered_documents"],
        1
    ):

        sources.append({
            "source_id": i,
            "content": doc.page_content,
            "retrieval_score": doc.metadata.get(
                "retrieval_score",
                None
            )
        })

    return {
        "query": request.query,
        "answer": result["answer"],
        "total_sources": len(sources),
        "sources": sources
    }

@app.get("/documents")
def list_documents():

    vectorstore = get_vectorstore()

    collection = vectorstore.get()

    return {
        "total_documents": len(collection["documents"])
    }

@app.post("/upload")
def upload_document(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    ingest_documents()

    return {
        "message": f"{file.filename} uploaded successfully"
    }

@app.post("/feedback")
def submit_feedback(
    request: FeedbackRequest
):

    return {
        "status": "Feedback received",
        "feedback": request.feedback,
        "comment": request.comment
    }