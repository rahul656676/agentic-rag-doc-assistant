from app.services.llm import get_llm

def grade_documents(state):

    llm = get_llm()

    query = state["query"]

    documents = state["documents"]

    filtered_docs = []

    for doc in documents:

        prompt = f"""
You are a document relevance grader.

Determine whether the document is relevant to the user question.

Question:
{query}

Document:
{doc.page_content}

Reply ONLY with:
YES
or
NO
"""

        response = llm.invoke(prompt)

        decision = response.content.strip().upper()

        if "YES" in decision:
            filtered_docs.append(doc)

    return {
        "filtered_documents": filtered_docs
    }