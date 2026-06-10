from schemas.skill_gap_schema import SkillGapReport

from utils.token_counter import count_tokens


def skill_gap_analyser(llm,vector_store,  jd):

    retriever = vector_store.as_retriever(
        search_kwargs={"k":3}
    )

    docs = retriever.invoke(jd)

    resume_text = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Analyze the resume against the job description.

    Return ONLY valid JSON using EXACTLY these keys:

    {{
        "matching_skills": [],
        "missing_skills": [],
        "priority_skills": [],
        "learning_roadmap": []
    }}

    Resume:
    {resume_text}

    Job Description:
    {jd}
"""
    print("Skill Gap Tokens:", count_tokens(prompt))

    structured_llm = llm.with_structured_output(
    SkillGapReport,
    method="json_mode"
)

    response = structured_llm.invoke(prompt)

    return response