from schemas.ats_schema import ATSReport



def ats_checker(llm, documents, jd=None):

    resume_text = "\n".join(
        [doc.page_content for doc in documents]
    )

    if jd:
        prompt = f"""
        Compare resume against the job description.

        Give
        - ATS score /100
        - Matching keywords
        - Missing keywords
        - Suggestions 

        resume:
        {resume_text}

        job description:
        {jd}
        """
    
    else :
        prompt = f"""
        Evaluate resume against general ATS standards.

        Give
        - ATS score /100
        - Missing Sections
        - Suggestions 

        resume:
        {resume_text}

        """

    structured_llm = llm.with_structured_output(
        ATSReport
    )

    response = structured_llm.invoke(prompt)

    return response