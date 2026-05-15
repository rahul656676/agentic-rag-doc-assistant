from langchain_chroma import Chroma
from app.services.embeddings import get_embedding_model

CHROMA_PATH = "chroma_db"

def get_vectorstore():
    embedding_model = get_embedding_model()

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_model
    )

    return vectorstore