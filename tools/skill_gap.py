from schemas.skill_gap_schema import SkillGapReport

def skill_gap_analyser(llm, documents, jd):

    resume_text = "\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = f"""
    Compare the resume with the job description.

    Identify:

    1. Matching Skills
    2. Missing Skills
    3. Top Priority Skills 
    4. Learning Roadmap 

    Resume:
    {resume_text}

    Job description:
    {jd}
    """

    structured_llm = llm.with_structured_output(
        SkillGapReport
    )

    response = structured_llm.invoke(prompt)

    return response