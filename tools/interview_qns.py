from schemas.interview_schema import InterviewReport

def interview_questions(llm, documents, target_role):
    resume_text = "\n".join(
        [doc.page_content for doc in documents]
    )
    prompt = f"""
    You are a hiring manager interviewing for a {target_role} role.

    Analyze the candidate's resume.

    Resume:
    {resume_text}

    Generate:

    - 5 Easy Questions
    - 10 Medium Questions
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