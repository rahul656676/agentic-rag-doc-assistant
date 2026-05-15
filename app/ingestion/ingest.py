from app.ingestion.loader import load_documents, split_documents
from app.services.vectorstore import get_vectorstore

def ingest_documents():
    print("Loading documents...")

    documents = load_documents()

    print(f"Loaded {len(documents)} documents")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    vectorstore = get_vectorstore()

    vectorstore.add_documents(chunks)

    print("Documents indexed successfully!")

if __name__ == "__main__":
    ingest_documents()