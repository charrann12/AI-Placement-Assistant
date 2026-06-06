from schemas.skill_gap_schema import SkillGapReport

def skill_gap_analyser(llm,vector_store,  jd):

    retriever = vector_store.as_retriever(
        search_kwargs={"k":5}
    )

    docs = retriever.invoke(jd)

    resume_text = "\n".join(
        [doc.page_content for doc in docs]
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