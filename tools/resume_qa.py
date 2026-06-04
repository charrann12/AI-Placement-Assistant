from langchain_core.prompts import ChatPromptTemplate
from utils.vectorstore import get_retriever

def resume_qa_tool(llm, question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs 
    )
    prompt = ChatPromptTemplate.from_template(
        """
        You are an expert placement mentor.

        Answer the question using ONLY the context provided.

        Resume Context:
        {context}

        Question:
        {question}

        If the answer is not present in the resume,
        say "This information is not available in the resume."
        """
    )
    chain = prompt|llm

    response = chain.invoke(
        {
            "context":context,
            "question":question
        }
    )

    return response.content