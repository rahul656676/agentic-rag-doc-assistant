def analyze_query(state):

    query = state["query"]

    rewritten_query = query.strip()

    return {
        "rewritten_query": rewritten_query
    }