from langgraph.graph import StateGraph, END

from app.state import GraphState

from app.nodes.query_analyzer import analyze_query
from app.nodes.retriever import retrieve_documents
from app.nodes.grader import grade_documents
from app.nodes.generator import generate_answer
from app.nodes.query_rewriter import rewrite_query

workflow = StateGraph(GraphState)

workflow.add_node(
    "analyze_query",
    analyze_query
)

workflow.add_node(
    "retrieve_documents",
    retrieve_documents
)

workflow.add_node(
    "grade_documents",
    grade_documents
)

workflow.add_node(
    "generate_answer",
    generate_answer
)

workflow.add_node(
    "rewrite_query",
    rewrite_query
)

workflow.set_entry_point(
    "analyze_query"
)

workflow.add_edge(
    "analyze_query",
    "retrieve_documents"
)

workflow.add_edge(
    "retrieve_documents",
    "grade_documents"
)

def decide_next_step(state):

    filtered_docs = state["filtered_documents"]

    retries = state["retries"]

    if len(filtered_docs) > 0:
        return "generate"

    if retries >= 2:
        return "generate"

    return "rewrite"

workflow.add_conditional_edges(
    "grade_documents",
    decide_next_step,
    {
        "generate": "generate_answer",
        "rewrite": "rewrite_query"
    }
)

workflow.add_edge(
    "rewrite_query",
    "retrieve_documents"
)

workflow.add_edge(
    "generate_answer",
    END
)

graph = workflow.compile()