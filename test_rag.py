from app.graph import graph

query = "What is LangGraph?"

initial_state = {
    "query": query,
    "rewritten_query": "",
    "documents": [],
    "filtered_documents": [],
    "answer": "",
    "retries": 0
}

result = graph.invoke(initial_state)

print("\nFINAL ANSWER:\n")

print(result["answer"])