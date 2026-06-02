def interview_questions_tool(llm, documents):
    resume_text = "\n".join(
        [doc.page_content for doc in documents]
    )
    prompt = f"""
    You are a hiring manager interviewing for a {target_role} role.

    Analyze the candidate's resume and generate realistic interview questions.

    Resume:
    {resume_text}

    Generate:

    1. Easy Questions (5)
    2. Medium Questions (10)
    3. Hard Questions (5)

    Include:
    - Technical Questions
    - Project-Based Questions
    - CS Fundamentals Questions
    - Behavioral Questions

    For every question provide:
    - Question
    - Expected Answer Outline
    - Difficulty Level

    Tailor all questions specifically for a {target_role} position.
    """
    result = llm.invoke(prompt)

    return result.content