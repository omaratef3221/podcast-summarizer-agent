from typing import TypedDict, Annotated
from langchain_core.messages import SystemMessage
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages
from get_transcripts_tools import tools
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition 
from prompt import system_message

llm = ChatOpenAI(
    model="o4-mini",
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2)

sys_msg = SystemMessage(system_message)
llm = llm.bind_tools(tools)

class State(TypedDict):
    messages:Annotated[list, add_messages]
        
def reasoner(state: State):
    return {"messages": llm.invoke([sys_msg] + state["messages"])}

## Graph
graph_builder = StateGraph(State)

graph_builder.add_node("reasoner", reasoner)
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.add_edge(START, "reasoner")
graph_builder.add_conditional_edges("reasoner", tools_condition)
graph_builder.add_edge("tools", "reasoner")

graph = graph_builder.compile()
graph