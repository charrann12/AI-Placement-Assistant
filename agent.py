from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

from tools.agent_tools import create_tools

memory = MemorySaver()

def build_agent(llm, documents, vector_store):

    tools = create_tools(
        llm,
        documents,
        vector_store
    )

    agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a placement assistant.

You MUST use a tool for every user request.

Never answer directly.

Available tools:

- resume_analysis_agent_tool
- ats_checker_agent_tool
- interview_questions_agent_tool
- resume_qa_agent_tool
- skill_gap_agent_tool

If user asks interview questions,
ALWAYS call interview_questions_agent_tool.

If user asks projects, skills, education,
ALWAYS call resume_qa_agent_tool.

Do not generate your own answers.
Only return tool outputs.
"""
        
    )

    return agent