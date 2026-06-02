def resume_analysis_tool(llm, documents):

    resume_text = "\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = f"""
    Analyze this resume.

    Return the response in the following format:

    ## Strengths
    - Point 1
    - Point 2

    ## Weaknesses
    - Point 1
    - Point 2

    ## Suggestions
    - Point 1
    - Point 2

    Resume:
        {resume_text}
    """

    result =  llm.invoke(prompt)

    return result.content