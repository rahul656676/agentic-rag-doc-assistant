from app.services.vectorstore import get_vectorstore

def retrieve_documents(state):

    vectorstore = get_vectorstore()

    query = state["rewritten_query"]

    results = vectorstore.similarity_search_with_score(
        query,
        k=3
    )

    documents = []

    for doc, score in results:

        doc.metadata["retrieval_score"] = float(score)

        documents.append(doc)

    return {
        "documents": documents
    }