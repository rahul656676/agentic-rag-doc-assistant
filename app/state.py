from typing import TypedDict, List
from langchain_core.documents import Document

class GraphState(TypedDict):

    query: str

    rewritten_query: str

    documents: List[Document]

    filtered_documents: List[Document]

    answer: str

    retries: int