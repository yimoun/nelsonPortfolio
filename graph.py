# LangGraph agent definition
from langgraph.graph import StateGraph
from langchain_core.messages import AIMessage
from state import AgentState
from orchestrator import limited_stream

# LangGraph node
async def llm_node(state: AgentState) -> AgentState:
    content = ""
    async for chunk in limited_stream(state["messages"]):
        content += chunk.content
    return {"messages": [AIMessage(content=content)]}

# Build graph
graph = StateGraph(AgentState)
graph.add_node("llm", llm_node)
graph.set_entry_point("llm")
graph.set_finish_point("llm")


agent = graph.compile()
