from mcp.server.mcpserver import MCPServer

from rag_pipeline import answer_question as answer_question_impl
from rag_pipeline import refresh_corpus as refresh_corpus_impl
from rag_pipeline import retrieve_context as retrieve_context_impl

mcp = MCPServer("Student Enrolment RAG MCP")
AVAILABLE_TOOLS = ["refresh_corpus", "retrieve_context", "answer_question"]

# Rag workflow: Data/Files → Corpus → Chunks → Vectors → ChromaDB → Retrieve Top-k Chunks → LLM → Answer + Citations
# example: students.pdf → Corpus → Chunk 12: "John is enrolled in ASD101" → Vector → ChromaDB → Retrieve Top 5 → LLM → "John is enrolled in ASD101" + Citation: students.pdf, Chunk 12

@mcp.tool()
def refresh_corpus(caller: str = "student"):
    return refresh_corpus_impl(caller=caller)


@mcp.tool()
def retrieve_context(query: str, k: int = 5, caller: str = "student"):
    return retrieve_context_impl(query=query, k=k, caller=caller)


@mcp.tool()
def answer_question(query: str, k: int = 5, caller: str = "student"):
    return answer_question_impl(query=query, k=k, caller=caller)


if __name__ == "__main__":
    print("Starting Student Enrolment RAG MCP Server...")
    print("Server status: RUNNING")
    print("Interact with RAG tools from a second terminal.")
    print("Available tools:")
    for tool in AVAILABLE_TOOLS:
        print(f"- {tool}")
    mcp.run()