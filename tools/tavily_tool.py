from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key= os.getenv("TAVILY_API_KEY")
)


def tavily_search(query):
    response = client.search(
        query= query,
        max_results= 5
    )

    results = []

    for i, r in enumerate(response["results"], 1):
        title   = r.get("title", "Unknown")
        url     = r.get("url", "")
        snippet = r.get("content", "").strip()
        # Keep only the first 300 characters to avoid wall-of-text
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results)
"""
Important Architectural Principle

This function should remain a thin abstraction over Tavily.

Its responsibilities are:

User/Agent Query
       ↓
tavily_search(query)
       ↓
Tavily API
       ↓
Search Results
       ↓
Extract + Clean + Format
       ↓
Return Results to Agent

The function itself should not decide the final answer to the user's question. Its job is only to retrieve and prepare relevant web-search information.

The AI agent is responsible for:

Search Results
      ↓
Understand Results
      ↓
Evaluate Relevance
      ↓
Reason / Synthesize
      ↓
Generate Final Answer

FOCUS: implementation, prioritize reliability, maintainability, security, clean separation of concerns, and suitability for integration into an AI-agent/LangGraph workflow."""