from schemas.ats_schema import ATSReport

from utils.token_counter import count_tokens

def ats_checker(llm, vector_store, jd):

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 4}
    )

    docs = retriever.invoke(jd)

    resume_text = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
    Compare the candidate's resume against the job description.

    Provide:

    1. ATS Score (out of 100)
    2. Matching Keywords
    3. Missing Keywords
    4. Actionable Suggestions

    Resume Context:
    {resume_text}

    Job Description:
    {jd}
    """
    print("ATS Tokens:", count_tokens(prompt))

    structured_llm = llm.with_structured_output(
        ATSReport
    )

    response = structured_llm.invoke(prompt)

    return response