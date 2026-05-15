from app.services.llm import get_llm

def rewrite_query(state):

    llm = get_llm()

    original_query = state["query"]

    retries = state["retries"] + 1

    prompt = f"""
Rewrite the following user query to improve document retrieval.

Original Query:
{original_query}

Provide ONLY the rewritten query.
"""

    response = llm.invoke(prompt)

    rewritten_query = response.content.strip()

    return {
        "rewritten_query": rewritten_query,
        "retries": retries
    }