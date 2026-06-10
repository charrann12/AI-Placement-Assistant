from langchain_core.prompts import ChatPromptTemplate
from utils.vectorstore import get_retriever

from utils.token_counter import count_tokens

def resume_qa(llm, vector_store,question):
    
    #print("Step 1")

    retriever = vector_store.as_retriever(
        search_kwargs={"k":3}
    )

    #print("Step 2")

    docs = retriever.invoke(question)

    #print("Step 3")
    
    context = "\n\n".join(
        doc.page_content for doc in docs 
    )
    prompt = ChatPromptTemplate.from_template(
        """
        You are a QnA expert.

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

    print("Resume QA Context Tokens:", count_tokens(context))
    
    response = chain.invoke(
        {
            "context":context,
            "question":question
        }
    )

    return response.content