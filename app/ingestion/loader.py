from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

DATA_PATH = "data"

def load_documents():

    text_loader = DirectoryLoader(
        DATA_PATH,
        glob="**/*.txt",
        loader_cls=TextLoader
    )

    pdf_loader = DirectoryLoader(
        DATA_PATH,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )

    text_documents = text_loader.load()

    try:
        pdf_documents = pdf_loader.load()
    except:
        pdf_documents = []

    documents = text_documents + pdf_documents

    return documents

def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(
        documents
    )

    return chunks