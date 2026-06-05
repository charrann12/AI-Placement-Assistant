def resume_analysis(llm, documents):

    resume_text = "\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = f"""
    Analyze this resume.

    Provide:

    ## Strengths
    ## Weaknesses
    ## Suggestions

    Resume:
    {resume_text}
    """

    response = llm.invoke(prompt)

    return response.content