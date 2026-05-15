from app.services.llm import get_llm

def generate_answer(state):

    llm = get_llm()

    query = state["query"]

    documents = state["filtered_documents"]

    if len(documents) == 0:

        return {
            "answer": "I could not find relevant information in the indexed documents."
        }

    context = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = f"""
You are an expert AI documentation assistant.

Answer the user's question using ONLY the provided context.

If the answer is not found in the context, say:
"I could not find relevant information in the documents."

Provide a clean and detailed technical answer.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }