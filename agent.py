from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

from tools.agent_tools import create_tools

memory = MemorySaver()

def build_agent(llm, documents):

    tools = create_tools(
        llm,
        documents
    )

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="""
        You are an AI Placement Assistant.

        Use the available tools whenever appropriate.

        - Resume analysis → analyze strengths and weaknesses
        - ATS checker → compare resume with job descriptions
        - Interview questions → generate role-specific interview questions
        - Resume Q&A → answer questions about the uploaded resume
        """,
        checkpointer = memory
    )

    return agent