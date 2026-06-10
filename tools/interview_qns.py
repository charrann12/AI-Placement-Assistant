from schemas.interview_schema import InterviewReport
from utils.token_counter import count_tokens

def interview_questions(llm,vector_store,  target_role):

    retriever = vector_store.as_retriever(
        search_kwargs={"k":5}
    )

    docs = vector_store.similarity_search(
        target_role,
        k = 4
    )

    resume_text = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
    You are a hiring manager interviewing for a {target_role} role.

    Analyze the candidate's resume.

    Resume:
    {resume_text}

    Generate:

    - 3 Easy Questions
    - 3 Medium Questions
    - 3 Hard Questions

    For every question provide:

    - question
    - difficulty
    - expected answer

    Questions should cover:
    - Technical Concepts
    - Projects
    - DSA
    - CS Fundamentals
    - Behavioral Topics

    Tailor everything to a {target_role} position.
    """
    print("Interview Tokens:", count_tokens(prompt))

    structured_llm = llm.with_structured_output(
        InterviewReport
    )

    response = structured_llm.invoke(prompt)

    return response