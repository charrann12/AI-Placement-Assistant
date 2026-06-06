from schemas.interview_schema import InterviewReport


def interview_questions(llm,vector_store,  target_role):

    retriever = vector_store.as_retriever(
        search_kwargs={"k":5}
    )

    docs = vector_store.similarity_search(
        target_role,
        k = 10
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

    - 5 Easy Questions
    - 5 Medium Questions
    - 5 Hard Questions

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

    structured_llm = llm.with_structured_output(
        InterviewReport
    )

    response = structured_llm.invoke(prompt)

    return response